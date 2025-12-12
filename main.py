# main.py

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn # <-- Added uvicorn import

# --- 1. Initialize FastAPI App ---
app = FastAPI(
    title="Health Web App Backend",
    description="FastAPI server to host the backend logic and serve the frontend templates."
)

# --- 2. Configure Template Directory ---
templates = Jinja2Templates(directory="templates")

# --- 3. Root Endpoint (Existing) ---
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """
    Serves the main index.html file.
    """
    return templates.TemplateResponse(
        request=request, 
        name="index.html", 
        context={}
    )

# --- 4. Dashboard Endpoint (Existing) ---
@app.get("/dashboard", response_class=HTMLResponse)
async def read_dashboard(request: Request):
    """
    Serves the macOS-themed dashboard.html file.
    """
    # Example context data, you can pass real data here later
    context = {
        "user_name": "Dr. Alex",
        "health_score": 88,
        "heart_rate": 72,
        "sleep_hours": 7.5,
        "steps_today": 9341
    }
    return templates.TemplateResponse(
        request=request, 
        name="dashboard.html", 
        context=context
    )

# --- 5. Example API Endpoint (Existing) ---
@app.get("/api/health")
async def get_health_status():
    """
    A simple API endpoint to confirm the backend is running.
    """
    return {"status": "ok", "service": "Health App Backend", "version": "1.0"}


# --- 6. Run the Server Block (NEW/UPDATED) ---
if __name__ == "__main__":
    # This block allows you to run the server using 'python main.py'
    # The 'reload=True' flag enables automatic restart on code changes during development
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
