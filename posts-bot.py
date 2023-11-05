import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command 
from aiogram.types import Message




roles:list[str] = ['admin', 'analyst', 'reader'];


class User:
    def __init__(self, id:int, fullname:str, role:str, isApproved = False) -> None:
      self.id = id  
      self.fullname = fullname  
      self.role = role
      self.isApproved = isApproved




users :dict[int, User] = {
    795034428: User(795034428, "Sasha", roles[0],),
    995189551: User(995189551, 'Саша', roles[1], isApproved= True)
}
posts = {
    10: {
        'title': 'post 1',
        'description': 'lorem== sfs fdsfjk fsh',
        'views': 1200,
    }
}

dp = Dispatcher();

@dp.message(Command('start'))
async def start(message: Message):
    user = users[message.chat.id];
    texts =  {
                roles[0]: "privet admin", 
                roles[1]: 'privet analyst', 
                roles[2]: 'priver reader',
            }
    msgText = texts[user.role ]

    await message.answer(msgText);




@dp.message(Command('details'))
async def deteails(message: Message):
    id = int(message.text.replace('/details', ""))
    user = users[message.chat.id] 

    if id not in posts:
        return await message.reply('net takogo posta');

    if not user.isApproved:
        return await message.answer('ty eshye ne proshel proverku');


    if user.role == roles[0] :        
        await message.reply(f'{user.name}, napishi /delete [id] chtobi udalit');
    elif user.role == roles[1]:
        await message.reply(f'{user.name}, napishi /publish [id] dlya togo chtobi reklamit\'')
    else:
        await message.reply(f'{user.name}, eta komanda tebe ne dostupna')
        # match user.role:
        #     case "admin":
        #         await message.reply('napishi /delete {id} chtobi udalit');
        #     case "analyst":
        #         await message.reply('napishi /publish {id} dlya togo chtobi reklamit\'')
        #     case _:
        #         await message.reply('eta komanda tebe ne dostupna')


        
async def main():

    bot = Bot("6881326098:AAEbpDodIFDdQwUHn_rqUFfVvZNUMrXu2j0")

    await dp.start_polling(bot)

if __name__ == "__main__":
   asyncio.run(main())