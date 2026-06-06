from fastapi import FastAPI

app=FastAPI()
@app.get('/')
async def rppt():
    return {"Message ":"Hello World"}
