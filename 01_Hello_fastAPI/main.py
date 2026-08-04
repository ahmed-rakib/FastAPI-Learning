from fastapi import FastAPI


app = FastAPI()

@app.get("/")
async def home():
    return {"message": "Hello FastAPI"}


@app.get("/about")
async def about():
    return {"project":"This is fastAPI project"}