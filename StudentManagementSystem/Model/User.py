from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from StudentManagementSystem.Config.database import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid

class UserModel(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        index=True,
        default=uuid.uuid4,
    )
    name: Mapped[str] = mapped_column(
        String(100), 
        nullable=False)
    email: Mapped[str] = mapped_column(
        String(100), 
        unique=True, 
        index=True, 
        nullable=False)
    hashed_password: Mapped[str] = mapped_column(
        String(255),
        nullable=False)