
import os
import requests
import time

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

def send_message(text):
    if not BOT_TOKEN or not CHANNEL_ID:
        print("Missing BOT_TOKEN or CHANNEL_ID")
        return
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHANNEL_ID, "text": text}
    try:
        response = requests.post(url, data=data)
        print("Message sent:", response.text)
    except Exception as e:
        print("Error sending message:", e)

def main_loop():
    while True:
        send_message("🤖 البوت يعمل الآن ويراقب شبكة سولانا...")
        time.sleep(60)  # كل دقيقة

if __name__ == "__main__":
    main_loop()
