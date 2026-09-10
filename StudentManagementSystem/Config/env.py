# StudentManagementSystem/Config/env.py
import os
from dotenv import load_dotenv

# load_dotenv()

class Settings:
    PROJECT_NAME: str = "Production CRUD API"
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL", 
        "postgresql://postgres:postgres@localhost:5432/postgres"
    )

settings = Settings()