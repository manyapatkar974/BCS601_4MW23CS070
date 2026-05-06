from flask import Flask, render_template, request

app = Flask(__name__)

# HOME
@app.route("/")
def home():
    return render_template("index.html")


# EVEN OR ODD
@app.route("/evenodd", methods=["GET", "POST"])
def evenodd():

    result = ""

    if request.method == "POST":

        number = int(request.form["number"])

        if number % 2 == 0:
            result = f"{number} is Even"
        else:
            result = f"{number} is Odd"

    return render_template("evenodd.html", result=result)


# LARGEST OF 3 NUMBERS
@app.route("/largest", methods=["GET", "POST"])
def largest():

    result = ""

    if request.method == "POST":

        num1 = int(request.form["num1"])
        num2 = int(request.form["num2"])
        num3 = int(request.form["num3"])

        largest_num = max(num1, num2, num3)

        result = f"Largest Number = {largest_num}"

    return render_template("largest.html", result=result)


# WORD COUNT
@app.route("/wordcount", methods=["GET", "POST"])
def wordcount():

    result = ""

    if request.method == "POST":

        sentence = request.form["sentence"]

        words = sentence.split()

        result = f"Total Words = {len(words)}"

    return render_template("wordcount.html", result=result)


# TEMPERATURE CONVERTER
@app.route("/temp", methods=["GET", "POST"])
def temp():

    result = ""

    if request.method == "POST":

        celsius = float(request.form["celsius"])

        fahrenheit = (celsius * 9/5) + 32

        result = f"Fahrenheit = {fahrenheit:.2f} °F"

    return render_template("temp.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)