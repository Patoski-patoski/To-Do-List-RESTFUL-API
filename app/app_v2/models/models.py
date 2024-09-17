#!/usr/bin/env python3
"""app/app_v2/models/models.py module"""

from app import db  # Import db from app.py
from utils.helpers import generate_hashed_password, verify_password


class User(db.Model):
    """User model"""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password_hash = db.Column(db.String(150), nullable=False)

    def __init__(self, email: str, password: str) -> None:
        self.email = email
        self.password_hash = generate_hashed_password(password)
    

    def verify_user(self, password):
        return verify_password(password)
