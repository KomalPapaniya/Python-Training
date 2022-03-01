class FormulaError(Exception):
    pass

class NumericError(FormulaError):
    pass

class FormatError(FormulaError):
    pass

class OperatorError(FormulaError):
    pass


while True:
    try:
        User_input = input("Enter: ").split(" ")
        if User_input == ["quit"]:
            break
        if len(User_input) != 3:
            raise FormatError

        a = User_input[0].split(".")
        b = User_input[2].split(".")

        if a[0].isnumeric() == False or b[0].isnumeric() == False:
            raise NumericError

        elif User_input[1] != "+" and User_input[1] != "-":
            raise OperatorError

        else:
            A = float(User_input[0])
            B = float(User_input[2])
            if User_input[1] == "+":
                print(A+B)
            elif User_input[1] == "-":
                print(A-B)
    
    except NumericError:
        print("1st and last value should be numeric\n")
    except FormatError:
        print("Input should be 3 space separated values\n")
    except OperatorError:
        print("centre element should be a + or - operator\n")