from datetime import datetime
from flask_login import UserMixin
from app import manager, db, app


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(32))
    email = db.Column(db.String(64), unique=True)
    is_confirm = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class EmailConfirm(db.Model):
    login = db.Column(db.String(20), primary_key=True)
    url = db.Column(db.String(32), unique=True)

@manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

with app.app_context():
    db.create_all()
