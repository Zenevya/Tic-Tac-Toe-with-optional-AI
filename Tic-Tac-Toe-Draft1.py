#Tic-Tac-Toe Game with an optinal AI
import random
import time
print("Hi, welcome to the Tic-Tac-Toe game!", "\n")
time.sleep(0.5)

A = [1, 2, 3]
B = [4, 5, 6]
C = [7, 8, 9]
L = [A, B, C]

def print_lists():
  print(A)
  print(B)
  print(C, "\n")
  print()

def cwin():
  if AI_enable == "yes":
    if turn == 1:
      congrats_message = "Congrats Player, you won!"
    elif turn == 2:
      congrats_message = "Sorry Player, you lost. AI won."
  elif AI_enable == "no":
    congrats_message = "Congrats Player " + str(turn) + ", you won!"

  if L[0][0] == L[0][1] and L[0][1] == L[0][2]:
    print_lists()
    print(congrats_message)
    return True
  elif L[1][0] == L[1][1] and L[1][1] == L[1][2]:
    print_lists()
    print(congrats_message)
    return True
  elif  L[2][0] == L[2][1] and L[2][1] == L[2][2]:
    print_lists()
    print(congrats_message)
    return True
  elif L[0][0] == L[1][1] and L[1][1] == L[2][2]:
    print_lists()
    print(congrats_message)
    return True
  elif L[0][2] == L[1][1] and L[1][1] == L[2][0]:
    print_lists()
    print(congrats_message)
    return True
  elif  L[0][0] == L[1][0] and L[1][0] == L[2][0]:
    print_lists()
    print(congrats_message)
    return True
  elif  L[0][1] == L[1][1] and L[1][1] == L[2][1]:
    print_lists()
    print(congrats_message)
    return True
  elif  L[0][2] == L[1][2] and L[1][2] == L[2][2]:
    print_lists()
    print(congrats_message)
    return True

def convert(loc):
  row = (loc-1)//3
  col = loc - (row*3) - 1
  return row, col
  # assert(convert(9) == (2, 2))
  # assert(convert(0) == (0, 0))
  # assert(convert(5) == (1, 1))

AI_enable = input("Would you like to play against an AI? (yes/no): ")
print()

# Playing against player 2
if AI_enable == "no":
  print("Player 1, you use X")
  time.sleep(0.3)
  print("Player 2, you use O", "\n")
  time.sleep(0.5)

  turn = 1
  count = 0

  while True:
    redo_turn = True
    print_lists()
    time.sleep(0.3)
    
    if turn == 1:
      xo = "X"
    else:
      xo = "O"
    
    print("Player",turn,"select a location to put [",xo,"]: ", end='')
    loc = int(input())
    print()
    row, col = convert(loc)

    if loc >9 or loc <1:
      print("Location doesn't exist! Please choose another location.", "\n")
      redo_turn = False
    elif L[row][col] == "X" or L[row][col] == "O":
      print("Sorry, somethings already there!", "\n")
      redo_turn = False
    else:
      L[row][col] = xo
      count = count + 1
    
    if cwin():
      break
    elif count == 9:
      print("Game ended in draw.")
      break

    if redo_turn == True: 
      # Flip turns unless the player messed it up
      if turn == 1:
        turn = 2
      else:
        turn = 1

# Playing against AI
elif AI_enable == "yes":
  lstxo = ["X", "O"]
  lstloc = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  player_xo = random.choice(lstxo)

  if player_xo == "X":
    AI_xo = "O"
  else:
    AI_xo = "X"

  print("Player, you're randomly chosen to play", player_xo)
  time.sleep(0.3)
  print("AI will play", AI_xo, "\n")
  time.sleep(0.5)

  if player_xo == "X":
    turn = 1
  else:
    turn = 2
  count = 0

  while True:    
    redo_turn = True
    print_lists()
    time.sleep(0.3)

    # Player starts
    if turn == 1:
      print("Player select a location to put [",player_xo,"]: ", end='')
      loc = int(input())
      print()
      row, col = convert(loc)

      if loc >9 or loc <1:
        print("Location doesn't exist! Please choose another location.", "\n")
        redo_turn = False
      elif L[row][col] == "X" or L[row][col] == "O":
        print("Sorry, somethings already there!", "\n")
        redo_turn = False
      else:
        L[row][col] = player_xo
        count = count + 1
        lstloc.remove(loc)

      if cwin():
        break
      elif count == 9:
        print("Game ended in draw.")
        break

      if redo_turn == True: 
        turn = 2
      else:
        turn = 1
    
    # AI starts
    elif turn == 2:
      AIloc = random.choice(lstloc)
      print("AI chose the location",AIloc,"to put [",AI_xo,"]")
      print()

      row, col = convert(AIloc)
      L[row][col] = AI_xo
      count = count + 1
      lstloc.remove(AIloc)

      if cwin():
        break
      elif count == 9:
        print("Game ended in draw.")
        break
    
      turn = 1
