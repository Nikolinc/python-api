from flask import Blueprint, jsonify, request
from .db import get_db_connection
from .models import insert_data, fetch_data

bp = Blueprint('routes', __name__)

@bp.route('/users', methods=['GET'])
def get_users():
    try:
        conn = get_db_connection()
        users = fetch_data(conn)
        formatted_users = [{
            "id": user[0],
            "name": user[1],
            "gender": user[2],
            "person_id": user[3],
            "data_of_birth": user[4]
            } for user in users]
        return jsonify(formatted_users), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@bp.route('/users', methods=['POST'])
def add_user():
    try:
        data = request.json
        if not data or 'name' not in data or 'age' not in data:
            return jsonify({"error": "Invalid input, 'name' and 'age' are required"}), 400

        conn = get_db_connection()
        msg = insert_data(conn, data['name'], data['age'])
        conn.close()

        return jsonify({"message": msg}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
