import asyncio
import telegram
from polechudes_kiixen import FOD

async def main():
    bot = telegram.Bot("6935608022:AAGm6fOmDBn0lDp8aBYPi_l9bwre3ceAA-8");
    update = None;
    
    game= FOD()
    game.start()
    
    
    while True:
        async with bot:
            # print(await bot.get_me())
            try:
                update = (await bot.getUpdates(offset= (update.update_id + 1) if update != None else None, limit =1, timeout=5))[0];
                print(update.update_id);
            
                message: telegram.Message = update.message
                print(message.text.lower())
                
                game.showHiddenWord()
                while "*" in game.hiddenWord != True : 
                    
                    await bot.sendMessage(chat_id = message.chat.id, text= "Enter your Letter or Word:")
                    update = (await bot.getUpdates(offset=(update.update_id + 1) if update != None else None, limit =1, timeout=60))[0];
                    letterOrWord = update.message.text
                    if letterOrWord in game.selectedWord:
            
                        game.guessedLetters.extend([l for l in letterOrWord])
                        await bot.sendMessage(chat_id= message.chat.id, text= "You have guessed a letter/word")
                    else :
                        await bot.sendMessage(chat_id=message.chat.id,text= "Try again you haven't guessed")
                    

                    await bot.sendMessage(chat_id = message.chat.id, text=game.showHiddenWord())

                await bot.sendMessage(chat_id= message.chat.id, text= "Congrats,you have rocked it!")
            except Exception as error:
                print('сообщений не было, идем в след цикл', error);


                # print(message.text.lower() in ['hello',"hi"]);
                # if message.text.lower() in ["what is your name?", "what's your name?"]:
                #     await bot.sendMessage(chat_id = message.chat.id, text= "I am a bot")
                # if message.text.lower() in ['hello a',"hi"]:  
                #     await bot.sendMessage(chat_id = message.chat.id, text="Hi")
               
            
print(__name__); 

if __name__ == '__main__':
    asyncio.run(main())