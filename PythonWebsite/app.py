from flask import Flask, request, render_template, jsonify
import datetime

app = Flask(__name__)

import DBcm
from appconfig import config


@app.route("/")  # HTTP request:	First page
def homepage():
    return render_template(
        "homepage.html",
        title="Home page",
        heading1=" Welcome!",
        heading2="This is the homepage, below are links you can follow to learn more about:",
    )


@app.route("/personal")  # HTTP request:	GET /personal
def personal():
    return render_template(
        "personal.html",
        title="About me page",
        heading1="Personal Page",
        heading2="This page is just going to include some small information about me.",
    )


@app.route("/cv")  # HTTP request: GET /cv
def cv():
    return render_template(
        "cv.html",
        title="CV Page",
        heading1="CV Application",
        heading2="Please take the time to go through my CV attached below.",
    )


@app.route("/interest")  # HTTP request: GET /interest
def interest():
    return render_template(
        "interest.html",
        title="My interests",
        heading1="Interests/Hobbies",
        heading2="Other hobbies outside of college are:",
    )


@app.route("/computing")  # HTTP request: GET /computing
def computing():
    return render_template(
        "computing.html",
        title="Computing",
        heading1="Computing technology interests",
        heading2="This page is the parent page of the links below which I talk three of my favourite computing technologies.",
    )


@app.route("/graphics")  # HTTP request: GET /computing/ graphics
def graphics():
    return render_template(
        "graphics.html",
        title="Graphics Software",
        heading1="Reasons I find Graphics software interesting",
    )


@app.route("/virtual")  # HTTP request: GET /computing/ graphics
def virtual():
    return render_template(
        "virtual.html",
        title="Virtual Reality",
        heading1="Reasons I find Virtual Reality interesting",
    )


@app.route("/artificial")  # HTTP request: GET /computing/ graphics
def artificial():
    return render_template(
        "artificial.html",
        title="Artifical Intelligence",
        heading1="Reasons I like Artifical Intelligence ",
    )


@app.route("/showform")  # Fill in form page
def display_form():
    return render_template(
        "comment.html", title="Feedback form", heading="Please fill in this form",
    )


@app.route("/commentform", methods=["POST"])  # Page showing details
def save_data():

    email = request.form["email"]
    message = request.form["message"]

    # saving the data into SQL database
    with DBcm.UseDatabase(config) as db:
        SQL = """
            insert into comments
            (email, message)
            values
            (%s, %s)
        """
        db.execute(SQL, (email, message))
    return render_template(
        "message.html", name=email, heading="Thank you for your submission!"
    )


@app.get("/comment")  # Page to details (email/message/time submitted) by visitor
def get_latest_comments():
    with DBcm.UseDatabase(config) as db:
        SQL = """
            select email,message,time
            from comments order by time desc
            limit 10
        """
        db.execute(SQL)
        data = db.fetchall()
    return render_template(
        "viewers.html", data=data, heading="Comments from the visitors.",
    )


# Display data in a json style
@app.get("/getdata")
def get_latest_data():
    with DBcm.UseDatabase(config) as db:
        SQL = """
        select email, message,time   
        from comments order by time desc
        """
        db.execute(SQL)
        data = db.fetchall()
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)  # pragma: no cover
