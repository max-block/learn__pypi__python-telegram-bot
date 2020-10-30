import os

import dotenv
from telegram import Update
from telegram.ext import CallbackContext, CommandHandler, Updater


def cmd1_handler(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    username = update.effective_chat.username
    params = context.args
    message = f"chat_id: {chat_id}, username: {username}, params={params}"
    context.bot.send_message(chat_id, message)


def main():
    dotenv.load_dotenv()
    token = os.getenv("TOKEN")

    updater = Updater(token=token, use_context=True)
    updater.dispatcher.add_handler(CommandHandler("cmd1", cmd1_handler))

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
