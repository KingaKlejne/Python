from flask import Flask, render_template, request
from post import Post
import requests
import datetime
import smtplib
import os

app = Flask(__name__)
posts = requests.get("https://api.npoint.io/25839bb60af01ff937e5").json()
all_posts_objects = [Post(post["id"], post["name"], post["date"], post["title"], post["subtitle"], post["body"]) for
                     post in posts]
current_year = datetime.datetime.now().year
MY_EMAIL = "gia80@ethereal.email"
PASSWORD = os.environ.get("PASSWORD")


@app.route('/')
def home():
    return render_template("index.html", all_posts=all_posts_objects, year=current_year)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    else:
        return render_template("contact.html", year=current_year, msg_sent=False)


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP(host="smtp.ethereal.email", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=email_message)


@app.route('/about')
def about():
    return render_template("about.html", year=current_year)


@app.route("/post/<int:index>")
def get_post(index):
    requested_post = None
    for blog_post in all_posts_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post, year=current_year)


if __name__ == "__main__":
    app.run(debug=True)
