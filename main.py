from fastapi import FastAPI
from StudentManagementSystem.Route.UserRoute import userRouter
import uvicorn

def start_application():
    import StudentManagementSystem.Config.database as database
    from sqlalchemy import text
    
    # Drop tables with CASCADE to handle foreign key dependencies (for development)
    # with database.engine.connect() as conn:
    #     conn.execute(text("DROP TABLE IF EXISTS branches CASCADE"))
    #     conn.execute(text("DROP TABLE IF EXISTS churches CASCADE"))
    #     conn.execute(text("DROP TABLE IF EXISTS approvals CASCADE"))
    #     conn.execute(text("DROP TABLE IF EXISTS activity_logs CASCADE"))
    #     conn.execute(text("DROP TABLE IF EXISTS notifications CASCADE"))
    #     conn.execute(text("DROP TABLE IF EXISTS users CASCADE"))
    #     conn.commit()
    
    # Create all tables with correct schema
    database.Base.metadata.create_all(bind=database.engine)

    app = FastAPI(title="Production OOP CRUD Service", version="1.0.0")
    app.include_router(userRouter)
    return app

app = start_application()

@app.get("/health", tags=["Health Check"])
def health_check():
    return {"status": "healthy"}

def main():
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)