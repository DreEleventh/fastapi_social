from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .import models
from .databaseConn import engine
from .routers import post, users, auth, votes

# This command tells sqlalchemy to run the creation statement and build all tables
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(votes.router)


@app.get("/")
async def root():
    return {"message": "This is my first FastAPI app!!"}


