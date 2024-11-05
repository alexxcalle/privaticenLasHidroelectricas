from sqlalchemy.orm import Session
from app.models.user import User as UserModel
from app.schemas.user import UserCreate, User
from typing import List

class UserService:
    @staticmethod
    def create_user(db: Session, user: UserCreate) -> User:
        db_user = UserModel(
            email=user.email,
            username=user.username,
            hashed_password=user.hashed_password
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return User.from_orm(db_user)

    @staticmethod
    def get_users(db: Session, skip: int = 0, limit: int = 100) -> List[User]:
        users = db.query(UserModel).offset(skip).limit(limit).all()
        return [User.from_orm(user) for user in users]

    @staticmethod
    def get_user(db: Session, user_id: int) -> User:
        user = db.query(UserModel).filter(UserModel.id == user_id).first()
        if user:
            return User.from_orm(user)
        return None

    @staticmethod
    def get_user_by_email(db: Session, email: str) -> User:
        user = db.query(UserModel).filter(UserModel.email == email).first()
        if user:
            return User.from_orm(user)
        return None

    @staticmethod
    def patch_user(db: Session, user_id: int, user: UserCreate) -> User:
        db_user = db.query(UserModel).filter(UserModel.id == user_id).first()
        if db_user:
            db_user.email = user.email
            db_user.username = user.username
            db_user.hashed_password = user.hashed_password
            db.commit()
            db.refresh(db_user)
            return User.from_orm(db_user)
        return None

    @staticmethod
    def delete_user(db: Session, user_id: int) -> User:
        db_user = db.query(UserModel).filter(UserModel.id == user_id).first()
        if db_user:
            db.delete(db_user)
            db.commit()
            return User.from_orm(db_user)
        return None