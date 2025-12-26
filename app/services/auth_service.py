from app.repositories.user_repo import UserRepository
from app.utils.password import hash_password, verify_password
from app.utils.jwt import create_access_token

class AuthService:
    def __init__(self):
        self.user_repo = UserRepository()

    def register_user(self, email: str, password: str):
        hashed_password = hash_password(password)
        user = self.user_repo.create_user(email, hashed_password)
        return user

    def authenticate_user(self, email: str, password: str):
        user = self.user_repo.get_user_by_email(email)
        if not user:
            return None
        if not verify_password(password, user["password"]):
            return None
        return user
    
    def login_user(self, email: str, password: str):
        user = self.authenticate_user(email, password)
        
        if not user:
            return None
        
        token = create_access_token({
            "sub": str(user["id"]),
            "email": user["email"]
        })

        return token