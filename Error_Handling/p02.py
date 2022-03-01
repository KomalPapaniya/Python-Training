import time
counter = 0
while(counter<500):
    try:
        time.sleep(1)
        print(counter+1)
        counter += 1
    except KeyboardInterrupt:
        pass