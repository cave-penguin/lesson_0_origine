from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor
from aiogram import types

api = "7887074932:AAGWX-FV2p_foXbF05fSXiAHuZ6LN8_zo8g"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
kb = ReplyKeyboardMarkup(resize_keyboard=True, )
button = KeyboardButton(text="Информация")
button2 = KeyboardButton(text="Начало")
kb.add(button)
kb.add(button2)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.answer("Привет!", reply_markup=kb)


@dp.message_handler(text="Информация")
async def inform(message: types.Message):
    await message.answer("Информация о боте!")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
