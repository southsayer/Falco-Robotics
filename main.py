from flask import Flask, render_template, request
import smtplib

MY_EMAIL = "akshitgaur.sky21@gmail.com"
MY_PASSWORD = "8xZ*XHKJ%7eJbB"
SEND_MAIL = "akshit.gaur1214@gmail.com"

from flask import Flask
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        return render_template("index.html")
    elif request.method == 'POST':
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=SEND_MAIL,
            msg=f"Subject:Got A Message from {name}\n\n{message} and my email is {email}"
        )
        return render_template("index.html", msg_sent=True)




if __name__ == "__main__":
    app.run(debug=True)
