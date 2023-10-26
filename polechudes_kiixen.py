import random 
class FOD:
    def start(self):
        words= ["crazy", "billion", "extravagance"]
        self.guessedLetters= []
        self.selectedWord= random.choice(words)
        # print(self.selectedWord)

        # print(self.showHiddenWord());
        # while "*" in self.hiddenWord != True : 
        #     self.askLetterOrWord();
        #     self.showHiddenWord();
        # print('congrats');
       
    def letterOrWordAsked(self, letterOrWord):
       
        if letterOrWord in self.selectedWord:
           
            self.guessedLetters.extend([l for l in letterOrWord])
            return "You have guessed a letter/word"
        else :
            return "Try again you haven't guessed"

    
    def showHiddenWord(self):
        self.hiddenWord=self.selectedWord
        for letter in self.hiddenWord:
            if letter in self.guessedLetters:
                continue
            self.hiddenWord=self.hiddenWord.replace(letter,"*")
        return self.hiddenWord, len(self.hiddenWord)
        


