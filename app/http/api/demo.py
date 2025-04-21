from fastapi import APIRouter, Depends

from app.http.deps import get_db
from app.models.user import User
from app.providers.database import redis_client
from app.services.auth import hashing
from app.support.api_response import *

router = APIRouter(
    prefix="/demo"
)


@router.get("/index")
def index(id:int=0):
    return success({
        "uri": "/api/demo/index"
    })


@router.get("/db_test", dependencies=[Depends(get_db)])
def db_test():
    try:
        password = hashing.get_password_hash("123456")
        user = User.create(username='fake_user_by_db_test_1', password=password)
        return success(user)
    except Exception as e:
        return error(str(e))


@router.get("/redis_test")
def redis_test():
    redis_client.incr('fastapi:test')
    return success({'value': redis_client.get('fastapi:test')})


@router.get("/show")
def show(id: int):
    return success({"id": id})
