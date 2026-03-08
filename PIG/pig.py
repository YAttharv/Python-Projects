# no error handling
import random
import time
LIMIT = 21
while True:
    players = input("Number of players(2-4): ")
    if players.isdigit():
        players = int(players)
        if (players in [2, 3, 4]):
            break
    print("Enter 2, 3, or 4")

players_score = []
for s in range(players):
    players_score.append(0)

while True:
    for playeridx in range(players):
        print("player " + str(playeridx+1) + "'s turn")
        numOfTurns = int(input("how many times you want to roll: "))
        for i in range(numOfTurns):
            dice = random.randint(1, 6)
            print("You rolled", dice)
            if dice == 1:
                players_score[playeridx] = 0
                print(f"{playeridx+1} rolled 1 so his score is 0")
                break
            players_score[playeridx] += dice
            print("score:", players_score[playeridx])
            if players_score[playeridx] >= LIMIT:
                print(f"Player {playeridx+1} Won")
                quit()
            # time.sleep(1)
        print("player " + str(playeridx+1) + "'s score:", players_score[playeridx])
