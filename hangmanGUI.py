from tkinter import *
from tkinter import messagebox
from os import environ
environ.__setitem__('DISPLAY', ':0.0')

class hangman:
    def __init__(self, guessWord):

        self.wordForResult = guessWord.lower()
        self.word = guessWord.lower()
        self.star = '*'*len(self.word) #stars to be displayed
        self.chances = 7
        self.missed = ''

        #creating the game interface
        self.window = Tk()
        self.window.geometry('800x400')
        self.window.title('Hangman')
        self.window.resizable(height=NO, width=NO)


        self.chancesLeftLabel = Label(self.window, text= "Chances Left: ", font='Times 18 bold')
        self.chancesLeftLabel.grid(row=1, column=1, padx=10,sticky=E)

        self.chancesLabel = Label(self.window, text=str(self.chances), font='Times 18 bold')
        self.chancesLabel.grid(row=1, column=2, padx=10,sticky=E)

        self.missedLetterLabel = Label(self.window, text= "Missed Letters: ", font='Times 18 bold')
        self.missedLetterLabel.grid(row=2, column=1, padx=10, sticky=E)

        self.missedLabel = Label(self.window, text= self.missed, font='Times 18 bold')
        self.missedLabel.grid(row=2, column=2, padx=10, sticky=E)

        self.guessWordLabel =  Label(self.window, text='Guess the word: ', font='Times 18 bold')
        self.guessWordLabel.grid(row=0, column=1, padx=10)
        self.label = Label(self.window, text= self.star, font= 'Times 20 bold')
        self.label.grid(row=0, column=2, padx=5)
        self.window.bind('<Key>', self.pressed)

        #creating a hangman
        self.canvas = Canvas(self.window, height=400, width=400)
        self.canvas.grid(row=0, column=0, rowspan=10)

        

        self.window.mainloop()


    @staticmethod
    def wordToList(word):
        lst = []
        for i in word:
            lst.append(str(i))

        return lst

    @staticmethod
    def listToWord(lst):
        word = ''
        for i in lst:
            word += str(i)
        
        return word

    #replacing the star with guess 
    #removing the star of the index where the guess is
    def replaceStar(self, guess):
        wordList = self.wordToList(self.word)
        starList = self.wordToList(self.star)
        
        if guess in wordList:
            while guess in wordList:
                starList[wordList.index(guess)] = guess
                wordList[wordList.index(guess)] = '*'
        else:
            self.chances -= 1
            self.missed += str(guess)
            self.drawhangman()
        
        if self.chances == 0:
            self.guessWordLabel.config(text='The Word is: ')
            self.guessWordLabel.update()
            self.missedLetterLabel.config(text='Result:')
            self.missedLetterLabel.update()
            # self.missedLabel.config(text='You Lost')
            # self.missedLabel.update()
        
        self.star = self.listToWord(starList)
        self.word = self.listToWord(wordList)

        return starList

    #drawing the hangman according to chances
    def drawhangman(self):
        b = self.canvas
        b.create_line(20, 380, 80, 380)
        b.create_line(50, 50, 50, 380)
        b.create_line(50,50,250,50)
        b.create_line(250,50,250,100)
        if self.chances == 6:
            b.create_oval(200,100,300,200)
        elif self.chances == 5:
            b.create_line(250,200,250,250)
        elif self.chances == 4:
            b.create_line(250,250,200,300)
        elif self.chances == 3:
            b.create_line(250,250,300,300)
        elif self.chances == 2:
            b.create_line(250,250,250,300)
        elif self.chances ==1:
            b.create_line(250,300,200,350)
        else:
            b.create_line(250,300,300,350)


    #getting which key is pressed 
    #replacing the pressed kry with right
    def pressed(self, event):

        if self.chances > 0:
            self.replaceStar(str(event.keysym))
            self.label.config(text=self.star)
            self.label.update()
            self.chancesLabel.config(text=str(self.chances))
            self.chancesLabel.update()

        if self.chances>0:
            self.missedLabel.config(text=self.missed)
            self.missedLabel.update()
        else:
            self.missedLabel.config(text='You Lost')
            self.missedLabel.update()
            self.label.config(text=self.wordForResult)
            self.label.update()
            

        if '*' not in self.star:
            self.missedLetterLabel.config(text='Result:')
            self.missedLetterLabel.update()
            self.missedLabel.config(text='You Won')
            self.missedLabel.update()

try:
    hangman('sharma')
except:
    messagebox.showerror(message="THere is an Error!")