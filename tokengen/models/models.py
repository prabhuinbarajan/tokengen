from datetime import datetime, timedelta

import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()


def future():
    return datetime.utcnow() + timedelta(days=14)

class tokens(db.Model):
    __tablename__ = 'tokens'
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(100))
    crypto_key = db.Column(db.String(100), unique=True)
    key_expiry=db.Column(db.DateTime, default=future)
    key_status=db.Column(db.String(100))
    created_date = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)