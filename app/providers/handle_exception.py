from fastapi.exception_handlers import request_validation_exception_handler, http_exception_handler
from fastapi.exceptions import RequestValidationError
from starlette.responses import JSONResponse

from app.exceptions.exception import AuthenticationError, AuthorizationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi import Request
from app.support.api_response import *


def register(app):

    @app.exception_handler(AuthenticationError)
    async def authentication_exception_handler(request: Request, e: AuthenticationError):
        """
        认证异常处理
        """
        return JSONResponse(status_code=401, content={"message": e.message})

    @app.exception_handler(AuthorizationError)
    async def authorization_exception_handler(request: Request, e: AuthorizationError):
        """
        权限异常处理
        """
        return JSONResponse(status_code=403, content={"message": e.message})

    @app.exception_handler(StarletteHTTPException)
    async def custom_http_exception_handler(request: Request, exc):
        return await http_exception_handler(request, exc)

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc):
        return await request_validation_exception_handler(request, exc)

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        """处理请求参数验证错误，返回自定义格式"""
        errors = []
        # for error in exc.errors():
        #     errors.append({
        #         "loc": ".".join(error["loc"]),
        #         "field": ".".join(str(loc) for loc in error["loc"][1:]) if len(error["loc"]) > 1 else error["loc"][0],
        #         "msg": error["msg"],
        #         "type": error["type"],
        #         "input": error["input"],
        #     })
        return JSONResponse(
            status_code=422,  # Unprocessable Entity
            content=ApiResponse(
                code=422,
                message="参数验证错误",
                data=exc.errors()
            ).model_dump()
        )