import requests
import time

BOT_TOKEN = "8834672342:AAH8W0iQx7hlQ3d84-8neh_Vs0Q1uxfZS-0"
CHANNEL_ID = "@fewtiny"

def get_price():
    url = "https://api.binance.com/api/v3/ticker/24hr?symbol=TRXUSDT"
    data = requests.get(url).json()
    return data["lastPrice"], data["priceChangePercent"]

while True:
    try:
        price, change = get_price()

        if float(change) >= 0:
            dot = "🟢"
        else:
            dot = "🔴"

        text = f"""💎 TRON (TRX)

💲 Price: ${price}
{dot} ({change}%)

⏰ {time.strftime("%H:%M:%S")}
"""

        requests.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            data={
                "chat_id": CHANNEL_ID,
                "text": text
            }
        )

        time.sleep(60)

    except Exception as e:
        print(e)
        time.sleep(60)
