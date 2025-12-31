#!/usr/bin/env python3
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token,
    jwt_required, get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# =====================================================
# Configuration
# =====================================================
app.config["JWT_SECRET_KEY"] = "super-secret-key"  # use strong key in real apps

auth = HTTPBasicAuth()
jwt = JWTManager(app)

# =====================================================
# In-memory users storage
# =====================================================
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

# =====================================================
# BASIC AUTHENTICATION
# =====================================================
@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if not user:
        return False
    if check_password_hash(user["password"], password):
        return username
    return False


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


# =====================================================
# JWT ERROR HANDLERS (ALL MUST RETURN 401)
# =====================================================
@jwt.unauthorized_loader
def handle_missing_token(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token(jwt_header, jwt_payload):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_fresh_token(err):
    return jsonify({"error": "Fresh token required"}), 401


# =====================================================
# JWT LOGIN
# =====================================================
@app.route("/login", methods=["POST"])
def login():
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Invalid credentials"}), 401

    user = users.get(username)
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    access_token = create_access_token(
        identity={
            "username": user["username"],
            "role": user["role"]
        }
    )

    return jsonify({"access_token": access_token})


# =====================================================
# JWT PROTECTED ROUTES
# =====================================================
@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    identity = get_jwt_identity()

    if identity.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


# =====================================================
# RUN SERVER
# =====================================================
if __name__ == "__main__":
    app.run()
