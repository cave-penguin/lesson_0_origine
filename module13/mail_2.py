from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.utils import executor

api = "7887074932:AAGWX-FV2p_foXbF05fSXiAHuZ6LN8_zo8g"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    address = State()


@dp.message_handler(text="Заказать")
async def bue(message):
    await message.answer("Send us your address, please")
    await UserState.address.set()


@dp.message_handler(state=UserState.address)
async def fsm_handler(message, state):
    await state.update_data(first=message.text)
    data = await state.get_data()
    await message.answer(f"The package will be sent to {data['first']}")
    await state.finish()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
