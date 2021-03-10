import os

from flask import Flask, render_template, send_from_directory, request

app = Flask(__name__)


@app.route("/")
def my_home():
    return render_template("index.html")


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    error = None
    # return render_template('login.html', error=error)
    return 'form submitted okay!'
