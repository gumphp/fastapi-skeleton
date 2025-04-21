from typing import Any, Generic, Optional, TypeVar
from pydantic import BaseModel

T = TypeVar('T')


class ApiResponse(BaseModel, Generic[T]):
    """统一的API响应格式"""
    code: int = 200
    message: str = "success"
    data: Any = None


def success(data: Any = None, message: str = "success", code: int = 200) -> ApiResponse:
    """
    创建成功响应
    """
    return ApiResponse(code=code, message=message, data=data)


def error(message: str = "error", code: int = 400, data: Any = None) -> ApiResponse:
    """
    创建错误响应
    """
    return ApiResponse(code=code, message=message, data=data) 