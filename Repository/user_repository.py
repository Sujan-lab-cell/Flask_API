from models.user_models import User


class UserRepository:
    def __init__(self):
        self.users = []

    def add_user(self, user: User):
        self.users.append(user)

    def get_user(self, user_id: int) -> User:
        for user in self.users:
            if user.id == user_id:
                return user
        return None

    def update_user(self, user_id: int, name: str, email: str) -> bool:
        for user in self.users:
            if user.id == user_id:
                user.name = name
                user.email = email
                return True
        return False

    def delete_user(self, user_id: int) -> bool:
        for i, user in enumerate(self.users):
            if user.id == user_id:
                del self.users[i]
                return True
        return False