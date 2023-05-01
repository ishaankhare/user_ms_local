from datetime import date
from pydantic import BaseModel


class usersFriends(BaseModel):
    root_user: str
    friends: [str]

    class Config:
        orm_mode = True