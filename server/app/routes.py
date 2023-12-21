from app import app


@app.get("/", tags=["Root"])
async def read_root():
    users = []
    
    return {"message": users}