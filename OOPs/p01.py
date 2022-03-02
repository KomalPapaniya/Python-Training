class IncorrectInput(Exception):
    pass

class Flashcard:
    def __init__(self, Word, Meaning):
        self.Word = Word
        self.Meaning = Meaning
    
    def __str__(self):
        return str(self.Word) + ' ( ' + str(self.Meaning) + ' )'
flash = []
while True:
    W = input("Enter Word: ")
    M = input("Enter Meaning: ")
    My_Object = Flashcard(W, M)
    flash.append(str(My_Object))
    try:
        Repeat = input("Enter 1 if you want to add another flashcard else enter 0: ")
        if Repeat != '0' and Repeat != '1':
            raise IncorrectInput
    except IncorrectInput:
        while True:
            v = input("Enter either 0 or 1: ")
            if v == '0' or v == '1':
                Repeat = v
                break    
    if Repeat == '0':
        break
    else:
        if Repeat == '0':
            break
        elif Repeat == '1':
            continue

print("\nYour flashcards")
for i in flash:
    print(">", i)