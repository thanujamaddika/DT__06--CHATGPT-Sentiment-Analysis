from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        msg = request.form.get("message")
        print(msg)  # Debugging
        return jsonify({"message": msg})  # Return a valid response
    return render_template("predict.html")

if __name__ == "__main__":
    app.run(debug=True)