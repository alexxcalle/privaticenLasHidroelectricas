from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.user import UserCreate, User
from app.services.user import UserService
from app.utils.jsend import jsend_success, jsend_fail, jsend_error

router = APIRouter()

@router.post("/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        created_user = UserService.create_user(db=db, user=user)
        return jsend_success(data=created_user)
    except Exception as e:
        return jsend_error(message=str(e))

@router.get("/", response_model=List[User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    try:
        users = UserService.get_users(db, skip=skip, limit=limit)
        return jsend_success(data=users)
    except Exception as e:
        return jsend_error(message=str(e))

@router.get("/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    try:
        user = UserService.get_user(db, user_id=user_id)
        if user is None:
            return jsend_fail(data={"user_id": "Usuario no encontrado"})
        return jsend_success(data=user)
    except Exception as e:
        return jsend_error(message=str(e))

@router.patch("/{user_id}", response_model=User)
def patch_user(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    try:
        db_user = UserService.get_user(db, user_id=user_id)
        if db_user is None:
            return jsend_fail(data={"user_id": "Usuario no encontrado"})
        updated_user = UserService.patch_user(db=db, user_id=user_id, user=user)
        return jsend_success(data=updated_user)
    except Exception as e:
        return jsend_error(message=str(e))

@router.delete("/{user_id}", response_model=User)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    try:
        db_user = UserService.get_user(db, user_id=user_id)
        if db_user is None:
            return jsend_fail(data={"user_id": "Usuario no encontrado"})
        deleted_user = UserService.delete_user(db=db, user_id=user_id)
        return jsend_success(data=deleted_user)
    except Exception as e:
        return jsend_error(message=str(e))