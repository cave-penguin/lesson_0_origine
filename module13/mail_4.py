from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
    KeyboardButton,
)
from aiogram.utils import executor
from aiogram import types

api = "7887074932:AAGWX-FV2p_foXbF05fSXiAHuZ6LN8_zo8g"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = InlineKeyboardMarkup()
button = InlineKeyboardButton(text="Информация", callback_data="info")
kb.add(button)

start_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Info")],
        [KeyboardButton(text="shop"), KeyboardButton(text="donate")],
    ],
    resize_keyboard=True,
)


@dp.message_handler(commands=["start"])
async def starter(message: types.Message):
    await message.answer("Рады вас видеть!", reply_markup=start_menu)


# @dp.callback_query_handler(text="info")
# async def info(call):
#     await call.message.answer("Информация о боте")
#     await call.answer()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
