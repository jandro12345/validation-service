import logging
import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from middleware import LogMiddleware
from routes.payment import payment_route


load_dotenv()
app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"])
app.add_middleware(LogMiddleware)


app.include_router(payment_route, prefix="/api/v1.0")

