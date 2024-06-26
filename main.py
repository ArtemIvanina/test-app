import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello from FastAPI"}

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=5000)
