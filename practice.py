from aiogram import Bot, Dispatcher, types, Router;
import asyncio;
from aiogram.types import Message
from aiogram.filters.command import Command;

names = ["Iskandar", "Aleksandr", "Mokhinur"];

temp = names[0];
names[0] = names[1];

names[1] = temp;

print(names);

x,y,z = 1,2,3

names[0], names[1] = names[1], names[0]

print(names);
txt = 'asfghjfhgewrtyryiljhjhcgfsdhjytfghdgf';
print([symbol for symbol in txt]);
symbolsList = [];
symbolsList[:0] = txt;
print(list(txt));


print(symbolsList);


class Game:

    def __init__(self, player: str) -> None:
        self.isStarted = False;
        self.isEnded = False;
        self.steps = []
        self.player = player;

    def start(self):
        self.isStarted = True;
        print('game is started');


    def addStep(self, a):
        self.steps.append(a);
        print('step has been registered');

    def end(self):
        self.isEnded = True;
        print('game is over!');
    def score(self):
        score = 0;
        for step in self.steps:
            score+= len(step.split(' '));
    
        return score;

    def __str__(self) -> str:
        return f'Game(isStarted={self.isStarted}, steps={self.steps}, isEnded={self.isEnded})';

game = Game('bot');

print(game);

game.start();
game.addStep('asdggfg, asd asd,as dasds');
print(game);


currentGames: dict[int, Game] = {
};

dp = Dispatcher();



@dp.message(Command('start'))
async def command_start_handler(message: Message):
    await message.answer('hello, for start game send command /s');



@dp.message(Command('s'))
async def command_s_handler(message: Message):
    currentGames[message.chat.id] = Game(player=message.chat.first_name);
    await message.answer('game started');

@dp.message()
async def command_handler(message: Message):
    currentGames[message.chat.id].addStep(message.text)

    # await message.answer(txt);
    for chatId in currentGames.keys():
        txt = '';
        for game in currentGames.values():
            txt += f"{'you' if game.player == currentGames[chatId].player else game.player}: {game.score()}\n"
        await message.bot.send_message(chat_id= chatId, text= txt);




async def main() -> None:
    bot = Bot('6935433814:AAHAe5BYlLzNqkvBVcxzcGCFfWtZLKapGKY');

    await dp.start_polling(bot);


if __name__ == "__main__":

    asyncio.run(main())
