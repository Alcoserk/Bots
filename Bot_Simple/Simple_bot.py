import time
import logging


from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor


TOKEN = ""
TXT = ''''''

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def start_handler(massage: types.Message):
    user_id = massage.from_user.id
    user_full_name = massage.from_user.full_name
    logging.info(f'{user_id=} {user_full_name=} {time.asctime()}')
    await massage.reply(f"Привет, {user_full_name}!")

    for i in range(10):
        time.sleep(1)
        await bot.send_message(user_id, TXT)


if __name__ == '__main__':
    executor.start_polling(dp)

