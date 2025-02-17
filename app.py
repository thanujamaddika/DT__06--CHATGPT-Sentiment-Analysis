from flask import Flask, render_template, request, jsonify
from test import TextToNum  # Ensure TextToNum is implemented correctly
import pickle
import os  # For checking file existence

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        msg = request.form.get("message")
        
        if not msg or msg.strip() == "":  # Handle empty input
            return jsonify({"error": "Message input is empty!"}), 400

        print("User Input:", msg)

        # Create an object of TextToNum
        ob = TextToNum(msg)
        ob.cleaner() 
        ob.token()
        ob.removeStop()
        ob.stemme()
        
        # Get processed text from TextToNum object
        st = ob.get_processed_text()  # Ensure this function exists in TextToNum

        if not st:  # If st is empty after processing
            return jsonify({"error": "Processed text is empty!"}), 400

        # Convert list to string (Ensure st is a list)
        if isinstance(st, list):
            stvc = " ".join(st)
        else:
            stvc = st  # If it's already a string

        # Check if Vectorizer.pickle exists
        if not os.path.exists("Vectorizer.pickle"):
            return jsonify({"error": "Vectorizer file not found!"}), 500
        
        # Load the vectorizer
        with open("Vectorizer.pickle", "rb") as vcfile:
            vc = pickle.load(vcfile)

        # Transform text
        try:
            data = vc.transform([stvc])
        except Exception as e:
            return jsonify({"error": f"Vectorization failed: {str(e)}"}), 500

        print("Vectorized Data:", data)

        # Check if model.pickle exists
        if not os.path.exists("model.pickle"):
            return jsonify({"error": "Model file not found!"}), 500

        # Load the model
        with open("model.pickle", "rb") as mbfile:
            model = pickle.load(mbfile)

        # Make prediction
        try:
            pred = model.predict(data)
        except Exception as e:
            return jsonify({"error": f"Model prediction failed: {str(e)}"}), 500

        # Return sentiment result
        sentiment = {0: "Neutral", 1: "Positive", -1: "Negative"}.get(pred[0], "Unknown")
        return jsonify({"result": sentiment})

    else:
        return render_template("predict.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

