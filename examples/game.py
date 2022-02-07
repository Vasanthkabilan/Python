print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
choice1 = input(
    'You\'re at a crossroad. Where do you want to go? Type "left" or "right"')
lowercase_choice1 = choice1.lower()
if lowercase_choice1 == "left":
    choice2 = input(
      'You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.'
    )
    lowercase_choice2 = choice2.lower()
    if lowercase_choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?"
        )
        lowercase_choice3 = choice3.lower()
        if lowercase_choice3 == "red":
            print('''
              ,.   (   .      )        .      "
          ("     )  )'     ,'        )  . (`     '`
        .; )  ' (( (" )    ;(,     ((  (  ;)  "  )"
        _"., ,._'_.,)_(..,( . )_  _' )_') (. _..( '..
          "It's a room full of fire. Game Over."
      ''')
        elif lowercase_choice3 == "yellow":
            print('''
                 ___ ___  _ __   __ _ _ __ __ _| |_ ___ 
                / __/ _ \| '_ \ / _` | '__/ _` | __/ __|
                | (_| (_) | | | | (_| | | | (_| | |_\__ 
                \___\___/|_| |_|\__, |_|  \__,_|\__|___/
                                __/ |                  
                                |___/                   

      ''')
        elif lowercase_choice3 == "blue":
            print('''
                  (    )
                      ((((()))
                      |o\ /o)|
                      ( (  _')
                      (._.  /\__
                      ,\___,/ '  ')
        '.,_,,       (  .- .   .    )
        \   \\     ( '        )(    )
          \   \\    \.  _.__ ____( .  |
          \  /\\   .(   .'  /\  '.  )
            \(  \\.-' ( /    \/    \)
            '  ()) _'.-|/\/\/\/\/\|
                '\\ .( |\/\/\/\/\/|
                  '((  \    /\    /
                  ((((  '.__\/__.')
                    ((,) /   ((()   )
                    "..-,  (()("   /
                pils  _//.   ((() ."
              _____ //,/" ___ ((( ', ___
                              ((  )
                                / /
                              _/,/'
                            /,/,"
      "You enter a room of beasts. Game Over." 
      ''')
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print('''

            .-''-.__.-'00  '-' ' ' ' ' ' ' ' '-.
         '.___ '    .   .--_'-' '-' '-' _'-' '._
          V: V 'vv-'   '_   '.       .'  _..' '.'.
            '=.____.=_.--'   :_.__.__:_   '.   : :
                    (((____.-'        '-.  /   : :
                                       (((-'\ .' /
                                    _____..'  .'
                                   '-._____.-'


      "You get attacked by an angry trout. Game Over."
      ''')
else:
    print("You fell into a hole. Game Over.")
