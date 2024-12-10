from flask import Blueprint, jsonify

bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    return jsonify({"message": "Hello, Flask running on Codespaces!"})
