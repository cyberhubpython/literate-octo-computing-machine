# /start - которая будет показывать приветственное сообщение, 
# все действующие команды нашего бота
# /create {title} - {priority} (vajniy, ne osobo vajniy) для 
# создания нового таска
# /all - показывать весь список задач
# /done {id}
# /clear

from aiogram import Bot, Dispatcher;
import asyncio
from aiogram.filters import Command
from aiogram.types import Message

class Task :
 def __init__(self, title, priority):
     self.title = title
     self.priority = priority

dp= Dispatcher()
tasks ={ 5148415630: [] }

@dp.message(Command("start"))
async def command_start_handler(message:Message):
    await message.answer("""
Greetings^^ 
/create - creates new text 
/all - shows all to do's 
/done - removes data 
/clear - remove all
           """)
    

@dp.message(Command("create"))
async def command_create_handler(message:Message):
    try:
        title,priority= message.text.replace("/create","").split("-")
        print(title,priority)
        tasks[message.chat.id] = tasks[message.chat.id] if  message.chat.id in  tasks else [];
        tasks[message.chat.id].append(Task(title, priority));
        print(tasks)
        await message.answer("your task successfully added to the list.")
    except Exception as e:
        print(e.with_traceback());
        await message.answer("enter title amd priority using command formatted as: /create title-priority")

@dp.message(Command("all"))
async def command_all_handler(message:Message): 
    # tasksStr = '\n'.join(map(lambda task:  f"{task.title} - {task.priority}",tasks[message.chat.id]));
    tasksStr = "all tasks: \n"
    for task in tasks[message.chat.id]:
        tasksStr += f'\n{tasks[message.chat.id].index(task)+1}. {task.title} : {task.priority};'
    await message.answer(tasksStr)

@dp.message(Command("done"))
async def command_done_handler(message:Message): 
    removeIds= message.text.replace("/done", "").split(",")
    for id in removeIds:
        tasks[message.chat.id].remove(tasks[message.chat.id][int(id)-1])
    await message.answer("all has been removed")


@dp.message(Command("clear"))
async def command_clear_handler(message:Message): 
    tasks[message.chat.id].clear();
    await message.answer("all cleared")

async def main():
    bot= Bot("6935608022:AAGm6fOmDBn0lDp8aBYPi_l9bwre3ceAA-8")
    await dp.start_polling(bot)
    

asyncio.run(main())