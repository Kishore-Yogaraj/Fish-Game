
# Read File
with open('Description', 'r') as f:
    f_contents = f.read()
    print(f_contents)

# global variable definition
points = 5
globalcount = 0
bait1 = 1
bait2 = 1
bait3 = 1
fishvalue = 0
import random
import sys


# base exception class
class Error(Exception):
    """base class for other exceptions"""
    pass


# spelling exception
class Spelling(Error):
    """raised when the input is spelled wrong"""
    pass


# negative input exception
class GameSpelling(Error):
    """raised when the input is spelled wrong while fishing"""
    pass


# game function for fishing
def game():
    # local variable + dictionary definition
    global points
    global globalcount
    global bait1
    global bait2
    global bait3
    global fishvalue

    # loop for correct inputs
    while True:

        fishdict = {'1': 'Trout', '2': 'Salmon', '5': 'Catfish', '10': 'Bluefish', '25': 'Amberjack',
                    '60': 'Blue Marlin'}

        try:
            bait = input("\n\nPlease enter what type of bait you would like to use: ")
            cast = input("\nType 'fish' to cast your rod! ")

            if cast == "fish" and bait == "simple" or bait == "advanced" or bait == "complex":

                # randomizer
                a = random.randint(0, 100)

                if bait == "simple":
                    conf = bait1
                elif bait == "advanced":
                    conf = bait2
                elif bait == "complex":
                    conf = bait3

                # odds of catching a fish (variable to the percentage given by purchasing rods)
                if 0 <= a and a <= 60 + globalcount and conf > 0:

                    # odds for simple bait
                    if bait == "simple" and bait1 > 0:
                        bait1 = bait1 - 1

                        print("""

,-.
_n_  \
(---)  `-.___________________________________________________________
~^~^~|~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^
|
|                                         }-<#('c
|
|
|                   }-<#('c                           <')"={
|
|      ><>                        <')"={
|                                                <><
|             }<('>             }<('>
J   <')"={

""")
                        print("\nYou caught a fish!")

                        n = random.randint(0, 100)

                        if 0 <= n and n <= 40:
                            points += 1
                            fishvalue = 1
                        elif 41 <= n and n <= 80:
                            points += 2
                            fishvalue = 2
                        elif 81 <= n and n <= 95:
                            points += 5
                            fishvalue = 5
                        elif 96 <= n and n <= 100:
                            points += 25
                            fishvalue = 25

                    # odds for advanced bait
                    if bait == "advanced" and bait2 > 0:
                        bait2 = bait2 - 1

                        print("""

,-.
_n_  \
(---)  `-.___________________________________________________________
~^~^~|~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^
|
|                                         }-<#('c
|
|
|                   }-<#('c                           <')"={
|
|      ><>                        <')"={
|                                                <><
|             }<('>             }<('>
J   <')"={

""")
                        print("\nYou caught a fish!")

                        n = random.randint(0, 100)

                        if 0 <= n and n <= 40:
                            points += 2
                            fishvalue = 2
                        elif 41 <= n and n <= 75:
                            points += 5
                            fishvalue = 5
                        elif 76 <= n and n <= 90:
                            points += 15
                            fishvalue = 15
                        elif 91 <= n and n <= 95:
                            print("You've caught a whale!")
                            points += 60
                            fishvalue = 50
                        elif 96 <= n and n <= 100:
                            print("The fish you caught was a JELLYFISH :(")
                            points -= 15
                            fishvalue = -15

                    # odds for complex bait
                    if bait == "complex" and bait3 > 0:
                        bait3 = bait3 - 1

                        print("""

,-.
_n_  \
(---)  `-.___________________________________________________________
~^~^~|~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^
|
|                                         }-<#('c
|
|
|                   }-<#('c                           <')"={
|
|      ><>                        <')"={
|                                                <><
|             }<('>             }<('>
J   <')"={

""")
                        print("\nYou caught a fish!")

                        n = random.randint(0, 100)

                        if 0 <= n and n <= 25:
                            points += 5
                            fishvalue = 5
                        elif 25 <= n and n <= 50:
                            points += 10
                            fishvalue = 10
                        elif 50 <= n and n <= 75:
                            points += 25
                            fishvalue = 25
                        elif 75 <= n and n <= 85:
                            points += 60
                            fishvalue = 60
                        elif 85 <= n and n <= 100:
                            print("The fish you caught was a SHARK :(")
                            points -= 50
                            fishvalue = -50

                    # statement for catching a fish (prints points given) and point total
                    if fishvalue == 1:
                        print("You caught a", fishdict['1'] + "!", "It's worth", fishvalue, "points!")
                    elif fishvalue == 2:
                        print("You caught a", fishdict['2'] + "!", "It's worth", fishvalue, "points!")
                    elif fishvalue == 5:
                        print("You caught a", fishdict['5'] + "!", "It's worth", fishvalue, "points!")
                    elif fishvalue == 10:
                        print("You caught a", fishdict['10'] + "!", "It's worth", fishvalue, "points!")
                    elif fishvalue == 25:
                        print("You caught a", fishdict['25'] + "!", "It's worth", fishvalue, "points!")
                    elif fishvalue == 60:
                        print("You caught a", fishdict['60'] + "!", "It's worth", fishvalue, "points!")
                    elif fishvalue < 0:
                        print("Oh no! You've just lost", str(fishvalue * (-1)), "points!")

                    print("Your point total is now:", str(points) + "!")

                    # testing for win lose conditionals
                    if points <= 0 and bait1 == 0 and bait2 == 0 and bait3 == 0:
                        break
                    elif points >= 150:
                        break
                    else:
                        ans1 = input(
                            "\nContinue fishing? Input <no> to leave, or press the enter button to continue fishing: ")
                        if ans1 == "no":
                            print("Entering the shop.")
                            shop()


                # fail to catch a fish
                elif 60 + globalcount < a <= 100 and conf > 0:

                    if bait == "simple":
                        bait1 -= 1
                    elif bait == "advanced":
                        bait2 -= 1
                    elif bait == "complex":
                        bait3 -= 1

                    print("""

,-.
_n_  \
(---)  `-.___________________________________________________________
~^~^~|~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^
|
|                                    
|
|
|              :c
|
|    
|    
|      
J        

""")
                    if points <= 0 and bait1 == 0 and bait2 == 0 and bait3 == 0:
                        break
                    elif points >= 150:
                        break
                    else:
                        ans = input(
                            "\nYou didn't catch a fish. Try again? Input <no> to leave, or press the enter button to continue fishing: ")
                        print("Your point total is still:", str(points) + "!")
                        if ans == "no":
                            shop()


                # not enough bait to go fishing
                else:
                    print("You don't have enough of this bait!")
                    ans = input("\nContinue?: ")
                    if ans == "no" or ans == "n":
                        shop()


            else:
                raise GameSpelling


        # spelling errors (inside game)
        except GameSpelling:
            print("\nSomething was spelled incorrectly or you typed too fast. Try again.")
            ans2 = input("Exit the fishing area? Input <yes> to leave, or press the enter button to continue fishing: ")
            if ans2 == "yes":
                shop()
            else:
                game()


# ------------------------------------------------------------------------------------------------------------------------------------------------------------


# shop function (main function)
def shop():
    # local variable definition
    rod1 = False
    rod2 = False
    rod3 = False
    global points
    global globalcount
    global bait1
    global bait2
    global bait3

    # Shop, loop until win condition or lose conditions met
    while True:

        # conditions for losing + loss screen
        if points <= 0 and bait1 == 0 and bait2 == 0 and bait3 == 0:
            print("""

                     _________         .    .
                    (..       \_    ,  |\  /|
                     \       O  \  /|  \ \/ /
                      \______    \/ |   \  /
                         vvvv\    \ |   /  |
                         \^^^^  ==   \_/   |
                          `\_   ===    \.  |
                          / /\_   \ /      |
                          |/   \_  \|      /
                                 \________/

                Oh no, you ran out of both points and bait!
                        Better luck next time!

                    Restart the program to play again!
            """)

            break

        # condition for winning + win screen
        elif points >= 150:
            print("""


                                       .
              . .                     -:-             .  .  .
            .'.:,'.        .  .  .     ' .           . \ | / .
            .'.;.`.       ._. ! ._.       \          .__\:/__.
             `,:.'         ._\!/_.                     .';`.      . ' .
             ,'             . ! .        ,.,      ..======..       .:.
            ,                 .         ._!_.     ||::: : | .        ',
     .====.,                  .           ;  .~.===: : : :|   ..===.
     |.::'||      .=====.,    ..=======.~,   |"|: :|::::::|   ||:::|=====|
  ___| :::|!__.,  |:::::|!_,   |: :: ::|"|l_l|"|:: |:;;:::|___!| ::|: : :|
 |: :|::: |:: |!__|; :: |: |===::: :: :|"||_||"| : |: :: :|: : |:: |:::::|
 |:::| _::|: :|:::|:===:|::|:::|:===F=:|"!/|\!"|::F|:====:|::_:|: :|::__:|
 !_[]![_]_!_[]![]_!_[__]![]![_]![_][I_]!//_:_\\![]I![_][_]!_[_]![]_!_[__]!
 -----------------------------------"---''''```---"-----------------------
 _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ |= _ _:_ _ =| _ _ _ _ _ _ _ _ _ _ _ _
                                     |=    :    =|                
_____________________________________L___________J________________________
--------------------------------------------------------------------------

            Congratulations on reaching 150 points!
            We hope you enjoyed playing our game!


            """)

            break

        # display the sgop
        try:
            menulist = ["1", "2", "3", "4"]

            print("""


                            (_\______/________
                               \-|-|/|-|-|-|-|/
                                \==/-|-|-|-|-/
                                 \/|-|-|-|,-'
                                  \--|-'''
                                   \_j________
                                   (_)     (_)

This is the shop! Here, you can buy yourself temporary baits and rods
to go fishing with. You can also see your point total if you want.""")

            command = input("""\nType 1 to buy 'baits', 2 to buy 'rods', or type 3 to see your
current point total. If you don't need anything for the moment,
please type 4 to start the next (or first) round of fishing: """)

            # show points
            if command == menulist[2]:
                print("\nYou currently have", points, "points.")


            # -------------------------------------------------------------------------------------------------------------------------------------------------------

            # BAITS Shop
            elif command == menulist[0]:

                # loop until exit command
                while True:
                    print("""\n\n
                                   /___\\
                                   \888/
~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~U~^~^~^~^~^~^~^
   simple bait (costs 1 point)       |
   advanced bait (costs 3 points)    |
   complex bait (costs 10 points)    |      ~
                ___        o         |
       _,.--,.'`   `~'-.._    O      |
      /_  .-"      _   /_\\'.         |   ~
     .-';'       (( `  \\0/  `\       #
    /__;          ((_  ,_     |  ,   #
    .-;                  \\_   /     _#,
   /  ;    .-' /  _.--""-.\\`/  ~`   `#(('\\        ~
   ;-';   /   / .'                  )) \\
       ; /.--'.'                   ((   ))
        \     |        ~            \\\ ((
         \    |                      )) `
   ~      \   |                      `""")

                    baitchoice = input("""\nType 'simple', 'advanced', or 'complex' to know more.
Conversely, type 'exit' to exit the baits shop: """)

                    # simple bait
                    if baitchoice == "simple":
                        print("\nYou currently have", str(bait1), "simple bait.")
                        purchasebait = input("Would you like to purchase some? (type yes or no): ")

                        # purchasing bait
                        if purchasebait == "yes":
                            simplechoice = int(input("\nInput the amount of bait to be purchased: "))

                            if simplechoice <= points and simplechoice > 0:
                                points -= simplechoice
                                bait1 += simplechoice
                                print("\nTransaction completed.")

                            else:
                                print("You either don't have enough points for that or entered an invalid input!")
                                print("Current points:", str(points) + ".")

                        # not purchasing bait
                        elif purchasebait == "no":
                            None

                        # not correct spelling
                        else:
                            print("\nInvalid input.")




                    # advanced bait
                    elif baitchoice == "advanced":
                        print("\nYou currently have", str(bait2), "advanced bait.")
                        purchasebait = input("Would you like to purchase some? (type yes or no): ")

                        # purchasing bait
                        if purchasebait == "yes":
                            advancedchoice = int(input("\nInput the amount of bait to be purchased: "))

                            if (advancedchoice * 3) <= points and advancedchoice > 0:
                                points -= (advancedchoice * 3)
                                bait2 += advancedchoice
                                print("\nTransaction completed.")

                            else:
                                print("You either don't have enough points for that or entered an invalid input!")
                                print("Current points:", str(points) + ".")

                        # not purchasing bait
                        elif purchasebait == "no":
                            None

                        # not correct spelling
                        else:
                            print("\nInvalid input.")




                    # complex bait
                    elif baitchoice == "complex":
                        print("\nYou currently have", str(bait3), "complex bait.")
                        purchasebait = input("Would you like to purchase some? (type yes or no): ")

                        # purchasing bait
                        if purchasebait == "yes":
                            complexchoice = int(input("\nInput the amount of bait to be purchased: "))

                            if (complexchoice * 10) <= points and complexchoice > 0:
                                points -= (complexchoice * 10)
                                bait3 += complexchoice
                                print("\nTransaction completed.")

                            else:
                                print("You either don't have enough points for that or entered an invalid input!")
                                print("Current points:", str(points) + ".")


                        # not purchasing bait
                        elif purchasebait == "no":
                            None

                        # not correct spelling
                        else:
                            print("\nInvalid input.")

                    # exit command
                    elif baitchoice == "exit":
                        break

                    # not correct spelling
                    else:
                        print("\nInvalid input.")

            # ------------------------------------------------------------------------------------------------------------------------------------------------------

            # RODS
            elif command == menulist[1]:

                # loop until exit command
                while True:

                    print("""

          ,-.    simple rod (5 points)
      O  /   `.       advanced rod (15 points)
      <\/      `.           complex rod (40 points)
       |*        `.
      / \          `.
     /  /            `>')3s,
--------.                 ,'
                         7
                """)

                    rodchoice = input("""Type simple, advanced, or complex to know more about each rod.
Conversely, type 'exit' to exit the rods shop: """)

                    # simple rod purchase
                    if rodchoice == "simple":
                        print("\n\nThis rod will increase the chances of catching a fish by (an additional) 5%!")
                        while rod1 == False:
                            rodtype1 = input("""\nYou currently do not have this rod.
Would you like to buy it? (type yes or no): """)

                            # buying rod
                            if rodtype1 == "yes":
                                if points >= 5:
                                    points -= 5
                                    rod1 = True
                                    print("\nYou now own this rod.")
                                    globalcount += 5
                                else:
                                    print("\nYou don't have enough points to buy this item!")
                            elif rodtype1 == "no":
                                break

                            # not correct spelling
                            else:
                                print("\nInvalid input.")

                        # already owned
                        if rod1 == True:
                            print("\nYou already own this rod!")



                    # advanced rod purchase
                    elif rodchoice == "advanced":
                        print("\n\nThis rod will increase the chances of catching a fish by (an additional) 10%!")
                        while rod2 == False:
                            rodtype2 = input("""\nYou currently do not have this rod.
Would you like to buy it? (type yes or no): """)

                            # buying rod
                            if rodtype2 == "yes":
                                if points >= 15:
                                    points -= 15
                                    rod2 = True
                                    print("\nYou now own this rod.")
                                    globalcount += 10
                                else:
                                    print("\nYou don't have enough points to buy this item!")
                            elif rodtype2 == "no":
                                break

                            # not correct spelling
                            else:
                                print("\nInvalid input.")

                        # already owned
                        if rod2 == True:
                            print("\nYou already own this rod!")




                    # complex rod purchase
                    elif rodchoice == "complex":
                        print("\n\nThis rod will increase the chances of catching a fish by (an addtional) 25%!")
                        while rod3 == False:
                            rodtype3 = input("""\nYou currently do not have this rod.
Would you like to buy it? (type yes or no): """)

                            # buying rod
                            if rodtype3 == "yes":
                                if points >= 40:
                                    points -= 40
                                    rod3 = True
                                    print("\nYou now own this rod.")
                                    globalcount += 25
                                else:
                                    print("\nYou don't have enough points to buy this item!")
                            elif rodtype3 == "no":
                                break

                            # not correct spelling
                            else:
                                print("\nInvalid input.")

                        # already owned
                        if rod3 == True:
                            print("\nYou already own this rod!")


                    # exit the rod shop
                    elif rodchoice == "exit":
                        break

                    # not correct spelling
                    else:
                        print("\nInvalid input.")


            # ------------------------------------------------------------------------------------------------------------------------------------------------------

            # start game function
            elif command == menulist[3]:
                fishdict = {'1': 'Trout', '2': 'Salmon', '5': 'Catfish', '10': 'Bluefish', '25': 'Amberjack',
                            '60': 'Blue Marlin'}

                # fish chart with values
                print("\nHere is your Fish Chart:")
                for key, val in fishdict.items():
                    print(key, "point =", val)

                game()


            # raise spelling error (outside game)
            else:
                raise Spelling

        # Spelling errors in the shop (outside game)
        except Spelling:
            print("\nSomething was spelled incorrectly or you typed too fast. Try again.")


# call on shop
shop()