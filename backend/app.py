from fastapi import FastAPI
from fastapi.middleware.gzip import GZipMiddleware

from routers import api

app = FastAPI()
app.add_middleware(GZipMiddleware, minimum_size=1000)
app.include_router(api.router)
