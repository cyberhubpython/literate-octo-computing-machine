import asyncio
import telegram

async def main():
    bot = telegram.Bot("6935433814:AAHAe5BYlLzNqkvBVcxzcGCFfWtZLKapGKY");
    update = None;
    while True:
        async with bot:
            # print(await bot.get_me())
            try:
                update = (await bot.getUpdates(offset= (update.update_id + 1) if update != None else None, limit
                =1, timeout=5))[0];
                print(update.update_id);
                # message: telegram.Message = (await bot.getUpdates(limit= 1, offset = ))[0].message
                # print(message.text)
                # await bot.sendMessage(chat_id = message.chat.id, text="Hello")
                # await bot.send_dice(chat_id = message.chat.id);
            except:
                print('сообщений не было, идем в след цикл');

print(__name__); 

if __name__ == '__main__':
    asyncio.run(main())