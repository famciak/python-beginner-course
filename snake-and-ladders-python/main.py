
import random

player1_position = 0
player2_position = 0

player_one = "player one"
player_two = "player two"

from_snack = [12, 23, 24, 30, 56, 80, 98]
to_snack = [1, 15, 3, 25, 40, 60, 2]

from_ladders = [13, 50, 81]
to_ladders = [30, 71, 95]

player1_authorization = False
player2_authorization = False


while True:

    INPUT = input("press any button for player 1 : ")
    tas = random.randint(1, 6)

    if player1_position == 0 and tas == 6:
        player1_authorization = True

    if player1_authorization:

        if player1_position + tas <= 100:
            player1_position = tas + player1_position

        print(f"tas = {tas} {player_one} position >> {player1_position}")

        if player1_position in from_snack:
            player_index = from_snack.index(player1_position)
            player1_position = to_snack[player_index]
            print(f"player position >> {player1_position}")

        if player1_position in from_ladders:
            player_index = from_ladders.index(player1_position)
            player1_position = to_ladders[player_index]
            print(f"player position >> {player1_position}")


    INPUT = input("press any button for player 2 : ")
    tas = random.randint(1, 6)

    if player2_position == 0 and tas == 6:
        player2_authorization = True

    if player2_authorization:

        if player2_position + tas <= 100:
            player2_position = tas + player2_position

        print(f"tas = {tas} {player_two} position >> {player2_position}")

        if player2_position in from_snack:
            player_index = from_snack.index(player2_position)
            player2_position = to_snack[player_index]
            print(f"player position >> {player2_position}")

        if player2_position in from_ladders:
            player_index = from_ladders.index(player2_position)
            player2_position = to_ladders[player_index]
            print(f"player position >> {player2_position}")
