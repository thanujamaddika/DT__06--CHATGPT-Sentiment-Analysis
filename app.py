from flask import Flask, render_template, request, jsonify

app = Flask(_name_)

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

if _name_ == "_main_":
    app.run(debug=True)