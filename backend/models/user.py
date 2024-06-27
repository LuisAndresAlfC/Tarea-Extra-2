

class User:
    def __init__(self, user_id, name, email,mensaje1, mensaje2 ,mensaje3):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.mensaje1 = mensaje1
        self.mensaje2 = mensaje2
        self.mensaje3 = mensaje3

    def serialize(self):
        return {
            'user_id': self.user_id,
            'name': self.name,
            'email': self.email,
            'mensaje1': self.mensaje1,
            'mensaje2': self.mensaje2,
            'mensaje3': self.mensaje3
        }
