from aiogram import Bot, Dispatcher, executor, types
from datetime import datetime, timedelta


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
# chat_id=-1001321252394
arr = {}


@dp.message_handler()
async def poll(message):
    try:
        print(message)
        try:
            chat_member = await bot.get_chat_member(message.chat.id, message["from"].id)
            status = chat_member["status"]
            print(status)
        except Exception as e:
            print(repr(e))
            status = "member"
        if status not in ["member", "restricted"] and "/poll" in message.text:
            await bot.delete_message(
                chat_id=message.chat.id, message_id=message.message_id
            )

    except Exception as e:
        print(repr(e))


@dp.message_handler(
    content_types=[types.ContentType.STICKER, types.ContentType.ANIMATION]
)
async def one(message):
    global arr

    print(arr)
    try:
        chat_member = await bot.get_chat_member(message.chat.id, message["from"].id)
        status = chat_member["status"]
        print(status)
    except Exception as e:
        print(repr(e))
        status = "member"
    if status not in ["member", "restricted"]:
        return
    arr[message["from"].id] = message
    if message["from"].id in arr.keys():
        print(message.date - arr[message["from"].id].date)
        if message.date - arr[message["from"].id].date <= timedelta(seconds=30):
            await bot.delete_message(
                chat_id=message.chat.id, message_id=message.message_id
            )

    await bot.restrict_chat_member(
        message.chat.id,
        message["from"].id,
        types.chat_permissions.ChatPermissions(
            can_send_messages=True,
            can_send_media_messages=True,
            can_send_polls=True,
            can_send_other_messages=False,
            can_add_web_page_previews=True,
            can_change_info=True,
            can_invite_users=True,
            can_pin_messages=True,
        ),
        message.date + timedelta(seconds=31),
    )

    print(arr)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
