import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()


# Your bot token
BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

# Get updates from the bot
url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"
response = requests.get(url)
data = response.json()

print("Response:", data)

if data["ok"] and data["result"]:
    # Get the latest message
    latest = data["result"][-1]
    chat_id = latest["message"]["chat"]["id"]
    print(f"\n✅ Your Chat ID is: {chat_id}")
else:
    print("❌ No messages found. Send a message to your bot first!")