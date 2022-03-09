import threading
import time

List = []

def Fruit():
    """
    Function to print fruits
    """
    global List
    for i in ["Apple", "Mango", "Orange", "Guava", "Watermelon"]:
        time.sleep(1)
        List.append(i)
        print(List)

def Number():
    """
    Function to print numbers
    """
    global List
    for i in [12, 3, 6, 21, 10]:
        time.sleep(1)
        List.append(i)
        print(List)

# creating thread
number_thread = threading.Thread(target= Number)
fruit_thread = threading.Thread(target= Fruit)

# starting number thread
number_thread.start() 

# starting fruit thread
fruit_thread.start()

number_thread.join()
fruit_thread.join()
