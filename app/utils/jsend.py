from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Any

def jsend_success(data: Any = None):
    if isinstance(data, BaseModel):
        data = data.dict()
    elif isinstance(data, list) and all(isinstance(item, BaseModel) for item in data):
        data = [item.dict() for item in data]
    elif isinstance(data, list) and all(hasattr(item, '__dict__') for item in data):
        data = [item.__dict__ for item in data]
    elif hasattr(data, '__dict__'):
        data = data.__dict__
    return JSONResponse(content={"status": "success", "data": data})

def jsend_fail(data: Any = None):
    if isinstance(data, BaseModel):
        data = data.dict()
    elif isinstance(data, list) and all(isinstance(item, BaseModel) for item in data):
        data = [item.dict() for item in data]
    elif isinstance(data, list) and all(hasattr(item, '__dict__') for item in data):
        data = [item.__dict__ for item in data]
    elif hasattr(data, '__dict__'):
        data = data.__dict__
    return JSONResponse(content={"status": "fail", "data": data})

def jsend_error(message: str, code: int = None, data: Any = None):
    response = {"status": "error", "message": message}
    if code:
        response["code"] = code
    if data:
        if isinstance(data, BaseModel):
            data = data.dict()
        elif isinstance(data, list) and all(isinstance(item, BaseModel) for item in data):
            data = [item.dict() for item in data]
        elif isinstance(data, list) and all(hasattr(item, '__dict__') for item in data):
            data = [item.__dict__ for item in data]
        elif hasattr(data, '__dict__'):
            data = data.__dict__
        response["data"] = data
    return JSONResponse(content=response)