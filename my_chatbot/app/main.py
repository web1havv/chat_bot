from fastapi import FastAPI
from app.api import endpoints

# Initialize the FastAPI app
app = FastAPI()

# Include the API endpoints from the endpoints module
app.include_router(endpoints.router)

# Define a root endpoint for basic testing
@app.get("/")
async def root():
    return {"message": "Welcome to the Chatbot API"}