import requests
import os

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_message(text):
    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": text
        },
        timeout=30
    )

def send_photo(photo_url, caption):
    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendPhoto",
        data={
            "chat_id": CHAT_ID,
            "photo": photo_url,
            "caption": caption
        },
        timeout=30
    )

def read_sent(filename):
    if not os.path.exists(filename):
        return set()

    with open(filename, "r", encoding="utf-8") as f:
        return set(line.strip() for line in f if line.strip())
```

def save_sent(filename, item_id):
with open(filename, "a", encoding="utf-8") as f:
f.write(item_id + "\n")

# ===================================================

# AUTOGEMPA

# ===================================================

try:

```
url = "https://data.bmkg.go.id/DataMKG/TEWS/autogempa.json"

data = requests.get(url, timeout=30).json()

gempa = data["Infogempa"]["gempa"]

gempa_id = (
    gempa["Tanggal"]
    + gempa["Jam"]
    + gempa["Magnitude"]
    + gempa["Wilayah"]
)

sent = read_sent("last_quake.txt")

if gempa_id not in sent:

    shakemap = gempa.get("Shakemap", "")

    caption = f"""
🚨 GEMPA TERBARU BMKG

📍 Lokasi
{gempa['Wilayah']}

📏 Magnitudo
M {gempa['Magnitude']}

📌 Kedalaman
{gempa['Kedalaman']}

🕒 Waktu
{gempa['Tanggal']} | {gempa['Jam']}

⚠ Potensi
{gempa['Potensi']}

━━━━━━━━━━━━━━
Sumber: BMKG
#GempaIndonesia
"""

    if shakemap:

        photo_url = (
            "https://data.bmkg.go.id/DataMKG/TEWS/"
            + shakemap
        )

        send_photo(photo_url, caption)

    else:
        send_message(caption)

    save_sent("last_quake.txt", gempa_id)

except Exception as e:
    print("AUTOGEMPA ERROR:", e)

# ===================================================

# GEMPA TERKINI

# ===================================================

try:

```
url = "https://data.bmkg.go.id/DataMKG/TEWS/gempaterkini.json"

data = requests.get(url, timeout=30).json()

sent = read_sent("sent_terkini.txt")

for gempa in reversed(data["Infogempa"]["gempa"]):

    gempa_id = (
        gempa["Tanggal"]
        + gempa["Jam"]
        + gempa["Magnitude"]
        + gempa["Wilayah"]
    )

    if gempa_id not in sent:

        pesan = f"""
```

📋 GEMPA TERKINI BMKG

📍 Lokasi
{gempa['Wilayah']}

📏 Magnitudo
M {gempa['Magnitude']}

📌 Kedalaman
{gempa['Kedalaman']}

🕒 Waktu
{gempa['Tanggal']} | {gempa['Jam']}

⚠ Potensi
{gempa['Potensi']}

━━━━━━━━━━━━━━
Sumber: BMKG
#GempaTerkini
"""

```
        send_message(pesan)

        save_sent(
            "sent_terkini.txt",
            gempa_id
        )
```

except Exception as e:
print("TERKINI ERROR:", e)

# ===================================================

# GEMPA DIRASAKAN

# ===================================================

try:

```
url = "https://data.bmkg.go.id/DataMKG/TEWS/gempadirasakan.json"

data = requests.get(url, timeout=30).json()

sent = read_sent("sent_dirasakan.txt")

for gempa in reversed(data["Infogempa"]["gempa"]):

    gempa_id = (
        gempa["Tanggal"]
        + gempa["Jam"]
        + gempa["Magnitude"]
        + gempa["Wilayah"]
    )

    if gempa_id not in sent:

        pesan = f"""
```

👥 GEMPA DIRASAKAN BMKG

📍 Lokasi
{gempa['Wilayah']}

📏 Magnitudo
M {gempa['Magnitude']}

📌 Kedalaman
{gempa['Kedalaman']}

🕒 Waktu
{gempa['Tanggal']} | {gempa['Jam']}

📢 Dirasakan
{gempa['Dirasakan']}

━━━━━━━━━━━━━━
Sumber: BMKG
#GempaDirasakan
"""

```
        send_message(pesan)

        save_sent(
            "sent_dirasakan.txt",
            gempa_id
        )
```

except Exception as e:
print("DIRASAKAN ERROR:", e)

print("SELESAI")
