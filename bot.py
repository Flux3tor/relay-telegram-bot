import asyncio
import os
from pyrogram import Client
from aiogram import Bot, Dispatcher, executor, types

BOT_TOKEN = os.getenv("8570147915:AAEZrDlzJg3OpZzyWI-5x-jzZC70VrZ15X8")
API_ID = int(os.getenv("32850564"))
API_HASH = os.getenv("08ed43687636aee6d1aa06689d335afe")

TARGET_BOT = "Porn_Paradise_Bot"  # without @

user = Client(
    "user_session",
    api_id=API_ID,
    api_hash=API_HASH
)

user.start()

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

lock = asyncio.Lock()

@dp.message_handler()
async def relay(message: types.Message):
    async with lock:
        await asyncio.sleep(2)

        user.send_message(TARGET_BOT, message.text)
        reply = user.listen(TARGET_BOT, timeout=15)

        if not reply:
            await message.reply("No response")
            return

        if reply.photo:
            await bot.send_photo(
                message.chat.id,
                reply.photo.file_id,
                caption=reply.caption or ""
            )
        elif reply.video:
            await bot.send_video(
                message.chat.id,
                reply.video.file_id,
                caption=reply.caption or ""
            )
        else:
            await message.reply("Only photos/videos supported")

if __name__ == "__main__":
    executor.start_polling(dp)
