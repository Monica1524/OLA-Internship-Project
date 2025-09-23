import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

# --------------------------------
# DB CONNECTION (cached for Streamlit)
# --------------------------------
@st.cache_resource
def get_connection():
    return sqlite3.connect("OLA.db", check_same_thread=False)

def run_query(query):
    conn = get_connection()
    return pd.read_sql_query(query, conn)

# --------------------------------
# PAGE CONFIG
# --------------------------------
st.set_page_config(page_title="OLA Analytics Dashboard", layout="wide")

st.title("🚖 OLA Ride Analytics Dashboard")

# --------------------------------
# SIDEBAR NAVIGATION
# --------------------------------
st.set_page_config(page_title="OLA Dashboard", layout="wide")

st.sidebar.image("assets/ola_logo.png", use_column_width=True)

views = ["Overall", "Vehicle Type", "Revenue", "Cancellation", "Ratings"]
choice = st.sidebar.radio("Select View", views)

# --------------------------------
# 1. OVERALL VIEW
# --------------------------------
if choice == "Overall":
    st.header("📈 Overall Ride Insights")

    # Ride Volume Over Time
    df1 = run_query("""
        SELECT booking_datetime, COUNT(booking_id) AS ride_count
        FROM OLA_Dataset
        WHERE booking_status = 'Success'
        GROUP BY booking_datetime
        ORDER BY booking_datetime
    """)
    fig1 = px.line(df1, x="booking_datetime", y="ride_count", title="Ride Volume Over Time")
    st.plotly_chart(fig1, use_container_width=True)

    # Booking Status Breakdown
    df2 = run_query("""
        SELECT booking_status, COUNT(booking_id) AS total
        FROM OLA_Dataset
        GROUP BY booking_status
    """)
    fig2 = px.pie(df2, names="booking_status", values="total", title="Booking Status Breakdown")
    st.plotly_chart(fig2, use_container_width=True)

# --------------------------------
# 2. VEHICLE TYPE VIEW
# --------------------------------
elif choice == "Vehicle Type":
    st.header("🚗 Vehicle Type Insights")

    df3 = run_query("""
        SELECT vehicle_type, SUM(ride_distance) AS total_distance
        FROM OLA_Dataset
        GROUP BY vehicle_type
        ORDER BY total_distance DESC
        LIMIT 5
    """)
    fig3 = px.bar(df3, x="vehicle_type", y="total_distance", title="Top 5 Vehicle Types by Ride Distance")
    st.plotly_chart(fig3, use_container_width=True)

# --------------------------------
# 3. REVENUE VIEW
# --------------------------------
elif choice == "Revenue":
    st.header("💰 Revenue Insights")

    df4 = run_query("""
        SELECT payment_method, SUM(booking_value) AS revenue
        FROM OLA_Dataset
        WHERE booking_status = 'Success'
        GROUP BY payment_method
    """)
    fig4 = px.bar(df4, x="payment_method", y="revenue", title="Revenue by Payment Method")
    st.plotly_chart(fig4, use_container_width=True)

    df5 = run_query("""
        SELECT customer_id, SUM(booking_value) AS total_value
        FROM OLA_Dataset
        WHERE booking_status = 'Success'
        GROUP BY customer_id
        ORDER BY total_value DESC
        LIMIT 5
    """)
    fig5 = px.bar(df5, x="customer_id", y="total_value", title="Top 5 Customers by Total Booking Value")
    st.plotly_chart(fig5, use_container_width=True)

    df6 = run_query("""
        SELECT date(booking_datetime) AS ride_date, SUM(ride_distance) AS total_distance
        FROM OLA_Dataset
        WHERE booking_status = 'Success'
        GROUP BY ride_date
    """)
    fig6 = px.area(df6, x="ride_date", y="total_distance", title="Ride Distance Distribution Per Day")
    st.plotly_chart(fig6, use_container_width=True)

# --------------------------------
# 4. CANCELLATION VIEW
# --------------------------------
elif choice == "Cancellation":
    st.header("❌ Cancellation Insights")

    df7 = run_query("""
        SELECT incomplete_rides_reason, COUNT(booking_id) AS cancellations
        FROM OLA_Dataset
        WHERE booking_status <> 'Success' AND incomplete_rides_reason <> ''
        GROUP BY incomplete_rides_reason
    """)
    fig7 = px.bar(df7, x="incomplete_rides_reason", y="cancellations",
                  title="Cancelled Rides Reasons", text_auto=True)
    st.plotly_chart(fig7, use_container_width=True)

# --------------------------------
# 5. RATINGS VIEW
# --------------------------------
elif choice == "Ratings":
    st.header("⭐ Ratings Insights")

    df8 = run_query("""
        SELECT driver_ratings
        FROM OLA_Dataset
        WHERE driver_ratings IS NOT NULL
    """)
    fig8 = px.histogram(df8, x="driver_ratings", nbins=10, title="Driver Ratings Distribution")
    st.plotly_chart(fig8, use_container_width=True)

    df9 = run_query("""
        SELECT vehicle_type,
               AVG(driver_ratings) AS avg_driver_rating,
               AVG(customer_rating) AS avg_customer_rating
        FROM OLA_Dataset
        GROUP BY vehicle_type
    """)
    fig9 = px.bar(df9, x="vehicle_type", y=["avg_driver_rating", "avg_customer_rating"],
                  barmode="group", title="Customer vs Driver Ratings by Vehicle Type")
    st.plotly_chart(fig9, use_container_width=True)
