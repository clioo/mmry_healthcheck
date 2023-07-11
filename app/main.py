from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
import dotenv


dotenv.load_dotenv(dotenv.find_dotenv())


origins = [
    "*",
]
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/healthcheck")
def read_item():
    
    return Response(status_code=200)
