import uvicorn
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from routes.routes import routes

app = FastAPI()

# Mount the static directory. Make sure you have a 'static' folder
# containing a 'css' subfolder with 'style.css' inside it.
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configure Jinja2 templates. Make sure you have a 'templates' folder
# containing your 'template.html' file.
# Changed directory name to "templates" (plural) as is common practice.
templates = Jinja2Templates(directory="templates")

# CORS Middleware - Keep if needed, but if serving frontend and backend
# from the same FastAPI app, it might not be strictly necessary.
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the router from routes.py
# This connects the /query_response and /session_history endpoints
app.include_router(routes)


# Endpoint to render the main HTML template
# This handles the initial GET request to load the page
@app.get("/", tags=["UI"])  # Added a tag for organization
async def index(request: Request):
    """
    Endpoint to render the main HTML template.
    """
    return templates.TemplateResponse("template.html", {"request": request})


# Removed the problematic @app.post("/") route.
# The query submission is handled by the /query_response endpoint in routes.py.

if __name__ == "__main__":

    uvicorn.run(
        app, host="0.0.0.0", port=8000, reload=True
    )  # Added reload=True for development
