from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST", "GET"])
def predict():
    if request.method == "POST":
        msg = request.form.get("message")  # Corrected here
        print(msg)  # You can use this to check what the user inputs
        # Implement your sentiment analysis logic here
        return render_template("predict.html", sentiment="Positive or Negative")  # Example sentiment output
    else:
        return render_template("predict.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5151)
