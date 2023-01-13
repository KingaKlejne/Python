import csv
from flask import Flask, redirect, render_template, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from wtforms.fields.html5 import URLField
from wtforms.validators import URL, DataRequired

app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6WlSihBXox7C0sKR6b"
Bootstrap(app)

coffee_rating_emojis = [
    "\u2615",
    "\u2615\u2615",
    "\u2615\u2615\u2615",
    "\u2615\u2615\u2615\u2615",
    "\u2615\u2615\u2615\u2615\u2615",
]
wifi_rating_emojis = [
    "\u2716",
    "\U0001f4aa",
    "\U0001f4aa\U0001f4aa",
    "\U0001f4aa\U0001f4aa\U0001f4aa",
    "\U0001f4aa\U0001f4aa\U0001f4aa\U0001f4aa",
    "\U0001f4aa\U0001f4aa\U0001f4aa\U0001f4aa\U0001f4aa",
]
power_rating_emojis = [
    "\u2716",
    "\U0001F50C",
    "\U0001F50C\U0001F50C",
    "\U0001F50C\U0001F50C\U0001F50C",
    "\U0001F50C\U0001F50C\U0001F50C\U0001F50C",
    "\U0001F50C\U0001F50C\U0001F50C\U0001F50C\U0001F50C",
]


class CafeForm(FlaskForm):
    cafe = StringField("Cafe name", validators=[DataRequired()])
    location_url = URLField(
        "Cafe Location on Google Maps (URL)", validators=[DataRequired(), URL()]
    )
    open_time = StringField("Open time e.g. 8AM", validators=[DataRequired()])
    closing_time = StringField("Closing time e.g. 5:30PM", validators=[DataRequired()])
    coffee_rating = SelectField(
        "coffee rating", validators=[DataRequired()], choices=coffee_rating_emojis
    )
    wifi_rating = SelectField(
        "wifi rating", validators=[DataRequired()], choices=wifi_rating_emojis
    )
    power_outlet = SelectField(
        "power outlet rating", validators=[DataRequired()], choices=power_rating_emojis
    )
    submit = SubmitField("Submit")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
        with open("cafe-data.csv", "a") as csv_file:
            writer_object = csv.writer(csv_file)
            new_row = [
                form.cafe.data,
                form.location_url.data,
                form.open_time.data,
                form.closing_time.data,
                form.coffee_rating.data,
                form.wifi_rating.data,
                form.power_outlet.data,
            ]
            writer_object.writerow(new_row)
            return redirect(url_for("cafes"))
    return render_template("add.html", form=form)


@app.route("/cafes")
def cafes():
    with open("cafe-data.csv", newline="") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=",")
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template("cafes.html", cafes=list_of_rows)


if __name__ == "__main__":
    app.run(debug=True)
