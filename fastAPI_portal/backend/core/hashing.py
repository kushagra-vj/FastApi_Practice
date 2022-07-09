import hashlib
from hmac import compare_digest


class Hasher():
    
    @staticmethod
    def verify_password(plain_passowrd, hashed_password):
        return hashlib.sha256(plain_passowrd.encode()).hexdigest() == hashed_password

    
    @staticmethod
    def get_password_hashed(password):
        encoded = password.encode()
        return hashlib.sha256(encoded).hexdigest()