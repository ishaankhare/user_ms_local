from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, ARRAY
from sqlalchemy.orm import relationship

from .database import Base


class users_friends(Base):
    __tablename__ = "user_friends"

    root_user = Column(String, ForeignKey("users_auth.username"), primary_key=True)
    friends = Column(ARRAY(String))



