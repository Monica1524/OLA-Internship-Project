# 🚖 OLA Ride Data Analytics Project

**Author: Monica Shree**

**Internship Project — 2025**

---

## 📌 Overview
This project analyzes **OLA ride booking data** using **SQL, Power BI, and Streamlit** to deliver actionable business insights.  

The analysis addresses key questions such as:
- How do ride volumes vary over time?
- What are the top cancellation reasons?
- Which vehicle types drive the most distance and revenue?
- How do customer vs driver ratings compare?

**Deliverables include:**
- SQL schema + analysis queries  
- Power BI dashboard (segmented by business themes)  
- Streamlit interactive dashboard (SQL-backed)  
- Project documentation (GitHub Pages)  

---

## 📂 Repository Structure

OLA_Project/
│── data/
│ └── OLA.db # SQLite database (cleaned dataset)

│── sql/
│ ├── schema.sql # DB schema
│ └── OLA.sql # Analysis queries
│
│── powerbi/
│ └── OLA_Rides.pbix # Power BI report
│ └── screenshots/ # PNG images of each page
│
│── streamlit_app/
│ ├── ola_dashboard.py # Streamlit app
│ └── requirements.txt # Dependencies

│── assets/ # Logos & visuals
│── README.md


---

## 🗄️ Database Schema
Table: **OLA_DataSet**

| Column | Type | Description |
|--------|------|-------------|
| booking_id | TEXT | Unique booking reference (alphanumeric) |
| booking_datetime | TEXT | Date & time of booking |
| booking_status | TEXT | Success / Cancelled by Customer / Cancelled by Driver / Incomplete |
| customer_id | TEXT | Unique customer reference |
| vehicle_type | TEXT | Category of vehicle booked |
| pickup_location | TEXT | Pickup location |
| drop_location | TEXT | Drop location |
| V_TAT | TEXT | Vendor turnaround time |
| C_TAT | TEXT | Customer turnaround time |
| canceled_rides_by_customer | TEXT | Flag if cancelled by customer |
| canceled_rides_by_driver | TEXT | Flag if cancelled by driver |
| incomplete_rides | TEXT | Flag for incomplete rides |
| incomplete_rides_reason | TEXT | Reason for incomplete ride |
| booking_value | REAL | Value of booking (fare) |
| payment_method | TEXT | Payment type (Card, UPI, Wallet, Cash) |
| ride_distance | REAL | Distance traveled |
| driver_ratings | REAL | Rating given to driver |
| customer_rating | REAL | Rating given to customer |
| cancelled_by_customer | INTEGER | 1 if cancelled by customer |
| cancelled_by_driver | INTEGER | 1 if cancelled by driver |
| successful_ride | INTEGER | 1 if successful |

---

## 📊 Business Questions Answered

### 1. Overall
- **Ride Volume Over Time** → Line chart (trend of rides by day/month)
- **Booking Status Breakdown** → Donut chart (Success vs Cancelled vs Incomplete)

### 2. Vehicle Type
- **Top 5 Vehicle Types by Ride Distance**  
- **Average Customer Ratings by Vehicle Type**

### 3. Revenue
- **Revenue by Payment Method**  
- **Top 5 Customers by Total Booking Value**  
- **Ride Distance Distribution per Day**

### 4. Cancellation
- **Cancelled Rides Reasons (Customer)**  
- **Cancelled Rides Reasons (Driver)**  

### 5. Ratings
- **Driver Ratings Distribution** (histogram with bins)  
- **Customer vs Driver Ratings** (clustered column)

---

## 📈 Power BI Dashboard
The Power BI report is structured into 5 pages:

- **Overall** → Ride trends + status breakdown  
- **Vehicle Type** → Distance and ratings by category  
- **Revenue** → Payment breakdown + top customers  
- **Cancellation** → Drill-down into reasons  
- **Ratings** → Compare driver vs customer feedback  

📂 File: `powerbi/OLA_dashboard.pbix`  
📸 Screenshots: `powerbi/screenshots/`

---

## 🌐 Streamlit Dashboard
The **Streamlit dashboard** provides a web-based interface to explore the same insights interactively.

### Features
- Sidebar navigation: **Overall, Vehicle Type, Revenue, Cancellation, Ratings**
- Visuals built with **Plotly** (line, bar, pie, histogram)
- Data queried live from **SQLite (OLA_dataset.db)**

### Run locally
```bash
# create venv
python -m venv venv
venv\Scripts\activate        # Windows

# install deps
pip install streamlit
pip install plotly

# run app
streamlit run streamlit_app/ola_dashboard.py
