from fastapi import FastAPI
import random

app = FastAPI()


#  http://127.0.0.1:8000
@app.get("/")
async def root():
    return {"message": "Hello World"}



@app.get("/teste2")
async def funcaoteste():
    return {"teste": True, "Aleatorio": random.randint(0, 1000)}