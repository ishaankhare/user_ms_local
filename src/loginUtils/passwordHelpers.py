from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def check_creds(input_creds, fake_users_db):
    if input_creds.username in fake_users_db.keys():
        if verify_password(input_creds.password, fake_users_db[input_creds.username]['password']):
            return 'Logged in'
        else:
            return 'Incorrect Password'
    else:
        return 'User not registered'

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def encrypt_password(password):
    return pwd_context.hash(password)