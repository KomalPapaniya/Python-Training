def Unique():

    userInput = input("Enter a sequence of numbers : ")
    sequence = list(int(n) for n in userInput.split())
    # print(sequence)
    for number in sequence:
        if sequence.count(number) > 1:
            print("NOT UNIQUE")
            break
    else:
        print("UNIQUE")

Unique()