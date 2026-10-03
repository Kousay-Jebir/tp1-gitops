import os
import socket

from flask import Flask

app = Flask(__name__)
VERSION = os.getenv("APP_VERSION", "dev")


@app.get("/")
def index():
    return {"version": VERSION, "pod": socket.gethostname()}


@app.get("/healthz")
def healthz():
    return "ok"