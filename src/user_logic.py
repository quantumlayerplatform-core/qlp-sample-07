class UserLogic:
    def __init__(self):
        self.users = {}

    def process_user_data(self, user_data):
        user_id = len(self.users) + 1
        self.users[user_id] = user_data
        return self.users[user_id]

    def retrieve_user(self, user_id):
        return self.users.get(user_id)

    def update_user(self, user_id, user_data):
        if user_id in self.users:
            self.users[user_id].update(user_data)
            return self.users[user_id]
        else:
            return None

    def delete_user(self, user_id):
        if user_id in self.users:
            del self.users[user_id]
            return True
        else:
            return False