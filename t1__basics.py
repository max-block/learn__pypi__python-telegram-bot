import logging
import os

import dotenv
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.error import BadRequest, ChatMigrated, NetworkError, TelegramError, TimedOut, Unauthorized
from telegram.ext import CommandHandler, Filters, InlineQueryHandler, MessageHandler, Updater

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

dotenv.load_dotenv()
token = os.getenv("TOKEN")

updater = Updater(token=token, use_context=True)


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


def caps(update, context):
    text_caps = " ".join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)


def inline_caps(update, context):
    query = update.inline_query.query
    if not query:
        return
    results = list()
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title="Caps",
            input_message_content=InputTextMessageContent(query.upper()),
        )
    )
    context.bot.answer_inline_query(update.inline_query.id, results)


def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")


def error_callback(update, context):
    try:
        raise context.error
    except Unauthorized:
        # remove update.message.chat_id from conversation list
        print("Unauthorized error")
    except BadRequest:
        # handle malformed requests - read more below!
        print("BadRequest error")
    except TimedOut:
        # handle slow connection problems
        print("TimedOut error")
    except NetworkError:
        # handle other connection problems
        print("NetworkError error")
    except ChatMigrated as e:
        # the chat_id of a group has changed, use e.new_chat_id instead
        print("ChatMigrated error")
    except TelegramError:
        # handle all other telegram related errors
        print("TelegramError error")


updater.dispatcher.add_handler(CommandHandler("start", start))
updater.dispatcher.add_handler(CommandHandler("caps", caps))
updater.dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), echo))
updater.dispatcher.add_handler(InlineQueryHandler(inline_caps))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))  # it must be at the last position!

updater.dispatcher.add_error_handler(error_callback)

updater.start_polling()
