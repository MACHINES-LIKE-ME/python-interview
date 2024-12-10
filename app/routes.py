import requests
from collections import Counter

from flask import Blueprint, jsonify
from pydantic import ValidationError

from app.logic.response_processing import process_random_user_response
from app.models.names_occurrences import NamesOccurrencesResponse
from app.models.random_users import RandomUserResponse


bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    return jsonify({"message": "Hello, Flask running on Codespaces!"})


@bp.route('/random-user', methods=['GET'])
def get_random_user():
    api_url = "https://randomuser.me/api/?results=100"
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        data = response.json()
    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Failed to fetch data from Random User API", "details": str(e)}), 500

    try:
        validated_data = RandomUserResponse(**data)
    except ValidationError as e:
        return jsonify({"error": "Invalid API response", "details": e.errors()}), 400

    serializable_data = validated_data.model_dump(mode="json")

    return jsonify(serializable_data)

@bp.route('/random-user/names', methods=['GET'])
def get_names_occurrences():
    api_url = "https://randomuser.me/api/?results=100"
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Failed to fetch data from Random User API", "details": str(e)}), 500

    try:
        response_model = process_random_user_response(data)
    except ValueError as e:
        return jsonify(e.args[0]), 400

    return jsonify(response_model.model_dump(mode="json"))