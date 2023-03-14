from flask import Blueprint, render_template
from Sampson.forms import customerform

mainbp = Blueprint("mainbp", __name__)


@mainbp.route("/",)
def index():
    return render_template("index.html")


@mainbp.route("/customer", methods=["GET","POST"])
def customer():

    form = customerform()

    if form.validate_on_submit():

        print(form.customercomplaint.data)


    return render_template("customer.html", form=form)

@mainbp.route("/analyst", methods=["GET","POST"])
def analyst():

    return render_template("analyst.html")


@mainbp.route("/dataanalyst", methods=["GET","POST"])
def dataanalyst():

    return render_template("dataanalyst.html")