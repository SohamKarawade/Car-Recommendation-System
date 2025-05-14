# Car Recommendation System

This project is a lightweight, interpretable, and web-based **Car Recommendation System** designed to suggest suitable cars based on user preferences. It is built using **Python (Flask)** for the backend, **Jupyter Notebook** for data analysis, and **HTML/CSS/JavaScript** for the front end. The system uses a **rule-based filtering** approach instead of complex machine learning models to maintain transparency and simplicity.

---

# Folder Structure

project2 : 1) input > CAR DETAILS FROM CAR DEKHO.csv/
           2) static > 1) static.js
                       2) style.css
                       3) font > static > Lexend-Regular.ttf/
            3) templates > 1) welcome.html
                           2) index.html
                           3) result.html
                           4) contact.html
            4) app.py
            5) python2.py
            6) project3.ipynb

---

# Project Objective

The aim is to build a transparent recommendation system that helps users select cars based on real-world parameters such as:
- Price range
- Fuel type
- Seller type
- Car condition (new/used)
- Driving experience
- Maintenance preference
- Interest in luxury vehicles

---

# Dataset

The dataset contains **4341 rows and 8 columns**, including:
- Car Name
- Year of Purchase
- Selling Price
- Kilometers Driven
- Fuel Type
- Seller Type
- Transmission Type
- Ownership Status

---

# Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS, JavaScript
- **Data Analysis:** Jupyter Notebook, Pandas, NumPy, Matplotlib, Seaborn

---

# Workflow

1. **Data Preprocessing**
   - Handle missing values and outliers
   - Convert year to car age
   - Standardize categorical data

2. **Exploratory Data Analysis (EDA)**
   - Identify trends, brand behaviors, and user preferences
   - Visualize distributions and feature importance

3. **Feature Engineering**
   - Group low-maintenance and luxury brands
   - Derive car age from year

4. **User Input Collection (Front End)**
   - Collects 7 preferences from the user through a form

5. **Rule-Based Filtering (Backend)**
   - Applies sequential filters on the dataset using user preferences
   - Returns top 5 relevant car recommendations

---

# Recommendation Logic (Examples)

- Low maintenance ➝ Maruti, Hyundai, Toyota
- Luxury cars ➝ Audi, BMW, Mercedes-Benz
- Driving experience 1–3 ➝ Only automatic
- New cars ➝ Purchased within last 1–2 years

---

# Key Features

- Fully functional end-to-end recommendation system
- No ML/AI models used — fully interpretable rule logic
- Fast and scalable
- Customizable for future ML integration

---
