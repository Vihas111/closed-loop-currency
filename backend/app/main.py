from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {
        "message": "Campus Currency Backend Running"
    }