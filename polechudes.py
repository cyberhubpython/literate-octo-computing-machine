import random;

class Game:
    words=[
        'helicopter',
        'astranaut',
        'universe'
    ]

    def __init__(self,) -> None:
        self.guessedLetters = ['r'];
        pass

    def start(self):
        self.getRandWord();
        print('game is started');
        letterOrWord =  input('скажи букву или слово: ');
        self.checkLetterOrWord(letterOrWord);

    def checkLetterOrWord(self, letterOrWord):
        # print(letterOrWord in self.currentWord, self.currentWord, letterOrWord);
        if  letterOrWord in self.currentWord:
            print(f'откройте букву {letterOrWord}');
    
    def getRandWord(self) :
        self.currentWord = Game.words[random.randrange(0, len(Game.words))]
        self.showWord()
       

    def showWord(self):
        current = self.currentWord;
        for letter in current:
            if letter in self.guessedLetters :
                continue;
            current = current.replace(letter, '*');
                    
        print(current,  f"len: {len(self.currentWord)}");




game = Game();

game.start();