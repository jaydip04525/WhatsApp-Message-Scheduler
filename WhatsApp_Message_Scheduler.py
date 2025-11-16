import pywhatkit
import datetime
import time

# -------- List of phone numbers --------
numbers = ["+919339355596"]

message = "🎉 Happy Birthday! Wishing you a fantastic year ahead! 🎂✨"

# --- Set your target date & time ---
year = 2025
month = 11
day = 16
hour = 6
minute = 19

target_time = datetime.datetime(year, month, day, hour, minute)
now = datetime.datetime.now()

# -------- Check if time is passed --------
if now > target_time:
    print("⛔ Scheduled time has already passed. Message will NOT be sent.")
    exit()

# -------- Wait until exact time --------
wait_seconds = (target_time - now).total_seconds()
print(f"⏳ Waiting {wait_seconds} seconds until scheduled time...")
time.sleep(wait_seconds)

# -------- Send message instantly --------
for phone in numbers:
    print(f"📩 Sending message to {phone}...")

    pywhatkit.sendwhatmsg_instantly(
        phone,
        message,
        wait_time=10,   # how long to wait for WhatsApp Web to load
        tab_close=True,
        close_time=3
    )

    time.sleep(5)
