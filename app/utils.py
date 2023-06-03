from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_passcode(password: str):
    # Hashes each password passed to it
    return pwd_context.hash(password)


def verify_passcode(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)