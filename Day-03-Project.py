print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input('You are at a crossroad, where do you want to go?'
                ' type "left" or "right"').lower()
if choice1 == "left":
   choice2 = input('you have come to a lake. '
          'There is an island in the middle of the lake.'
          ' Type "wait" to wait for a boat.'
          ' Type "swim" to swim across.').lower()
   if choice2 == "wait":
       choice3 = input("You arrive at the island unharmed. "
                       "there is house with 3 doors.one red,"
                       "one yellow and one blue. "
                       "Which colour do you choose?").lower()
       if choice3 == "yellow":
           print("You win")
       elif choice3 == "red":
           print("Game over")
       elif choice3 == "blue":
           print("Game over")
   elif choice2 == "swim":
       print("Game over.")
elif choice1 == "right":
    print("Game over")
