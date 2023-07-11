from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from os import environ


origins = [
    "*",
]
app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


@app.get("/healthcheck")
def read_item():
    is_healthy = environ.get("IS_HEALTHY", "YES") == "YES"
    status_code = 200 if is_healthy else 201
    return Response(status_code=status_code)
