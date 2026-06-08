from fastapi import FastAPI

app = FastAPI(title="EdTech Analytics API")

@app.get("/")
def home():
    return {"message": "API EdTech Analytics opérationnelle"}

@app.get("/health")
def health():
    return {"status": "ok"}