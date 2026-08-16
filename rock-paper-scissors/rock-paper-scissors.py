import random

point_U =0
point_C =0

3
print("this game is paper sisser rock")

games =["paper","sisser","rock"]
try:

    start = input("if you are ready for this game please enter START >> ")
    if start == "START":
        while True :
            try:
                user =input("what do you get { paper }  { sisser }  { rock }  ")
                computer = random.choice(games)
                print(f"user >> {user}  vs  computer >> {computer} ")

                win_game ={"paper":"rock","sisser":"paper","rock":"sisser"}
                if user==computer:
                    print("draw")
                elif win_game[user] == computer:
                    point_U = point_U + 1
                    print(f"your point is >> {point_U}")

                else :
                    point_C = point_C + 1
                    print(f"computer's point is >> {point_C}")
            
                if point_U == 10 :
                    print("user winnnnnn ")
                    exit()

                if point_C ==10:
                    print("computer winnnn, you  lose")
                    exit()
            except: pass


except: pass



else :

    print("this game can't launch ")
