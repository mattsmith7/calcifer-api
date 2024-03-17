from fastapi import FastAPI

# create FastAPI instance
calcifer_api = FastAPI()

# use command "uvicorn main:calcifer_api --reload" to launch uvicorn local server

# default route path
@calcifer_api.get("/")
async def root():
    return {"message": "Hello World"}