import os

import dotenv
from telegram import Update
from telegram.ext import CallbackContext, Filters, MessageHandler, Updater


def message_handler(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    username = update.effective_chat.username
    msg = update.message.text
    message = f"chat_id: {chat_id}, username: {username}, msg={msg}"
    context.bot.send_message(chat_id, message)


def main():
    dotenv.load_dotenv()
    token = os.getenv("TOKEN")

    updater = Updater(token=token)
    updater.dispatcher.add_handler(MessageHandler(Filters.all, message_handler))

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
