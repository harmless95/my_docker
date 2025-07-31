import uvicorn
from fastapi import FastAPI

app_main = FastAPI()

@app_main.get("/")
async def get_hello_world():
    # Hello world
    return {
        "message": "Hello world"
    }

if __name__ == "__main__":
    uvicorn.run("main:app_main", host="0.0.0.0", port=8080)
