import telebot
import pytz
from datetime import datetime, timedelta
import time

# === CONFIGURATION ===
BOT_TOKEN = "8068629449:AAFk4zcwW22FkrvdmmoQpBGWvqOj1A2xQWk"
CHANNEL_USERNAME = "@Cyberxploitpremium"
TIMEZONE = "Asia/Dhaka"  # BD time

bot = telebot.TeleBot(BOT_TOKEN)

def get_next_times():
    tz = pytz.timezone(TIMEZONE)
    now = datetime.now(tz)
    times = []
    start_times = [now.replace(hour=15, minute=0, second=0), now.replace(hour=23, minute=0, second=0)]

    for start in start_times:
        for i in range(5):
            t = start + timedelta(minutes=7 * i)
            if t > now:
                times.append(t)

    return times[:5]

@bot.message_handler(commands=['start'])
def start_signal(message):
    bot.reply_to(message, "Bot is active! Signals will be sent on schedule.")
    send_signals()

def send_signals():
    times = get_next_times()
    for t in times:
        delay = (t - datetime.now(pytz.timezone(TIMEZONE))).total_seconds()
        if delay > 0:
            time.sleep(delay)
        signal = generate_signal()
        bot.send_message(CHANNEL_USERNAME, signal)

def generate_signal():
    # Customize your signal logic here
    logic = "Strong Resistance Breakout"
    direction = "CALL"
    time_now = datetime.now(pytz.timezone(TIMEZONE)).strftime('%Y-%m-%d %H:%M:%S')
    return f"""
🚧 LIVE BOT SIGNAL 🚧
📊 EURUSD
🕓 {datetime.now(pytz.timezone(TIMEZONE)).strftime('%H:%M')}
⏳ M1
🟢 {direction}
🎯 Logic: {logic}
🧠 Time: {time_now}
🔗 Powered by: @Crystal_ic
"""

bot.polling()
