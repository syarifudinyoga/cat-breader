from app.config.database import Database

class UserRepository:
    def __init__(self):
        self.db = Database()

    def create_user(self, email: str, hashed_password: str):
        query = """
        INSERT INTO users (email, password) 
        VALUES (%s, %s)
        RETURNING id, email;
        """
        try:
            return self.db.execute(query, (email, hashed_password), fetchOne=True)
        except Exception as e:
            print("DB ERROR:", e)
            raise


    def get_user_by_email(self, email: str):
        query = "SELECT id, email, password FROM users WHERE email = %s;"
        result = self.db.execute(query, (email,), fetchOne=True)
        return result