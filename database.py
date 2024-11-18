from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class EmailStatus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False)  
    status = db.Column(db.String(50), nullable=False)  
    delivery_status = db.Column(db.String(50), nullable=True) 

    def __repr__(self):
        return f"<EmailStatus {self.email}, Status: {self.status}, Delivery Status: {self.delivery_status}>"
