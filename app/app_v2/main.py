#!/usr/bin/env python3
"""main module"""

from flask import jsonify, request, abort
from app import app, db, User
from sqlalchemy.exc import IntegrityError


@app.route("/index/<string:user_name>")
def index(user_name):
    """test flask app"""
    return jsonify({f"Hello {user_name} ": "Welcome to the world"})


@app.route("/users/", methods=["POST"], strict_slashes=False)
def create_user():
    data = request.json

    if not data or not all(key in data for key in ("email",  "password")):
        abort(400, description="Error! Email and Password are required")

    user = User(email=data["email"], password=data["password"])
    try:
        db.session.add(user)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        abort(409, error="Error! User with this email already exists.")

    return jsonify({"messagge": "User created successfully", "email": user.email}), 201

@app.route("/users/", methods=['DELETE'], strict_slashes=False)
def delete_user():
    data = request.json
    
    if not data or not all(key in data for key in ("email", "password")):
        abort(400, description="Error! Email and Password are required")
    
    user = User.query.filter_by(email=data['email']).first()
    if not user:
        abort(404, description="Error! No User with this email.")
        
    try:
        db.session.delete(user)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        abort(409, error="Error! Could not delete this user")
    
    return jsonify({"message": "Deleted successfully"}), 200


if __name__ == "__main__":
    app.run(debug=True)
