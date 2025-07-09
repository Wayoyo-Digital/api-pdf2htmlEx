from core import bootstrap
from fastapi import FastAPI

app = FastAPI()

bootstrap.run(app)
