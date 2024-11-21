from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor

api = "7887074932:AAGWX-FV2p_foXbF05fSXiAHuZ6LN8_zo8g"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(text=["Urban", "eer"])
async def urban_message(message):
    print("Urban message")
    await message.answer("Urban message")


@dp.message_handler(commands=["start"])
async def start_message(message):
    print("start message")
    await message.answer("We are glad to see you in our bot!")


@dp.message_handler()
async def all_message(message):
    print("Мы получили сообщение")
    await message.answer(message.text.upper())


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
