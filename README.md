# OLA Ride-Sharing Analytics

Analyzing OLA ride-sharing data to extract actionable insights on ride trends, revenue, cancellations, and ratings. This project uses SQL, Power BI, and Streamlit for analytics and visualization.

---

## **1. Problem Statement**
The rise of ride-sharing platforms has transformed urban mobility. OLA generates vast amounts of data related to ride bookings, driver availability, fare calculations, and customer preferences. The challenge is to convert this data into actionable insights to improve operational efficiency, customer satisfaction, and business strategies.

---

## **2. Business Use Cases**
- Identify peak demand hours and optimize driver allocation.
- Analyze customer behavior for personalized marketing strategies.
- Understand pricing patterns and surge pricing effectiveness.
- Detect anomalies or fraudulent activities in ride data.

---

## **3. Dataset**
- File: `dataset/OLA_Cleaned.xlsx`
- Contains columns such as booking_id, booking_datetime, booking_status, vehicle_type, ride_distance, booking_value, driver_ratings, customer_rating, payment_method, and derived flags (success, cancelled_by_customer, cancelled_by_driver).

---

## **4. Project Approach**

1. **Data Cleaning & Preprocessing**
   - Handle missing values and incorrect formats.
   - Validate numeric ranges (ratings 0–5, distances positive).
   - Remove duplicates and check primary key (`booking_id`).
   - Added derived columns for:
     - `successful_ride` (1 if ride completed)
     - `cancelled_by_customer` (1 if cancelled by customer)
     - `cancelled_by_driver` (1 if cancelled by driver)

2. **SQL Database (SQLite)**
   - Imported cleaned Excel as CSV into SQLite.
   - Fixed datatypes for:
     - `booking_id` → INTEGER PRIMARY KEY
     - `driver_ratings` → REAL
   - Wrote queries to extract insights: successful rides, average distances, cancellations, top customers, revenue, ratings.

3. **Power BI Dashboard**
   - Visualized key metrics:
     - Overall: Ride Volume Over Time, Booking Status Breakdown
     - Vehicle Type: Top 5 Vehicle Types by Ride Distance, Avg Customer Ratings
     - Revenue: Revenue by Payment Method, Top 5 Customers, Ride Distance Distribution
     - Cancellations: Reasons for cancelled rides
     - Ratings: Driver Ratings Distribution, Customer vs Driver Ratings

4. **Streamlit Application**
   - Interactive dashboard replicating Power BI visuals.
   - Sidebar for navigation: Overall, Vehicle Type, Revenue, Cancellation, Ratings.
   - SQL queries fetch live data from SQLite DB.
   - Plots: line charts, bar charts, pie charts using Plotly.

---

## **5. SQL Queries**
All queries are in the `sql_queries/` folder. Examples:

| File | Description |
|------|-------------|
| all_successful_bookings.sql | Retrieve all completed rides |
| avg_ride_distance.sql | Average ride distance per vehicle type |
| cancelled_rides.sql | Count of cancelled rides by customer/driver |
| top_customers.sql | Top 5 customers by total booking value |
| ... | ... |

---

## **6. Streamlit Dashboard**
- Script: `streamlit_app/ola_dashboard.py`
- Run locally:

```bash
pip install -r streamlit_app/requirements.txt
streamlit run streamlit_app/ola_dashboard.py
