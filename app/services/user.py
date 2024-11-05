from sqlalchemy.orm import Session
from app.models.user import User as UserModel
from app.schemas.user import UserCreate

class UserService:
    @staticmethod
    def create_user(db: Session, user: UserCreate):
        db_user = UserModel(
            email=user.email,
            username=user.username,
            hashed_password=user.hashed_password
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    @staticmethod
    def get_users(db: Session, skip: int = 0, limit: int = 100):
        try:
            users = db.query(UserModel).offset(skip).limit(limit).all()
            return users
        except Exception as e:
            print(f"Error: {e}")
            raise e
    
    def get_user(db: Session, user_id: int):
        return db.query(UserModel).filter(UserModel.id == user_id).first()
    
    def get_user_by_email(db: Session, email: str):
        return db.query(UserModel).filter(UserModel.email == email).first()
    
    def patch_user(db: Session, user_id: int, user: UserCreate):
        db_user = db.query(UserModel).filter(UserModel.id == user_id).first()
        db_user.email = user.email
        db_user.hashed_password = user.hashed_password
        db.commit()
        db.refresh(db_user)
        return db_user
    
    def delete_user(db: Session, user_id: int):
        db_user = db.query(UserModel).filter(UserModel.id == user_id).first()
        db.delete(db_user)
        db.commit()
        return db_user