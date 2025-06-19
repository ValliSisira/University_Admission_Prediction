from flask import Flask, render_template, request
import numpy as np
import pickle

# Load the trained model
with open("admission_model.pkl", "rb") as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")  # Uses templates/index.html

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get form values
        gre = float(request.form["gre"])
        toefl = float(request.form["toefl"])
        rating = float(request.form["rating"])
        sop = float(request.form["sop"])
        lor = float(request.form["lor"])
        cgpa = float(request.form["cgpa"])
        research = int(request.form["research"])

        # Make prediction
        input_features = np.array([[gre, toefl, rating, sop, lor, cgpa, research]])
        prediction = model.predict(input_features)[0]

        # Return result page with prediction
        return render_template("result.html", prediction=f"{prediction:.2f}")

    except Exception as e:
        return f"<h3>Error: {e}</h3><a href='/'>Back</a>"

if __name__ == "__main__":
    app.run(debug=True)


