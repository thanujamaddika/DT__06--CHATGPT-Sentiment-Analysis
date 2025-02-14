from flask import Flask, render_template, request, jsonify
from test import TextToNum  # Ensure TextToNum is correctly implemented
import pickle  # Corrected import

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        msg = request.form.get("message")
        print("User Input:", msg)
        
        # Create an object of TextToNum
        ob = TextToNum(msg)
        ob.cleaner() 
        ob.token()
        ob.removeStop()
        ob.stemme()
        
        # Get processed text from the TextToNum object
        st = ob.get_processed_text()  # Make sure this function exists in TextToNum

        if not st:  # Check if st is empty
            return jsonify({"error": "Processed text is empty!"}), 400
        
        stvc = " ".join(st)  # Convert list to string

        # Load the vectorizer
        with open("Vectorizer.pickle", "rb") as vcfile:
            vc = pickle.load(vcfile)

        # Transform text
        data = vc.transform([stvc])
        print("Vectorized Data:", data)

        # Load the model
        with open("model.pickle", "rb") as mbfile:
            model = pickle.load(mbfile)

        # Make prediction
        pred = model.predict(data)
        if pred[0]==0:
            return jsonify({"result":"Neutral"})
        elif pred[0]==1:
            return jsonify({"result":"Positive"})
        else:
            return jsonify({"result":"Negative"})
        return jsonify({"result": str(pred[0])})
    else:
        return render_template("predict.html")

if __name__ == "__main__":
    app.run(debug=True)
