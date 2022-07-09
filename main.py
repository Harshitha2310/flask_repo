from fastapi import FastAPI

app = FastAPI()


@app.get("/name/{username}")
async def read_name(username : str):
    return {username: username}
    
@app.get("/experience/{experienced_yrs}")
async def read_experience(experienced_yrs: int):
    return {experienced_yrs : experienced_yrs}

@app.post("/")
async def role():
    return "Associate consultant"




























