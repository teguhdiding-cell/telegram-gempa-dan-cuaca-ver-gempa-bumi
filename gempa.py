import requests
import os

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

url = "https://data.bmkg.go.id/DataMKG/TEWS/autogempa.json"

data = requests.get(url).json()
gempa = data["Infogempa"]["gempa"]

pesan = f"""
🚨 GEMPA TERBARU BMKG

📍 {gempa['Wilayah']}
📏 Magnitudo : {gempa['Magnitude']}
📌 Kedalaman : {gempa['Kedalaman']}

🕒 {gempa['Tanggal']} {gempa['Jam']}

⚠ {gempa['Potensi']}

#BMKG
#GempaIndonesia
"""

requests.post(
    f"https://api.telegram.org/bot{TOKEN}/sendMessage",
    data={
        "chat_id": CHAT_ID,
        "text": pesan
    }
)
