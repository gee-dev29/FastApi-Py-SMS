import base64, hashlib, hmac, os
from uuid import UUID

from sqlalchemy.orm import Session
from StudentManagementSystem.Model.User import UserModel
from StudentManagementSystem.Schema.User import UserCreate


def hash_password(password: str) -> str:
    salt = os.urandom(16)
    hashed = hashlib.scrypt(
        password.encode("utf-8"),
        salt=salt,
        n=2**14,
        r=8,
        p=1,
        dklen=32,
    )
    return f"scrypt${base64.b64encode(salt).decode()}${base64.b64encode(hashed).decode()}"


def verify_password(password: str, stored_hash: str) -> bool:
    try:
        algorithm, encoded_salt, encoded_hash = stored_hash.split("$", 2)
        if algorithm != "scrypt":
            return False
        salt = base64.b64decode(encoded_salt, validate=True)
        expected_hash = base64.b64decode(encoded_hash, validate=True)
        actual_hash = hashlib.scrypt(
            password.encode("utf-8"),
            salt=salt,
            n=2**14,
            r=8,
            p=1,
            dklen=len(expected_hash),
        )
    except (ValueError, TypeError):
        return False
    return hmac.compare_digest(actual_hash, expected_hash)


class UserController:

    @staticmethod
    def create_user(db: Session, user_in: UserCreate) -> UserModel:
        user = UserModel(
            name=user_in.name,
            email=user_in.email,
            hashed_password=hash_password(user_in.password)
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    @staticmethod
    def get_user(db: Session, user_id: UUID) -> UserModel | None:
        return db.query(UserModel).filter(UserModel.id == user_id).first()

    @staticmethod
    def get_users(db: Session, skip: int = 0, limit: int = 100) -> list[UserModel]:
        return db.query(UserModel).offset(skip).limit(limit).all()

    @staticmethod
    def update_user(db: Session, user_id: UUID, user_in: UserCreate) -> UserModel | None:
        user = UserController.get_user(db, user_id)
        if not user:
            return None
        
        user.name = user_in.name
        user.email = user_in.email
        user.hashed_password = hash_password(user_in.password)
        
        db.commit()
        db.refresh(user)
        return user

    @staticmethod
    def delete_user(db: Session, user_id: UUID) -> bool:
        user = UserController.get_user(db, user_id)
        if not user:
            return False
        
        db.delete(user)
        db.commit()
        return True