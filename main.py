# main.py

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn 

# --- 1. Initialize FastAPI App ---
app = FastAPI(
    title="Health Web App Backend",
    description="FastAPI server to host the backend logic and serve the frontend templates."
)

# --- 2. Configure Template Directory ---
# This points to the 'templates' folder where dashboard.html and medication.html reside.
templates = Jinja2Templates(directory="templates")

# --- 3. Root Endpoint ---
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """
    Serves the main index.html file (Initial page).
    """
    return templates.TemplateResponse(
        request=request, 
        name="index.html", 
        context={}
    )

# --- 4. Dashboard Endpoint ---
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

# --- 5. Medication Endpoint ---
@app.get("/medication", response_class=HTMLResponse)
async def read_medication(request: Request):
    """
    Serves the Medication Tracker page (medication.html).
    """
    context = {"user_name": "Dr. Alex"}
    return templates.TemplateResponse(
        request=request, 
        name="medication.html", 
        context=context
    )

# --- 6. Chat Endpoint (NEW) ---
@app.get("/chat", response_class=HTMLResponse)
async def read_chat(request: Request):
    """
    Serves the Chat page (chat.html).
    """
    context = {"user_name": "Dr. Alex"}
    return templates.TemplateResponse(
        request=request, 
        name="chat.html", 
        context=context
    )


# --- 7. Example API Endpoint (Health Check) ---
@app.get("/api/health")
async def get_health_status():
    """
    A simple API endpoint to confirm the backend is running.
    """
    return {"status": "ok", "service": "Health App Backend", "version": "1.0"}


# --- 8. Run the Server Block ---
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
