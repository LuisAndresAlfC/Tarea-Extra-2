from models.user import User  

class UserService:
    def __init__(self):
        self.users = {}
        self.next_user_id = 1

    def create_user(self, name, email, mensaje1, mensaje2, mensaje3):
        user_id = self.next_user_id
        self.next_user_id += 1
        user = User(user_id,name, email, mensaje1, mensaje2, mensaje3)
        self.users[user_id] = user
        return user

    def get_user(self, user_id):
        return self.users.get(user_id)

    def update_user(self, user_id, name, email, mensaje1, mensaje2, mensaje3):
        if user_id in self.users:
            user = self.users[user_id]
            user.name = name
            user.email = email
            user.mensaje1 = mensaje1
            user.mensaje2 = mensaje2
            user.mensaje3 = mensaje3
            return True
        return False

    def delete_user(self, user_id):
        if user_id in self.users:
            del self.users[user_id]
            return True
        return False


