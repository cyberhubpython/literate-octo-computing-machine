import aiogram
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

dp = Dispatcher()

dict = {}
#todos "message.chat.id: list"
class Todo():
    def __init__(self, title, priority) -> None:
        self.title = title
        self.priority = priority

    pass

@dp.message(Command("start"))
async def command_start_handler(message: Message):
    print(message.chat)
    return await message.answer("""Welcome, dear user. If you want to use this bot, you have the following commands: 
\n/create - priorities of creating tasks \n/all - all of the existing tasks \n/done - delete chat id, \n/clear - clear tasks""")

@dp.message(Command("create"))
async def command_create_handler(message: Message):
    title, priority = message.text.replace("/create", "").split("-")
    print(title, priority)
    dict[message.chat.id].append(Todo(title, priority))
    pass

@dp.message(Command("all"))
async def command_all_handler(message: Message):
    pass

@dp.message(Command("done"))
async def command_done_handler(message: Message):
    pass

@dp.message(Command("clear"))
async def command_clear_handler(message: Message):
    pass

async def main():
    bot = Bot('6849358088:AAHhK2e1Wayj6ApN0U0-j2wfd_uvdBv2ubY')
    await dp.start_polling(bot)
asyncio.run(main())