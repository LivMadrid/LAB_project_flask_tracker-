"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)

    html = render_template("student_info.html",
                            first=first,
                            last=last,
                            github=github)

    return html


@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")

@app.route("/student-add") 
def display_student_form():

    return render_template("student_add.html")  


@app.route("/student-add", methods=["POST"])
def student_add():

    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    github_username = request.form.get("github_username")

    make_new_student(first_name, last_name, github_username)

    return redirect("/student-add-succes")


@app.route("/student-add-succes") 
def student_add_succes():

    return  render_template("student_add_succes.html ")


if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True, host="0.0.0.0")
