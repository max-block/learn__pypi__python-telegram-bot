import os

import dotenv
from telegram.ext import Filters, MessageHandler, Updater


def message_handler(update, context):
    print("update", update)
    print("context", context)


def main():
    dotenv.load_dotenv()
    token = os.getenv("TOKEN")

    updater = Updater(token=token, use_context=True)
    updater.dispatcher.add_handler(MessageHandler(Filters.all, message_handler))

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
