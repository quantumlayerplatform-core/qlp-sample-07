from sqlalchemy.orm import Session
from models.user import User

class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def add_user(self, username: str, email: str):
        new_user = User(username=username, email=email)
        self.session.add(new_user)
        self.session.commit()
        return new_user

    def get_user_by_username(self, username: str):
        return self.session.query(User).filter(User.username == username).first()

    def get_user_by_id(self, user_id: int):
        return self.session.query(User).filter(User.id == user_id).first()

    def delete_user(self, user_id: int):
        user_to_delete = self.get_user_by_id(user_id)
        if user_to_delete:
            self.session.delete(user_to_delete)
            self.session.commit()
            return True
        return False