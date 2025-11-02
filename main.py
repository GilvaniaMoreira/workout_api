from fastapi import FastAPI

app = FastAPI(title="Workout API", description="A simple workout API")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run('main:app', host="0.0.0.0", port=8045, log_level="info", reload=True)
