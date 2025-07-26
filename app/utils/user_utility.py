class UserUtility:
    def validate_user_data(self, user_data):
        required_fields = ['name', 'email']
        return all(field in user_data for field in required_fields)