from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
# chat_id=-1001321252394
@dp.message_handler()
async def poll(message: types.Message):
    try:
        print(message)
        # if message.chat.id==chat_id and message["from"]["username"] in ["rostcraft","Extrematorx"] and "/poll " in message.text:
        #    msg=message.text.replace("/poll ","")
        #    await bot.send_poll(chat_id,question=msg,options=["9","10","11","12"], open_period=90)
        chat_member = await bot.get_chat_member(message.chat.id, message["from"].id)
        status = chat_member["status"]
        if (
            status in ["Вчитель", "Вчителька", "Адмін"]
            and "/poll " in message.text
        ):
            msg = message.text.replace("/poll ", "")
            await bot.send_poll(
                message.chat.id,
                question=msg,
                options=["9", "10", "11", "12"],
                open_period=90,
            )
    except Exception as e:
        print(repr(e))


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
