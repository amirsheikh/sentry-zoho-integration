from fastapi import FastAPI, Request, HTTPException
import httpx
import os

# Load the Zoho Cliq Webhook URL from environment variable
ZOHO_CLIQ_WEBHOOK_URL = os.getenv("ZOHO_CLIQ_WEBHOOK_URL")

if not ZOHO_CLIQ_WEBHOOK_URL:
    raise ValueError("ZOHO_CLIQ_WEBHOOK_URL environment variable is not set.")

app = FastAPI()

# Helper function to send notifications to Zoho Cliq
async def send_cliq_notification(message: str):
    payload = {
        "text": message
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.post(ZOHO_CLIQ_WEBHOOK_URL, json=payload)
        response.raise_for_status()

# Endpoint to receive Sentry webhooks
@app.post("/sentry-webhook")
async def sentry_webhook(request: Request):
    # Get JSON payload from Sentry
    try:
        payload = await request.json()
    except Exception as e:
        raise HTTPException(status_code=400, detail="Invalid JSON payload") from e

    # Extract relevant information from Sentry event
    logger = payload.get("logger", "No Logger")
    environment = payload.get("environment", "No environment")
    triggering_rules = payload.get("triggering_rules", list())
    event_title = triggering_rules[0] if triggering_rules else ""
    event_message = payload.get("message", "No Message")
    event_url = payload.get("url", "No URL Provided")
    project_name = payload.get("project_name", "No Project Name")
    # Format message for Zoho Cliq
    cliq_message = f"Project Name: {project_name}\nEnvironment: {environment}\nLogger: {logger}\nSentry Alert: {event_title}\nMessage: {event_message}\n[View in Sentry]({event_url})"

    # Send message to Zoho Cliq
    await send_cliq_notification(cliq_message)

    return {"status": "Notification sent to Zoho Cliq"}

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Sentry to Zoho Cliq Webhook Forwarder!"}

