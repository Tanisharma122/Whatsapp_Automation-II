"""Send a test WhatsApp message via the Cloud API."""
import sys, asyncio
sys.path.insert(0, "src")

from app.integrations.whatsapp_client import WhatsAppClient
from app.config import settings

async def main():
    recipient = settings.test_recipient_phone or "919876543210"
    print(f"Sending WhatsApp message to {recipient}...")
    try:
        async with WhatsAppClient() as client:
            await client.send_text(
                to=recipient,
                body="Welcome to Cloud Kitchen!\n\nI'm your AI food assistant. Ask me about our menu, place an order, or ask any question!\n\nTry saying:\n- What's on the menu?\n- I'd like to order butter chicken\n- What are your hours?"
            )
        print("SUCCESS - Message sent! Check your WhatsApp now.")
        print("Reply to it - your reply will trigger the webhook.")
    except Exception as e:
        print(f"FAILED: {e}")

asyncio.run(main())
