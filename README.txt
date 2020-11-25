--> telegram.error.BadRequest: Message is too long
There is no a way how to do it with the library. Split a long text yourself:
if len(info) > 4096:
    for x in range(0, len(info), 4096):
        bot.send_message(message.chat.id, info[x:x+4096])
else:
    bot.send_message(message.chat.id, info)