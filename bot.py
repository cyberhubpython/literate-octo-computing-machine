from aiogram import Bot, Dispatcher;
from aiogram.types import Message;
from aiogram.filters import Command;
import asyncio;
dp = Dispatcher();
@dp.message(Command('start'))
async def command_start_handler(message: Message):
    print(message.chat);
    if message.chat.username == 'CrazyySasha':
        return await message.answer('poshel von!!');    
    return await message.answer('welcome')
@dp.message()
async def message_handler(message: Message):
    print(message.text);
    await message.answer(text='privet, che xotel ?');
async def main():
    bot = Bot('6935433814:AAHAe5BYlLzNqkvBVcxzcGCFfWtZLKapGKY');
    await dp.start_polling(bot);
asyncio.run(main());

