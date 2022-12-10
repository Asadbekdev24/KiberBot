

import logging

from aiogram import Bot, Dispatcher, executor, types

import aiogram.utils.markdown as md

from aiogram import Bot, Dispatcher, types

from aiogram.contrib.fsm_storage.memory import MemoryStorage

from aiogram.dispatcher import FSMContext

from aiogram.dispatcher.filters import Text

from aiogram.dispatcher.filters.state import State, StatesGroup

from aiogram.types import ParseMode

from aiogram.utils import executor

API_TOKEN = '5833776592:AAFs8971d5uE_6ncNh934vU7V1DlBKyNkDE'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


class Form(StatesGroup):

    shifr = State()
    deshir = State()
    kod = State()




@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Assalomu alaykum! Botimizdan foydalanish\nyo'riqnomasi bilan tanishib chiqish uchun uchun /help buyrug'ini yuboring!")

@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.answer("Assalomu alaykum! Bu bot yordamida matnlarni xavsiz\n shifrlashingiz va shifrlangan matnni maxsus kalit yordamida deshirlashingiz mumkin!")
    await message.answer("Axborotni shifrlash uchun /encryption buyrug'ini deshirlash uchun /decryption buyrug'ini yuboring!")





@dp.message_handler(commands=['encryption'], state='*')
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)


    await message.answer("Matn kiriting!")







@dp.message_handler(state='*')
async def echo(message: types.Message):
         Form.shifr = '4'
         matn = message.text
         shifrmatn=matn[::-1]
         await message.reply(f"Shifrlangan matn: {shifrmatn}")
        # await message.reply(f"Matnni deshirlash uchun kalit: {kalit}")

      # await message.answer("Iltimos botimizdan to'g'ri foydalanish uchun /help buyrug'ini yuborib yo'riqnoma bilan tanishib chiqing!")


@dp.message_handler(commands=['decryption'], state='*')
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)


    await message.answer("Matnni deshifrlash uchun kalitni kiriting:")



@dp.message_handler()
async def echo(message: types.Message):


        #if(kalit==message.text):

          await message.answer("Shifrlangan matnni yuboring")


            #await message.answer("Kalit xato boshqatdan urinib ko'ring")
            #await message.answer("Buning uchun /decryption buyrug'ini yuboring")




@dp.message_handler()
async def echo(message: types.Message):




      matn2 = message.text
      shifrmatn2 = matn2[::-1]
      await message.reply(f"Deshifrlangan matn: {shifrmatn2}")


         # await message.answer(
         #     "Iltimos botimizdan to'g'ri foydalanish uchun /help buyrug'ini yuborib yo'riqnoma bilan tanishib chiqing!")



@dp.message_handler()
async def echo(message: types.Message):

    await message.answer("Iltimos botimizdan to'g'ri foydalanish uchun /help buyrug'ini yuborib yo'riqnoma bilan tanishib chiqing!")



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)