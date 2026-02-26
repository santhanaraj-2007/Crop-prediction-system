
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    n = float(request.form["nitrogen"])
    p = float(request.form["phosphorus"])
    k = float(request.form["potassium"])
    ph = float(request.form["ph"])
    rain = float(request.form["rain"])

    crop = "Crop not matched"
    fertilizer = "General NPK Fertilizer"

    if 160 <= n <= 300 and 60 <= p <= 100 and 80 <= k <= 200 and 6 <= ph <= 7.5 and 150 <= rain <= 300:
        crop = "Sugarcane"
        fertilizer = "Urea + Potash"

    elif 120 <= n < 160 and 40 <= p <= 80 and 40 <= k <= 100 and 6 <= ph <= 7 and 50 <= rain <= 120:
        crop = "Corn"
        fertilizer = "Ammonium Nitrate"

    elif 80 <= n < 120 and 30 <= p <= 50 and 30 <= k <= 50 and 6 <= ph <= 7.5 and 40 <= rain <= 120:
        crop = "Wheat"
        fertilizer = "NPK Mix"

    elif 60 <= n < 80 and 25 <= p <= 50 and 25 <= k <= 50 and 6 <= ph <= 8 and 50 <= rain <= 120:
        crop = "Cotton"
        fertilizer = "Potassium Sulphate"

    elif 40 <= n < 60 and 20 <= p <= 40 and 20 <= k <= 40 and 5.5 <= ph <= 7.5 and 200 <= rain <= 400:
        crop = "Millet"
        fertilizer = "Organic Compost"

    elif 90 <= n <= 150 and 40 <= p <= 60 and 30 <= k <= 60 and 5.5 <= ph <= 6.5 and 100 <= rain <= 200:
        crop = "Paddy"
        fertilizer = "Urea + DAP"

    return render_template("index.html", result_crop=crop, result_fertilizer=fertilizer)


if __name__ == "__main__":
    from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    n = float(request.form["nitrogen"])
    p = float(request.form["phosphorus"])
    k = float(request.form["potassium"])
    ph = float(request.form["ph"])
    rain = float(request.form["rain"])

    crop = "Crop not matched"
    fertilizer = "General NPK Fertilizer"

    if 160 <= n <= 300 and 60 <= p <= 100 and 80 <= k <= 200 and 6 <= ph <= 7.5 and 150 <= rain <= 300:
        crop = "Sugarcane"
        fertilizer = "Urea + Potash"

    elif 120 <= n < 160 and 40 <= p <= 80 and 40 <= k <= 100 and 6 <= ph <= 7 and 50 <= rain <= 120:
        crop = "Corn"
        fertilizer = "Ammonium Nitrate"

    elif 80 <= n < 120 and 30 <= p <= 50 and 30 <= k <= 50 and 6 <= ph <= 7.5 and 40 <= rain <= 120:
        crop = "Wheat"
        fertilizer = "NPK Mix"

    elif 60 <= n < 80 and 25 <= p <= 50 and 25 <= k <= 50 and 6 <= ph <= 8 and 50 <= rain <= 120:
        crop = "Cotton"
        fertilizer = "Potassium Sulphate"

    elif 40 <= n < 60 and 20 <= p <= 40 and 20 <= k <= 40 and 5.5 <= ph <= 7.5 and 200 <= rain <= 400:
        crop = "Millet"
        fertilizer = "Organic Compost"

    elif 90 <= n <= 150 and 40 <= p <= 60 and 30 <= k <= 60 and 5.5 <= ph <= 6.5 and 100 <= rain <= 200:
        crop = "Paddy"
        fertilizer = "Urea + DAP"

    return render_template("index.html", result_crop=crop, result_fertilizer=fertilizer)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5002)