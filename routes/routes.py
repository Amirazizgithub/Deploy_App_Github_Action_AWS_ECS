from fastapi import APIRouter, Request, HTTPException
from model.model import Generative_AI_Model
import warnings

warnings.filterwarnings("ignore")

## Global Route
routes = APIRouter()

## Routes for Generative AI Model APIs


# Endpoint to response of the user query
# This endpoint is intended to be called via AJAX/Fetch
@routes.post("/query_response")
async def response_of_user_query(request: Request):
    try:
        data = await request.json()
        # Expecting keys 'user_query' and 'model_type' from the frontend
        if "user_query" not in data or "model_type" not in data:
            raise HTTPException(
                status_code=400, detail="user_query and model_type are required"
            )

        user_query = data["user_query"]
        model_type = data["model_type"]

        generative_ai_model = Generative_AI_Model()
        return generative_ai_model.generate_response_according_selected_model_type(
            model_type=model_type, user_query=user_query
        )

    except HTTPException as e:
        # Re-raise HTTP exceptions to ensure proper status codes
        raise e

    except Exception as e:
        # Return an error response as JSON
        raise HTTPException(status_code=500, detail=str(e))


# Endpoint to fetch last 10 session history
@routes.get("/session_history")
async def get_session_history():
    try:
        generative_ai_model = Generative_AI_Model()
        return generative_ai_model.get_session_history_from_MongoDB()
    except Exception as e:
        print(f"Error in /session_history: {e}")
        raise HTTPException(status_code=500, detail=str(e))
