from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import random
from datetime import datetime

TOKEN_API = '7237228139:AAGZQ5XFGV1RPBS9NLhLSHuaTwWFwXIsUq8'
bot = Bot(token = TOKEN_API)
dp = Dispatcher(bot)

keyboard1 = InlineKeyboardMarkup(row_width= 1)
button1 = InlineKeyboardButton('Переключиться на клавиатуру 2', callback_data='go_to_2')
button2 = InlineKeyboardButton('Отправь случайное число', callback_data='send_random_number')
keyboard1.add(button1, button2)

keyboard2 = InlineKeyboardMarkup(row_width= 1)
button3 = InlineKeyboardButton('Переключиться на клавиатуру 1', callback_data='go_to_1')
button4 = InlineKeyboardButton('Текущее время', callback_data='send_datetime')
keyboard2.add(button3, button4)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.reply('Ты на клавиатуре 1, нажми кнопку, чтобы перейти на 2', reply_markup= keyboard1)

@dp.callback_query_handler(lambda c: c.data == 'go_to_2')
async def go_to_2(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text('Ты перешёл на 2 клавиатуру, нажми на кнопку, чтобы вернуться на 1', reply_markup = keyboard2)

@dp.callback_query_handler(lambda c: c.data == 'go_to_1')
async def go_to_1(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text('Ты перешёл на 1 клавиатуру, нажми на кнопку, чтобы вернуться на 2', reply_markup= keyboard1)

@dp.callback_query_handler(lambda c: c.data == 'send_random_number')
async def random_number(callback_query: types.CallbackQuery):
    random_num = random.randint(1,100)
    await callback_query.message.answer(f'Ваше случайное число: {random_num}')

@dp.callback_query_handler(lambda c: c.data == 'send_datetime')
async def send_datetime(callback_query: types.CallbackQuery):
    current_time = datetime.now().strftime("%H:%M:%S")
    await callback_query.message.answer(f'Текущее время: {current_time}')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)