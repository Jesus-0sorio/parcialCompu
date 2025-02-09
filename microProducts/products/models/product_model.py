from db.db import db

class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

