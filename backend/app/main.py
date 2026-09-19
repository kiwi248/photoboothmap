from fastapi import FastAPI

app = FastAPI(title="PhotoboothMap API")


@app.get("/health")
def health():
    return {"status": "ok"}
