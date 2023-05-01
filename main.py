from src.dependencies.tokenValidation import *
from fastapi import Depends, FastAPI
from fastapi import Response

from src.dependencies.tokenValidation import *
from src.sql import models
from src.sql.database import SessionLocal, engine
from src.friendsUtils.friends import *
from sqlalchemy.orm import Session


models.Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


app = FastAPI(dependencies=[Depends(passCurrentUser)])

fake_users_db = {
    "ishaan": {"vihaan", "jojo"},
    "vihaan": {"ishaan", "jojo"},
}


@app.get("/user/")
async def home(request: Request, response: Response):
    current_user = response.headers['currentUser']
    return f"Hello World to User app: {current_user}"

@app.get("/user/friends-db/")
async def home(request: Request, response: Response, db: Session = Depends(get_db)):
    current_user = response.headers['currentUser']
    friends_list = fetch_friends(current_user, db).friends
    return f"Hello {current_user}, you friends are: {friends_list}"



@app.get("/user/friends/")
async def home(request: Request, response: Response):
    current_user = response.headers['currentUser']
    friends_list = fake_users_db[current_user]
    return f"Hello {current_user}, you friends are: {friends_list}"





