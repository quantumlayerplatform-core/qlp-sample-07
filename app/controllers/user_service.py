import json
from logic.user_logic import UserLogic
from utility.user_utility import UserUtility

class UserService:
    def __init__(self):
        self.user_logic = UserLogic()
        self.user_utility = UserUtility()

    def create_user(self, user_data):
        if not self.user_utility.validate_user_data(user_data):
            raise ValueError("Invalid user data provided")
        user = self.user_logic.process_user_data(user_data)
        return json.dumps(user)

    def get_user(self, user_id):
        user = self.user_logic.retrieve_user(user_id)
        if user is None:
            raise ValueError("User not found")
        return json.dumps(user)

    def update_user(self, user_id, user_data):
        if not self.user_utility.validate_user_data(user_data):
            raise ValueError("Invalid user data provided")
        updated_user = self.user_logic.update_user(user_id, user_data)
        return json.dumps(updated_user)

    def delete_user(self, user_id):
        result = self.user_logic.delete_user(user_id)
        return json.dumps({"success": result})