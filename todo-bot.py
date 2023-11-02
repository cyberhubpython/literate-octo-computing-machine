import asyncio;
from aiogram import Dispatcher, Bot
from aiogram.filters import Command
from aiogram.types import Message
dp = Dispatcher()


class Todo:
    def __init__(self, title, priority) -> None:
        self.title = title;
        self.priority = priority;



# def decor(fn, **args):
#     print('hi from decorator', args);
#     def d(*arg, **kwargs):
#         print(kwargs['event_update']['message']);
#         for x in kwargs.keys():
#             print(x);
#         return fn(*arg, **kwargs)
    
#     return d


@dp.message(Command('start'))
async def command_start_handler(message: Message):
    await message.answer(
"""
welcome!
my commands:
/create - for create new task with format: {title}-{priority}
/all -
/done - 
/clear -
""");

isCreateCalled = False;

@dp.message(Command("create"))
async def command_create_handler(message: Message):
        context = preparation(message);
        global isCreateCalled;
        try:
            if '-' not in message.text and len(message.text.split(' ')) < 2:
                async def defineTitle(message):
                    context['newTaskTitle'] = message.text;
                    await message.answer('enter task priority:');
                    async def definePriority(message):
                        context['newTaskPriority'] = message.text;   
                        context['tasks'].append(Todo(title= context['newTaskTitle'], priority= context['newTaskPriority'])); 
                    context['steps'].append(definePriority);   
                context['steps'].append(defineTitle);  
                return await message.answer('введите загаловок таска:');
         
            title, priority = message.text.replace('/create', '').split('-')
            context['tasks'].append(Todo(title, priority))
            print(context['tasks']);
        except ValueError as error:
             await message.answer('формат вызова команды /create неверный');


@dp.message(Command("all"))
async def command_all_handler(message:Message): 
    user =  preparation(message);
    # tasksStr = '\n'.join(map(lambda task:  f"{task.title} - {task.priority}",tasks[message.chat.id]));
    tasksStr = "all tasks: \n"

    for task in user['tasks']:
        tasksStr += f'\n{user["tasks"].index(task)+1}. {task.title.strip()}: {task.priority.strip()};'

    await message.answer(tasksStr)


class Context:
    pass


users = {};
def preparation(message):
    if message.chat.id in users:
        return users[message.chat.id];

    users[message.chat.id] = {'steps': [], 'tasks': [], 'personal': {'name': '',}}
    
    return preparation(message);

newTaskTitle = None;
newTaskPriority = None;
@dp.message()
async def message_handler(message: Message) :
    context = preparation(message)
    if len(context['steps']):
        await context['steps'][0](message);
        del context['steps'][0]
    # global newTaskPriority, newTaskTitle;
    # if isCreateCalled and  newTaskTitle == None:
    #     newTaskTitle = message.text;
    #     return await message.answer('enter task priority:');
    # if isCreateCalled :
    #     newTaskPriority = message.text;
    #     accountsData[message.chat.id] = [] if message.chat.id not in  accountsData else accountsData[message.chat.id];
    #     accountsData[message.chat.id].append(Todo(title=newTaskTitle, priority= newTaskPriority));
        
    #     return await message.answer('successfully created');
    
    # await command_start_handler(message);

async def main():
    bot = Bot('6935433814:AAHAe5BYlLzNqkvBVcxzcGCFfWtZLKapGKY')
    await dp.start_polling(bot);
    
    
asyncio.run(main())