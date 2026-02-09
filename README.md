# Customer Churn Prediction System

## Project Overview

This project is a Customer Churn Prediction System built using Machine Learning and Django. The goal of the system is to predict whether a customer is likely to churn (leave the service) based on demographic information, service usage details, and billing-related features.

The application provides a web-based interface where users can enter customer details, select a machine learning model, and obtain churn predictions along with the probability of churn. The system is designed following clean software engineering and ML deployment practices.

---

## Machine Learning Models

The system supports two machine learning models:

- Random Forest Classifier
- XGBoost Classifier

Both models were trained on the Telco Customer Churn dataset with proper preprocessing, feature engineering, and one-hot encoding. Separate feature column mappings and probability thresholds were stored for each model. The user can dynamically select which model to use during prediction.

---

## Project Structure

customer_churn/
├── churn_project/        (Django project settings)
├── predictor/            (Django app: views, forms, preprocessing)
├── templates/            (HTML templates for input and output)
├── Machine Learning/     (Training notebooks – ignored in Git)
├── manage.py
├── Pipfile
├── Pipfile.lock
├── .gitignore
└── README.md

---

## Data Preprocessing

All preprocessing is handled in a dedicated preprocess.py file. The preprocessing pipeline includes:

- Mapping binary and categorical variables to numeric values
- One-hot encoding

---

## Web Application (Django)

The Django web application provides:

- Django Forms for structured and validated input
- Dropdowns and radio buttons to avoid invalid user input
- A clean input page for entering customer details
- A result page displaying:
  - Selected model
  - Churn prediction (1 = Churn, 0 = No Churn)
  - Churn probability as a percentage

The backend loads the appropriate model, applies preprocessing, and performs prediction using predict_proba.

---

## Technology Stack

Backend:
- Django

Machine Learning:
- Scikit-learn
- XGBoost
- Random Forest

Data Processing:
- Pandas
- NumPy
- matplotlib

Model Persistence:
- Joblib

Environment & Version Control:
- Pipenv
- Git and GitHub

---

## Running the Project Locally

1. Clone the repository:
   git clone <repository-url>
   cd customer-churn

2. Install dependencies:
   pipenv install
   pipenv shell

3. Apply migrations:
   python manage.py migrate

4. Run the development server:
   python manage.py runserver

5. Open in browser:
   http://127.0.0.1:8000/


## Author

Mothilal Chowdary  
Machine Learning and Django Developer

---

## Summary

This project demonstrates an end-to-end machine learning workflow integrated with a Django web application. It follows clean architecture, proper version control practices, making it suitable for both academic and industry use.
