import os
import requests

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
SERVICE_URL = os.getenv('SERVICE_URL')

def send_telegram_message(message):
  """Send a message to a Telegram chat using a bot."""
  url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
  payload = {
    'chat_id': TELEGRAM_CHAT_ID,
    'text': message
  }
  try:
    response = requests.post(url, data=payload)
    if response.status_code == 200:
      print("Notification sent successfully.")
    else:
      print(f"Failed to send message. Status code: {response.status_code}")
  except Exception as e:
    print(f"Error sending message: {e}")

def check_service():
  """Ping the service URL and check if it's running"""
  try:
    response = requests.get(SERVICE_URL)
    if response.status_code == 200:
      print(f"Service at {SERVICE_URL} is running.")
    else:
      message = f"Service at {SERVICE_URL} is down. Status code: {response.status_code}"
      print(message)
      send_telegram_message(message)
  except requests.exceptions.RequestException as e:
    message = f"Failed to reach {SERVICE_URL}: {e}"
    print(message)
    send_telegram_message(message)

if __name__ == "__main__":
  check_service()
