from flask import Blueprint, jsonify, request
from .db import get_db_connection

bp = Blueprint('routes', __name__)

@bp.route('/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users;")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(users)

@bp.route('/users', methods=['POST'])
def add_user():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s) RETURNING id;", (data['name'], data['age']))
    user_id = cursor.fetchone()[0]
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"id": user_id, "message": "User added successfully!"}), 201
