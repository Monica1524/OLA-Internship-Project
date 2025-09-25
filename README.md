# 🚖 OLA Ride Data Analytics Project

**Author: Monica Shree**

**Internship Project — 2025**

---

## 📌 Overview
The OLA Ride Analytics Project aims to analyze customer ride behavior, vehicle usage, revenue streams, cancellations, and ratings.

We leveraged:

SQLite database (for structured storage and querying).

SQL queries (for extracting KPIs).

Power BI dashboards (for business-focused visualization).

Streamlit dashboard (for interactive analytics & deployment).

The goal was to provide data-driven insights for OLA’s operations, cancellations, and customer satisfaction.

---

## 📂 Repository Structure

```
OLA_Project/
│── data/
│ └── OLA_Dataset.xslx
│ └── OLA.db # SQLite database (cleaned dataset)
│── sql/
│ ├── schema.sql # DB schema
│ └── OLA.sql # Analysis queries
│── powerbi/
│ ├── OLA_Rides.pbix # Power BI report
│ └── screenshots/ # PNG images of each page
│── streamlit_app/
│ ├── ola_dashboard.py # Streamlit app
│── assets/ # Logos & visuals
│── README.md

```
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
- File: `dataset/OLA_Dataset.xlsx`
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

## **5. SQL Queries**
-- **1. Retrieve all Successful bookings**:-

SELECT * FROM OLA_DataSet

WHERE booking_status = 'Success';

-- **2. Find the average ride distance for each vehicle type**:-

SELECT 
    vehicle_type,
    AVG(CAST(ride_distance AS REAL)) AS avg_distance

FROM OLA_DataSet

WHERE ride_distance GLOB '[0-9]*'

GROUP BY vehicle_type;

-- **3. Get the total number of cancelled rides by customers**:-

SELECT COUNT(*) AS Total_cancellation_by_customers

FROM OLA_DataSet

WHERE booking_status = 'Canceled by Customer';

-- **4. List the top 5 customers who booked the highest number of rides**:-

SELECT 
    customer_id,
    COUNT(booking_id) AS total_rides

FROM OLA_DataSet

GROUP BY customer_id

ORDER BY total_rides DESC
LIMIT 5;

-- **5. Get the number of rides cancelled by drivers due to personal and car-related issues**:-

SELECT 
    incomplete_rides_reason,
    COUNT(booking_id) AS cancelled_count

FROM OLA_DataSet

WHERE booking_status = 'Canceled by Driver'
  
  AND incomplete_rides_reason IN ('Customer Demand', 'Vehicle Breakdown')

GROUP BY incomplete_rides_reason;

-- **6. Find the maximum and minimum driver ratings for Prime Sedan bookings**:-

SELECT 
    MAX(CAST(driver_ratings AS REAL)) AS max_driver_rating,
    MIN(CAST(driver_ratings AS REAL)) AS min_driver_rating

FROM OLA_DataSet

WHERE vehicle_type = 'Prime Sedan'
  
  AND driver_ratings GLOB '[0-9]*';
  
-- **7. Retrieve all rides where payment was made using UPI**:-

SELECT *

FROM OLA_DataSet

WHERE payment_method = 'UPI';

-- **8. Find the average customer rating per vehicle type**:-

SELECT 
    vehicle_type,
    AVG(CAST(customer_rating AS REAL)) AS avg_customer_rating

FROM OLA_DataSet

WHERE customer_rating GLOB '[0-9]*'

GROUP BY vehicle_type;

-- **9. Calculate the total booking value of rides completed successfully**:-

SELECT 
    SUM(CAST(booking_value AS REAL)) AS total_success_booking_value

FROM OLA_DataSet

WHERE booking_status = 'Success'
  AND booking_value GLOB '[0-9]*';

-- **10. List all incomplete rides along with the reason**:-

SELECT 
    booking_id,
    booking_status,
    incomplete_rides_reason

FROM OLA_DataSet

WHERE booking_status <> 'Success';

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
<img width="1907" height="831" alt="image" src="https://github.com/user-attachments/assets/56360daf-33e4-49c4-8640-2a012b09122c" />
<br/>
<br/>
 
- **Vehicle Type** → Distance and ratings by category
<img width="1907" height="872" alt="image" src="https://github.com/user-attachments/assets/20ac1808-234f-4c99-b13e-87bf166c5171" />
<br/>
<br/>

- **Revenue** → Payment breakdown + top customers
<img width="1917" height="896" alt="image" src="https://github.com/user-attachments/assets/c61681c5-1c9a-459c-acac-7d660fc92d5f" />
<br/>
<br/>

- **Cancellation** → Drill-down into reasons
<img width="1903" height="888" alt="image" src="https://github.com/user-attachments/assets/f0a5647b-8dee-4715-b46e-6ff55f417be1" />
<br/>
<br/>

- **Ratings** → Compare driver vs customer feedback
<img width="1915" height="912" alt="image" src="https://github.com/user-attachments/assets/46d0476d-aa5f-455f-8a03-254e05bcf399" />
<br/>
<br/>


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

```
<img width="1906" height="963" alt="image" src="https://github.com/user-attachments/assets/a0f36fae-c1ac-48ed-b4cc-c0daa5f05044" />
<br/>
<br/>
<img width="1890" height="973" alt="image" src="https://github.com/user-attachments/assets/c5159448-dd30-4cb1-888a-db6c14e1d51d" />
<br/>
<br/>
<img width="1867" height="871" alt="image" src="https://github.com/user-attachments/assets/347c4f5e-a23c-4c96-bce6-cd5583612e85" />
<br/>
<br/>
<img width="1903" height="962" alt="image" src="https://github.com/user-attachments/assets/c5517cfc-6dc8-4de1-9fc5-327ed5bdb570" />
<br/>
<br/>
<img width="1911" height="970" alt="image" src="https://github.com/user-attachments/assets/167ccd1a-29f9-4c94-83c5-e48a9c42e0af" />
<br/>
<br/>
<img width="1833" height="955" alt="image" src="https://github.com/user-attachments/assets/a76df0a7-04ff-4f88-b352-20b5b1e4345b" />
<br/>
<br/>
<img width="1915" height="962" alt="image" src="https://github.com/user-attachments/assets/32d89295-68de-4b54-ac78-e856307ae30f" />
<br/>
<br/>
<img width="1912" height="950" alt="image" src="https://github.com/user-attachments/assets/881f04f4-b5e2-4be5-91f2-2883f90d98d6" />
<br/>
<br/>


---

**Deliverables include:**
- SQL schema + analysis queries  
- Power BI dashboard (segmented by business themes)  
- Streamlit interactive dashboard (SQL-backed)  
- Project documentation (GitHub Pages)  

---


## 6. Business Insights

- ✅ Peak Ride Days: Ride demand is highest on weekends.
- ✅ Popular Vehicles: Sedans & SUVs contribute highest ride distances.
- ✅ Payment Preference: Digital methods (UPI & Wallet) dominate over cash.
- ✅ Customer Loyalty: A few top customers account for significant revenue share.
- ✅ Cancellations: More cancellations are customer-driven (location issues, change of plan).
- ✅ Ratings Gap: Customers tend to rate drivers slightly lower than drivers rate customers.

---

## 7. Conclusion

This project demonstrates how SQL + Power BI + Streamlit can provide a complete end-to-end analytics solution:

SQL → clean, structured data for KPIs.

Power BI → executive-level dashboards.

Streamlit → interactive web app for business users.

🚀 With these insights, OLA can improve customer experience, reduce cancellations, and optimize driver allocation.

---




