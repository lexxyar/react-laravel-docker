from fastapi import FastAPI
import uvicorn

app = FastAPI()
port = 7000


@app.get("/")
def healthcheck():
    return 'OK'


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=port)
