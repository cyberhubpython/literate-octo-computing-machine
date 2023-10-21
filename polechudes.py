import random;
class Word:
    def __init__(self, w):
        self.w = w;
        self.length = len(w);
    
    def __iter__(self):
        self.count = 0;

    def __next__(self):
        x = self.w[self.count] if self.w[self.count] in self.guessedLetters else '*';
        self.count+=1;
        return x;

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
        if self.checkLetterOrWord(letterOrWord):
            self.guessedLetters.append(letterOrWord)
            self.showWord();
    

    def checkLetterOrWord(self, letterOrWord):
        # print(letterOrWord in self.currentWord, self.currentWord, letterOrWord);
        if  letterOrWord in self.currentWord:
            print(f'откройте букву {letterOrWord}');
            return True;
        return False;
    
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