from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Asset(db.Model):
    __tablename__ = 'assets'
    id = db.Column(db.Integer, primary_key=True)
    asset_number = db.Column(db.String(50))
    system_name = db.Column(db.String(100))
    status = db.Column(db.String(50))
    assigned_to = db.Column(db.String(100))
    asset_type = db.Column(db.String(50))
    location = db.Column(db.String(100))
    manufacturer = db.Column(db.String(100))
    model = db.Column(db.String(100))
    color = db.Column(db.String(50))
    serial_number = db.Column(db.String(100))
    mac = db.Column(db.String(100))
    purchase_date = db.Column(db.Date)
    issue_date = db.Column(db.Date)
    return_date = db.Column(db.Date)
    warranty_expire_date = db.Column(db.Date)
    condition = db.Column(db.String(100))
    notes = db.Column(db.Text)
