import time, random
players = ['Komal', 'Vishruti', 'Aksh', 'Kshitij', 'Prachi', 'Praveen']
players_left = len(players)
total_time = 0
r = 1
time.sleep(1)
print("-----------------------------------------------------------------------------------------")
print("                                HOT POTATO GAME!!!")
print("-----------------------------------------------------------------------------------------")
 
time.sleep(1)
print("Starting in...")
for i in range(3,0,-1):
    time.sleep(1)
    print(i)
time.sleep(1)
print("GO!!!")
time.sleep(1)
 
# print("\nPLAYERS = ",players, "\n")
# time.sleep(3)
 
while players_left > 1:
    print('---------------------------ROUND {}------------------------------'.format(r))
    time.sleep(1)
    player = 0
    round_duration = random.uniform(5, 20)
    while total_time <= round_duration:
        print(players[player], "---holds hot potato")
        holding_time = float("{:.2f}".format(random.uniform(0.1,3.0)))
        time.sleep(holding_time)
        total_time += holding_time
        turn = players[player]
        player += 1
        if player == players_left:
            player = 0
 
    print("\nTIME UP\n")
    print("{} is out !!! 😬\n".format(turn))
    players.remove(turn)
 
    total_time = 0
    players_left -= 1
    r += 1
    time.sleep(3)
 
print("----------------------{} wins the game 😎🥳🎉-------------------------\n".format(players[0]))
