import os

import dotenv
from telegram import Bot


def main():
    dotenv.load_dotenv()
    token = os.getenv("TOKEN")
    chat_id = os.getenv("CHAT_ID")

    if not token or not chat_id:
        print("TOKEN or CHAR_ID is not set")
        exit(1)

    bot = Bot(token=token)
    bot.send_message(chat_id, "bla bla bla")


if __name__ == "__main__":
    main()
