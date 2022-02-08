import random

def loadAnswers():
    with open("../data/answers.txt", 'r') as f:
        text = f.read()
        return eval(text)

def loadGuesses():
    with open("../data/allowed.txt", "r") as f:
        text = f.read()
        return eval(text) 

class Wordle:
    def __init__(self):
        self.answers = loadAnswers()
        self.possibilities = set(loadGuesses() + self.answers) 
        self.answer = self.answers[random.randint(0, len(self.answers))]
        self.turnCount = 0
        self.current = ""

    def checkWord(self):
        response = ""
        for i in range(len(self.current)): #could hardcode to range(5)
            if self.current[i] == self.answer[i]:
                response += "G" #Corresponds to getting the right letter in the right spot
            elif self.current[i] in self.answer:
                response += "Y" #Right letter wrong spot
            else:
                response += "*" #Wrong letter altogether
        return response

    def guess(self):
        guessWord = input("Please guess a word: ")
        if guessWord not in self.possibilities:
            print("Not a valid guess, try again. \n")
            self.guess()
        else:
            self.current = guessWord
            print(self.checkWord())

    def turn(self):
        print(f"You are on turn: {self.turnCount + 1}. You have {6-self.turnCount} guesses remaining")
        self.guess()
        self.turnCount += 1

    def play(self):
        while self.turnCount < 6 and self.current != self.answer:
            self.turn()
        print("Wordle Game completed.")
        print(f"The answer was: {self.answer}")
if __name__ == "__main__":
    game = Wordle()
    game.play()