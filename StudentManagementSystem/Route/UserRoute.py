from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from StudentManagementSystem.Config.database import get_db
from StudentManagementSystem.Schema.User import (
    UserCreate,
    UserDeleteResponse,
    UserListResponse,
    UserResponse,
)
from StudentManagementSystem.Controller.UserController import UserController

userRouter = APIRouter(prefix="/users", tags=["Users"])

@userRouter.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return UserController.create_user(db=db, user_in=user)

@userRouter.get("/", response_model=UserListResponse)
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return {
        "message": "Users retrieved successfully",
        "users": UserController.get_users(db=db, skip=skip, limit=limit),
    }

@userRouter.get("/{user_id}", response_model=UserResponse)
def read_user(user_id: UUID, db: Session = Depends(get_db)):
    db_user = UserController.get_user(db=db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User retrieved successfully", "user": db_user}

@userRouter.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: UUID, user: UserCreate, db: Session = Depends(get_db)):
    db_user = UserController.update_user(db=db, user_id=user_id, user_in=user)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User updated successfully", "user": db_user}

@userRouter.delete("/{user_id}", response_model=UserDeleteResponse)
def delete_user(user_id: UUID, db: Session = Depends(get_db)):
    success = UserController.delete_user(db=db, user_id=user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}