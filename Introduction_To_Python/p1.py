def Unique():

    userInput = input("Enter a sequence of numbers : ")
    sequence = list(int(n) for n in userInput.split())
    # print(sequence)
    for number in sequence:
        if sequence.count(number) > 1:
            print("All numbers are NOT UNIQUE")
            break
    else:
        print("All numbers are UNIQUE")

Unique()