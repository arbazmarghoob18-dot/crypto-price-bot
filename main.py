import requests
import time

BOT_TOKEN = "8834672342:AAH8W0iQx7hlQ3d84-8neh_Vs0Q1uxfZS-0"
CHANNEL_ID = "@fewtiny"

while True:
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=tron&vs_currencies=usd"
data = requests.get(url).json()
price = data["tron"]["usd"]

        price = data["price"]

        text = f"""💎 TRON (TRX)

💰 Price: ${price}

🕒 {time.strftime("%H:%M:%S")}
"""

        requests.post(
            f"https://api.telegram.org/bot{8834672342:AAH8W0iQx7hlQ3d84-8neh_Vs0Q1uxfZS-0}/sendMessage",
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
