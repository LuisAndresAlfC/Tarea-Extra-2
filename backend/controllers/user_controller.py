from flask import Blueprint, request, jsonify
from services.user_service import UserService

user_blueprint = Blueprint('user', __name__)
user_service = UserService()

@user_blueprint.route('/submit', methods=['POST'])
def submit():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    mensaje1  = data.get('mensaje1')
    mensaje2  = data.get('mensaje2')
    mensaje3  = data.get('mensaje3')

    if not name or not email:
        return jsonify({'error': 'Missing required fields'}), 400

    user = user_service.create_user(name, email, mensaje1, mensaje2, mensaje3)
    return jsonify(user.serialize()), 201

@user_blueprint.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = user_service.get_user(user_id)
    if user:
        return jsonify(user.serialize())
    else:
        return jsonify({'error': 'User not found'}), 404

@user_blueprint.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    name = data.get('name')
    email = data.get('email')
    mensaje1  = data.get('mensaje1')
    mensaje2  = data.get('mensaje2')
    mensaje3  = data.get('mensaje3')

    if not name or not email:
        return jsonify({'error': 'Missing required fields'}), 400

    if user_service.update_user(user_id, name, email,mensaje1, mensaje2, mensaje3):
        user = user_service.get_user(user_id)
        return jsonify(user.serialize())
    else:
        return jsonify({'error': 'User not found'}), 404

@user_blueprint.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_service.delete_user(user_id):
        return '', 204
    else:
        return jsonify({'error': 'User not found'}), 404
