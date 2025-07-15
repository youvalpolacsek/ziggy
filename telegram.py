import os
from telegram.ext import Updater, CommandHandler

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Ziggy here!")

def echo(update, context):
    message = ' '.join(context.args)
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"You said: {message}")

def start_telegram_bot():
    if not TOKEN:
        print("Telegram token not set.")
        return
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("say", echo))
    updater.start_polling()
