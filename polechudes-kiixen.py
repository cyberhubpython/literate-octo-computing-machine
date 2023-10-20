import random 
class FOD:
    def start(self):
        words= ["crazy", "billion", "extravagance"]
        self.guessedLetters= []
        self.selectedWord= random.choice(words)
        # print(self.selectedWord)

        self.showHiddenWord()
        while "*" in self.hiddenWord != True : 
            self.askLetterOrWord()
            self.showHiddenWord()
        print("Congrats, you've rocked it!")


    def askLetterOrWord(self):
        letterOrWord= input("Enter your Letter or Word: ")
        if letterOrWord in self.selectedWord:
           
            self.guessedLetters.extend([l for l in letterOrWord])
            print("You have guessed a letter/word")
        else :
            print("Try again you haven't guessed")

    
    def showHiddenWord(self):
        self.hiddenWord=self.selectedWord
        for letter in self.hiddenWord:
            if letter in self.guessedLetters:
                continue
            self.hiddenWord=self.hiddenWord.replace(letter,"*")
        print(self.hiddenWord, len(self.hiddenWord))

    
game= FOD()
game.start()


