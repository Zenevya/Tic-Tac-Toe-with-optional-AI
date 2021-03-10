# Tic-Tac-Toe Game with an optinal AI
import random
import time
Green = "\033[0;32m"
Orange = "\033[1;33m"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"
RESET = "\033[0m"

print(BOLD + "Hi, welcome to the Tic-Tac-Toe game!", "\n" + RESET)
time.sleep(0.3)

A = [1, 2, 3]
B = [4, 5, 6]
C = [7, 8, 9]
L = [A, B, C]

def congrats_message():
  if AI_enable == "yes":
    if turn == 1:
      print("Congrats Player, you won!")
    elif turn == 2:
      print("Sorry Player, you lost. AI won.")
  elif AI_enable == "no":
    print("Congrats Player " + str(turn) + ", you won!")

def print_lists():
  print(" ".join(map(str, A)))
  print(" ".join(map(str, B)))
  print(" ".join(map(str, C)))
  print()

def cwin():
  if L[0][0] == L[0][1] and L[0][1] == L[0][2]:
    return True
  elif L[1][0] == L[1][1] and L[1][1] == L[1][2]:
    return True
  elif  L[2][0] == L[2][1] and L[2][1] == L[2][2]:
    return True
  elif L[0][0] == L[1][1] and L[1][1] == L[2][2]:
    return True
  elif L[0][2] == L[1][1] and L[1][1] == L[2][0]:
    return True
  elif  L[0][0] == L[1][0] and L[1][0] == L[2][0]:
    return True
  elif  L[0][1] == L[1][1] and L[1][1] == L[2][1]:
    return True
  elif  L[0][2] == L[1][2] and L[1][2] == L[2][2]:
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
  print("Player 1, you use", Green + "X" + RESET)
  time.sleep(0.3)
  print("Player 2, you use", Orange + "O" + RESET, "\n")
  time.sleep(0.3)

  turn = 1
  count = 0
  lstloc = [1, 2, 3, 4, 5, 6, 7, 8, 9]

  while True:
    redo_turn = True
    print_lists()
    time.sleep(0.3)
    
    if turn == 1:
      xo = "X"
    else:
      xo = "O"
    
    print(UNDERLINE + "Player",turn,"select a location to put [",xo,"]: ", end='' + RESET)
    loc = input()
    print()

    # Making sure the user's input is int type
    repeat_enable = "on"
    while repeat_enable == "on":
      try:
        int(loc)
      except ValueError:
        loc = input("Please give a number!: ")
        try:
          int(loc)
        except ValueError:
          print()
          print_lists()
        else:
          print()
        if type(loc) == int:
          repeat_enable = "off"
      else:
        loc = int(loc)
        repeat_enable = "off"

    row, col = convert(loc)

    if turn == 1:
      color = Green
    else:
      color = Orange

    if loc >9 or loc <1:
      print("Location doesn't exist! Please choose another location.", "\n")
      redo_turn = False
    elif L[row][col] == Green +"X" +RESET or L[row][col] == Orange +"O" + RESET:
      print("Sorry, somethings already there!", "\n")
      redo_turn = False
    else:
      L[row][col] = color + xo + RESET
      count = count + 1
      lstloc.remove(loc)

    # if there's only one available space
    if len(lstloc) == 1:
        print_lists()
        last_space = str(lstloc[0])
        row, col = convert(int(lstloc[0]))
        count = count + 1
        time.sleep(0.3)

        if turn == 1:
          turn = 2
        else:
          turn = 1
        L[row][col] = color + xo + RESET
        print(UNDERLINE + "Player", turn, "the only available space for",xo, "was", last_space + "!" + RESET)
        print()
    
    if cwin():
      print_lists()
      congrats_message()
      break
    elif count == 9:
      print_lists()
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

  print("Player, you're randomly chosen to play", Green + player_xo + RESET)
  time.sleep(0.3)

  print("AI will play", Orange + AI_xo + RESET, "\n")
  time.sleep(0.3)

  if player_xo == "X":
    turn = 1
  else:
    turn = 2
  count = 0

  while True:    
    redo_turn = True
    print_lists()
    time.sleep(0.3)

    # Player's turn
    if turn == 1:
      print(UNDERLINE + "Player select a location to put [",player_xo,"]: ", end='' + RESET)
      loc = input()
      print()

      # Making sure the user's input is int type
      repeat_enable = "on"
      while repeat_enable == "on":
        try:
          int(loc)
        except ValueError:
          loc = input("Please give a number!: ")
          try:
            int(loc)
          except ValueError:
            print()
            print_lists()
          else:
            print()
          if type(loc) == int:
            repeat_enable = "off"
        else:
          loc = int(loc)
          repeat_enable = "off"

      row, col = convert(loc)

      if loc >9 or loc <1:
        print("Location doesn't exist! Please choose another location.", "\n")
        redo_turn = False
      # need to write all possible color xo possibilities
      elif L[row][col] == Green+"X"+RESET or L[row][col] == Orange+"X"+RESET or L[row][col] == Green+"O"+RESET or L[row][col] == Orange+"O"+RESET:
        print("Sorry, somethings already there!", "\n")
        redo_turn = False
      else:
        L[row][col] = Green + player_xo + RESET
        count = count + 1
        lstloc.remove(loc)

      if cwin():
        print_lists()
        congrats_message()
        break
      elif count == 9:
        print_lists()
        print("Game ended in draw.")
        break

      if redo_turn == True: 
        turn = 2
      else:
        turn = 1
    
    # AI's turn
    elif turn == 2:
      found_wloc = False
      for i in range(1,10):
        row, col = convert(i)
        if L[row][col] == i:
          L[row][col] = Orange + AI_xo + RESET

          if cwin() == True:
            count = count + 1
            lstloc.remove(i)
            print("AI chose the location",i,"to put [",AI_xo,"]")
            found_wloc = True
            break
          elif cwin() != True:
            L[row][col] = Green + player_xo + RESET
            if cwin() == True:
              count = count + 1
              lstloc.remove(i)
              L[row][col] = Orange + AI_xo + RESET
              print("AI chose the location",i,"to put [",AI_xo,"]")
              print()
              found_wloc = True
              break
            else:
              L[row][col] = i
      
      if found_wloc == False:
        if count != 9:
          AIloc = random.choice(lstloc)
          row, col = convert(AIloc)
          L[row][col] = Orange + AI_xo + RESET
          count = count + 1
          lstloc.remove(AIloc)
          print("AI chose the location",AIloc,"to put [",AI_xo,"]")
          print()
      
      # if there's one available space
      if len(lstloc) == 1:
        print_lists()
        last_space = str(lstloc[0])
        row, col = convert(int(lstloc[0]))
        L[row][col] = Green + player_xo + RESET
        count = count + 1
        time.sleep(0.3)
        print(UNDERLINE + "Player the only available space", player_xo, "was", last_space + "!" + RESET)
        print()

      if cwin():
        print()
        print_lists()
        congrats_message()
        break
      elif count == 9:
        print_lists()
        print("Game ended in draw.")
        break
    
      turn = 1