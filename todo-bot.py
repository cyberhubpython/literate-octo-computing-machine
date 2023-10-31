import asyncio;
from aiogram import Dispatcher, Bot
from aiogram.filters import Command
from aiogram.types import Message
dp = Dispatcher()


class Todo:
    def __init__(self, title, priority) -> None:
        self.title = title;
        self.priority = priority;



accountsData = {
    # message.chat.id : [Todo(title, priority)]
}


@dp.message(Command('start'))
async def command_start_handler(message: Message):
    await message.answer(
"""
welcome!
my commands:
/create - for create new task with format: {title}-{priority}
""");
    accountsData[message.chat.id] = [];



@dp.message(Command("create"))

async def command_create_handler(message: Message):
    title, priority = message.text.replace('/create', '').split('-')
    accountsData[message.chat.id].append(Todo(title, priority))

    print();
    print(accountsData);




async def main():
    bot = Bot('6935433814:AAHAe5BYlLzNqkvBVcxzcGCFfWtZLKapGKY')
    await dp.start_polling(bot);
    
    
asyncio.run(main())