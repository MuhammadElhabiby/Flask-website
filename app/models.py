from . import db
from datetime import datetime

class UserPrompt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    prompt = db.Column(db.String(255), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"UserPrompt('{self.prompt}')"

class TextEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"TextEntry('{self.content}')"
