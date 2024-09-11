from fastapi import APIRouter, Request, HTTPException
from app.core.chat import generate_response
from app.core.actions import execute_action

router = APIRouter()

@router.post("/chat")
async def chat(request: Request):
    data = await request.json()
    query = data.get("query")
    if not query:
        raise HTTPException(status_code=400, detail="Query is required")
    
    # Generate a response from the chatbot
    bot_message = generate_response(query)
    return {"bot_message": bot_message}

@router.post("/action")
async def action(request: Request):
    data = await request.json()
    action_type = data.get("action_type")
    parameters = data.get("parameters", {})
    
    if not action_type:
        raise HTTPException(status_code=400, detail="Action type is required")
    
    # Execute the specified action
    result_message = execute_action(action_type, parameters)
    return {"bot_message": result_message}