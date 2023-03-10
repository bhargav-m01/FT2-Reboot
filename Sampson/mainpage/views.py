from flask import Blueprint, render_template

mainbp = Blueprint("mainbp", __name__)


@mainbp.route("/",)
def index():
    return render_template("index.html")


@mainbp.route("/customer", methods=["GET","POST"])
def customer():

    return render_template("customer.html")

@mainbp.route("/analyst", methods=["GET","POST"])
def analyst():

    return render_template("analyst.html")