from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import InkItUp

# Initialize the app
app = FastAPI()

app.include_router(InkItUp.router)

# GET operation at route '/'
@app.get('/')
def root_api():
    return {"message": "Welcome to Balasundar's Technical Blog"}