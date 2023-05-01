from fastapi import FastAPI, Request, APIRouter, Depends, HTTPException, Response
from fastapi.responses import RedirectResponse
import starlette.status as status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from src.models.UserModels import *
from src.loginUtils.passwordHelpers import *
from jose import JWTError, jwt
from datetime import datetime, timedelta
from src.loginUtils.tokenHelpers import *


def get_token(request: Request, response: Response):
    token = request.cookies['signInToken']
    token_answer = request.path_params['user']

    if validate_token(token, token_answer) == 'okay':
        response.headers['currentUser'] = token_answer
        return token_answer
    else:
        raise HTTPException(status_code=403, detail="Item not found")


def passCurrentUser(request: Request, response: Response):
    token = request.cookies['signInToken']
    response.headers['currentUser'] = decode_token(token)['sub']
    return
