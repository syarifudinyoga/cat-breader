from fastapi import FastAPI
from app.config.database import Database
from app.db.migrate import Migrator

app = FastAPI(title="API Breader", version="1.0.0")

@app.get("/")
async def read_root():
    return {"message": "Hello World"}

@app.get("/db")
async def db_test():
    db = Database()
    query = "SELECT NOW() AS current_time;"
    result = db.execute(query, fetchOne=True)
    return {"current_time": result[0]}

@app.post("/migrate")
async def run_migrations():
    migrator = Migrator()
    migrator.run()
    return {"message": "Migrations executed successfully"}