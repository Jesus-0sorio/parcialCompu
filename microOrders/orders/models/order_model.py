from db.db import db

class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userName = db.Column(db.String(255), nullable=False)
    userEmail = db.Column(db.String(255), nullable=False)
    saleTotal = db.Column(db.Integer, nullable=False)

    def __init__(self, userEmail, userName, saleTotal):
        self.userEmail = userEmail
        self.userName = userName
        self.saleTotal = saleTotal

