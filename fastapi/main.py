from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello from FastAPI on EKS via ArgoCD!"}

@app.get("/health")
async def health_check():
    return {"status": "ok"}
# CI Trigger
