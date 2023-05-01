from src.sql import models


def fetch_friends(user, db):
    records = db.query(models.users_friends).filter(models.users_friends.root_user == user).first()
    return records
