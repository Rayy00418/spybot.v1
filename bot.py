import telegram
from telegram.ext import CommandHandler, Updater
import json

with open('config.json') as f:
    config = json.load(f)

TOKEN = config["token"]
CHAT_ID = config["chat_id"]

def start(update, context):
    update.message.reply_text(
        "🛸 LEVIATHAN Tools Cam by MIRAY\n\nPilih Mode:\n1. Tangkap Bintang\n2. Pendeteksi Ekspresi\n3. Kamera Luar Angkasa\n\nKetik nomor mode:"
    )

def handle_message(update, context):
    msg = update.message.text.strip()
    if msg in ['1', '2', '3']:
        update.message.reply_text(f"🔗 Link kamu: https://your-domain.com/web/index.html?mode={msg}")
    else:
        update.message.reply_text("Pilih 1 / 2 / 3 bro!")

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
dp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text & ~telegram.ext.Filters.command, handle_message))

updater.start_polling()
updater.idle()