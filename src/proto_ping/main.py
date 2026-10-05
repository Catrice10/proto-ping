from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/hello")
def read_hello():
    return {"Hello": "World"}

def main():
    uvicorn.run(app, host="0.0.0.0", port=8080)