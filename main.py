# main.py

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# --- 1. Initialize FastAPI App ---
app = FastAPI(
    title="Health Web App Backend",
    description="FastAPI server to host the backend logic and serve the frontend templates."
)

# --- 2. Configure Template Directory ---
# This tells FastAPI where to look for HTML files (in the 'templates' folder)
templates = Jinja2Templates(directory="templates")

# Note: If you add static files like compiled Tailwind CSS (e.g., /static/css/styles.css),
# you would uncomment and configure the StaticFiles mount here:
# app.mount("/static", StaticFiles(directory="static"), name="static")


# --- 3. Root Endpoint to Serve the HTML Page ---
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """
    Serves the main HTML file from the templates directory.
    The `request` object is required by Jinja2 to render the template context.
    """
    # You can pass context variables here (e.g., {'app_name': 'My Health Tracker'})
    # The 'request': request part is mandatory for Jinja2Templates
    return templates.TemplateResponse(
        request=request, 
        name="index.html", 
        context={}
    )


# --- 4. Example API Endpoint (Health Check) ---
@app.get("/api/health")
async def get_health_status():
    """
    A simple API endpoint to confirm the backend is running.
    """
    return {"status": "ok", "service": "Health App Backend", "version": "1.0"}


# --- 5. Run the Server (Optional, Uvicorn is usually run via the command line) ---
# This block is primarily for quick testing or specialized deployment scenarios.
# The standard way to run the app is shown below.
if __name__ == "__main__":
    import uvicorn
    # The command to run this directly: python main.py
    # This runs the app on http://127.0.0.1:8000
    uvicorn.run(app, host="0.0.0.0", port=8000)
