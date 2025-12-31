# Customer Churn Prediction - Advanced Falsk,Python UI Web App
Using Telco Customer Dataset


Live Project URL: [https://officialranausama.pythonanywhere.com](https://officialranausama.pythonanywhere.com)

---

## Introduction
Welcome to the **Customer Churn Prediction** project. This project is a fully functional, SaaS-style web application that predicts customer churn for businesses. It helps identify which customers are at risk of leaving, allowing businesses to take proactive measures to retain them.  

The web app features an **interactive, professional UI** with dropdowns, input validation, and responsive design, providing a real-time user experience.

---

## Screenshots

![Screenshot 1](https://res.cloudinary.com/daqmobuym/image/upload/v1767189394/xxepc5hil6rpf52wp0xg.png)
![Screenshot 2](https://res.cloudinary.com/daqmobuym/image/upload/v1767189398/uc070qibm15uw4wc5it4.png)


## Features

### UI & UX
- **Professional SaaS-style interface** with hero section and footer.  
- **Dropdown menus** for categorical features such as gender, internet service, and contract type.  
- **Input validation** for numeric values (tenure, monthly charges, total charges).  
- **Responsive design** optimized for desktop and mobile devices.  
- **Live predictions** with instant feedback in colored alert boxes.  
- **Social links** in hero and footer for portfolio and contact.  

### Machine Learning Features
- Uses **Logistic Regression** for customer churn prediction.  
- Input preprocessing includes:
  - Encoding categorical features.
  - Scaling numeric features.
- Aligns input features with trained model for accurate predictions.  

### Advanced Sections
- Hero section with project title, your name, and portfolio/social links.  
- Prediction result displayed in a **dynamic alert box** on form submission.  
- Footer section with consistent branding and social links.  

---

## Dataset
The model is trained on the **Telco Customer Churn dataset**, which contains:
- Demographics
- Service subscriptions
- Customer churn status

The dataset includes both **numerical and categorical variables** and is preprocessed for optimal model performance.  

---

## Project Objectives
1. **Churn Prediction:** Identify customers likely to churn.  
2. **Data Analysis:** Understand customer behavior and key churn indicators.  
3. **Model Building:** Build a Logistic Regression model with preprocessing for real-time prediction.  
4. **Web Integration:** Provide a **user-friendly web interface** to predict churn instantly.  

---

## Data Preprocessing
- **Handling Missing Values:** Ensured data integrity by filling or removing nulls.  
- **Encoding Categorical Variables:** Converted dropdown features into numeric values compatible with the model.  
- **Scaling Numeric Features:** Standardized features like tenure, monthly charges, and total charges.  

---


## How to Use

### 1. Clone the repository:

```
git clone https://github.com/usama1095/predict_telco_customer_churn
```

### 2. Install dependencies

```
pip install -r requirements.txt

```

## 3. Run the Flask app locally:

```
python app.py
```

## 4. Open your browser at 
``` http://127.0.0.1:5000/ ```

## 5. Enter customer details using the interactive form.

## 6. Get real-time predictions whether the customer will stay or churn.

## Dependencies

The project requires the following Python libraries:

```
1. Flask
2. pandas
3. numpy
4. scikit-learn
5. pickle (for saving/loading models)
6. Bootstrap 5 (for UI – via CDN)
```
## Live Demo

Try the live project here: [https://officialranausama.pythonanywhere.com](https://officialranausama.pythonanywhere.com)

License

This project is licensed under the MIT License.

## Author

## Rana Usama

[Fiverr](https://www.fiverr.com/ranausama881)

[GitHub](https://github.com/usama1095)

[Instagram](https://www.instagram.com/ishowtechskills)
