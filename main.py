import requests
import time

BOT_TOKEN = "8834672342:AAH8W0iQx7hlQ3d84-8neh_Vs0Q1uxfZS-0"
CHANNEL_ID = "@fewtiny"

while True:
    try:
        url = "https://api.binance.com/api/v3/ticker/price?symbol=TRXUSDT"
        data = requests.get(url).json()

        price = data["price"]

        text = f"""💎 TRON (TRX)

💰 Price: ${price}

🕒 {time.strftime("%H:%M:%S")}
"""

        requests.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            data={
                "chat_id": CHANNEL_ID,
                "text": text
            }
        )

        print("Message Sent")
        time.sleep(60)

    except Exception as e:
        print(e)
        time.sleep(60)
