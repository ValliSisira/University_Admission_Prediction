# 🎓 University Admission Prediction with Flask

This project is a web-based University Admission Predictor that estimates the **chance of admission** based on academic metrics like GRE, TOEFL, CGPA, and more. It uses a **Linear Regression model**, and the interface is built with **Flask**.

---

## 🚀 Features

- User-friendly web form for input
- Predicts the probability of admission
- Displays the result with a clean UI
- Custom styling using `style.css`
- Flask-based backend with a trained `.pkl` model

---

## 🧠 Model

The model is trained on the [Admission_Predict_Ver1.1.csv](Admission_Predict_Ver1.1.csv) dataset and saved as:
- `university_rating_linear_model.pkl`

---

## 🖥️ Interface

### 🔹 `index.html`
- Input form for GRE, TOEFL, SOP, LOR, CGPA, and Research experience
- Responsive UI styled with `style.css`

### 🔹 `results.html`
- Displays the predicted **chance of admission** clearly and concisely

---

## 📁 Folder Structure


University_Admission_Prediction/
│
├── admission_flask_app.py # Flask backend
├── university_rating_linear_model.pkl # Trained model
├── Admission_Predict_Ver1.1.csv # Dataset
│
├── templates/
│ ├── index.html # Input form UI
│ └── results.html # Output UI
│
├── static/
│ └── style.css # Styling for HTML pages
│
└── README.md # Project documentation


---

## ⚙️ How to Run the App

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/University_Admission_Prediction.git
   cd University_Admission_Prediction
2. Install dependencies - pip install flask pandas scikit-learn
3. Run the Flask app: python admission_flask_app.py
4. Open browser and view the results.
