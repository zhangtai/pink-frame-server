from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .routers import weather

app = FastAPI()


app.include_router(weather.router)
app.mount("/images", StaticFiles(directory="output"), name="images")


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
