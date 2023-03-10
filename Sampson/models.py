from Sampson import db



class Tbproductsme(db.Model):

    id = db.Column(db.Integer,primary_key=True)
    mdproductname = db.Column(db.Text,index=True)
    mdproductsmename = db.Column(db.Text)