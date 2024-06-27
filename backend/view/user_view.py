from flask import jsonify

def user_response(user):
    response = {
        'status': 'success',
        'user': {
            'name': user.name,
            'email': user.email,
            'mensaje1' : user.mensaje1,
            'mensaje2' : user.mensaje2,
            'mensaje3' : user.mensaje3
        }
    }
    return jsonify(response)
