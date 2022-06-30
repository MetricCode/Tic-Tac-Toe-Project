import random
import time
from sys import stdout

def write(text):

    for i in text:
        #yes i can use print(), but there's a problem, print() creates a new line every print.
        stdout.write(i)
        stdout.flush()
        time.sleep(.086)


def table():
  row1=["","",""]
  row2=["","",""]
  row3=["","",""]
  print(row1)
  print(row2)
  print(row3)


write("\nWelcome to my python Tic Tac Toe Game")
time.sleep(2)
write("\nBelow is your tic tac toe board\n")
time.sleep(2)

table()

time.sleep(3)
write("\nIn this game you will always be X\n")



def game1():
  list=[1,2,3,4,5,6,7,8,9]
  player=[]
  comp=[]
  n=0
  win1 = [1,2,3]
  win2 = [1,3,2]
  win3 = [2,3,1]
  win4 = [2,1,3]
  win5 = [3,1,2]
  win6 = [3,2,1]


  win7 = [4,5,6]
  win8 = [4,6,5]
  win9 = [5,6,4]
  win10= [5,4,6]
  win11= [6,5,4]
  win12= [6,4,5]


  win13= [7,8,9]
  win14= [7,9,8]
  win15= [8,9,7]
  win16= [8,7,9]
  win17= [9,7,8]
  win18= [9,8,7]


  win19 = [1,4,7]
  win20 = [1,7,4]
  win21 = [4,1,7]
  win22 = [4,7,1] 
  win23 = [7,1,4]
  win24 = [7,4,1]


  win25 = [2,5,8]
  win26 = [2,8,5] 
  win27 = [5,8,2]
  win28 = [5,2,8]
  win29 = [8,2,5]
  win30 = [8,5,2] 


  win31 = [3,6,9]
  win32 = [3,9,6] 
  win33 = [6,9,3]
  win34 = [6,3,9]
  win35 = [9,3,6]
  win36 = [9,6,3]


  win37 = [1,5,9]
  win38 = [1,9,5]
  win39 = [5,9,1]
  win40 = [5,1,9] 
  win41 = [9,1,5]
  win42 = [9,5,1]


  win43 = [3,5,7]
  win44 = [3,7,5] 
  win45 = [5,7,3] 
  win46 = [5,3,7] 
  win47 = [7,3,5] 
  win48 = [7,5,3]





  # The display table 
  t1 = ["_","_","_"]
  t2 = ["_","_","_"]
  t3 = ["_","_","_"]

  # End of the display table


  while n < 3:
    time.sleep(1)

    # Time for the player to make his move
    # Time for the player to make his move
    player_play1=int(input("Choose your position:"))
    list.remove(player_play1)
    player.append(player_play1)
    print("Your current trend",player)
    time.sleep(1)
    if player_play1 ==1 :
      t1[0]="X"
      print(t1)
      print(t2)
      print(t3)
    elif player_play1 ==2:
      t1[1]="X"
      print(t1)
      print(t2)
      print(t3)
    elif player_play1 ==3:
      t1[-1]="X"
      print(t1)
      print(t2)
      print(t3)
    elif player_play1 ==4:
      t2[0]="X"
      print(t1)
      print(t2)
      print(t3)
    elif player_play1 ==5:
      t2[1]="X"
      print(t1)
      print(t2)
      print(t3)
    elif player_play1 ==6:
      t2[-1]="X"
      print(t1)
      print(t2)
      print(t3)
    elif player_play1 ==7:
      t3[0]="X"
      print(t1)
      print(t2)
      print(t3)
    elif player_play1 ==8:
      t3[1]="X"
      print(t1)
      print(t2)
      print(t3)
    elif player_play1 ==9:
      t3[-1]="X"
      print(t1)
      print(t2)
      print(t3)
    else:
      write("\nEnter a number from 1-9")





     # Time for the computer to make its move
    print("Computer's turn ")
    time.sleep(2)
    comp_play1 = random.choice(list)
    list.remove(comp_play1)
    comp.append(comp_play1)
    time.sleep(2)
    print(comp_play1)
    time.sleep(1)
    print("Computer's current trend",comp)
    time.sleep(2)



    if comp_play1 ==1 :
      t1[0]="Y"
      print(t1)
      print(t2)
      print(t3)
    elif comp_play1 ==2:
      t1[1]="Y"
      print(t1)
      print(t2)
      print(t3)
    elif comp_play1 ==3:
      t1[-1]="Y"
      print(t1)
      print(t2)
      print(t3)
    elif comp_play1 ==4:
      t2[0]="Y"
      print(t1)
      print(t2)
      print(t3)
    elif comp_play1 ==5:
      t2[1]="Y"
      print(t1)
      print(t2)
      print(t3)
    elif comp_play1 ==6:
      t2[-1]="Y"
      print(t1)
      print(t2)
      print(t3)
    elif comp_play1 ==7:
      t3[0]="Y"
      print(t1)
      print(t2)
      print(t3)
    elif comp_play1 ==8:
      t3[1]="Y"
      print(t1)
      print(t2)
      print(t3)
    elif comp_play1 ==9:
      t3[-1]="Y"
      print(t1)
      print(t2)
      print(t3)
    else:
      write("\nEnter a number from 1-9")

    print("Choices are : ",list)
    n +=1
    # Check if some values are equal

  time.sleep(3)
  write("\nfinal round")
  time.sleep(2)
  write("\nChecking...\n")
  time.sleep(2)
  
  time.sleep(2)
  if player == win1 or player == win2 or player == win3 or player == win4 or player == win5 or player == win6 or player == win7 or player == win8:
    print(" player wins")

  elif player == win9 or player == win10 or player == win11 or player == win12 or player == win13 or player == win14 or player == win15 or player == win16:
    print("player wins")

  elif player == win17 or player == win18 or player == win19 or player == win20 or player == win21 or player == win22 or player == win23 or player == win24:
    print("player wins")

  elif player == win25 or player == win26 or player == win27 or player == win28 or player == win29 or player == win30 or player == win31 or player == win32:
    print("player wins")

  elif player == win33 or player == win34 or player == win35 or player == win36 or player == win37 or player == win38 or player == win39 or player == win40:
    print("player wins")

  elif player == win41 or player == win42 or player == win43 or player == win44 or player == win45 or player == win46 or player == win47 or player == win48:
    print("player wins")

  elif comp == win1 or comp == win2 or comp == win3 or comp == win4 or comp == win5 or comp == win6 or comp == win7 or comp == win8:
    print(" Computer wins")

  elif comp == win9 or comp == win10 or comp == win11 or comp == win12 or comp == win13 or comp == win14 or comp == win15 or comp == win16:
    print("Computer wins")

  elif comp == win17 or comp == win18 or comp == win19 or comp == win20 or comp == win21 or comp == win22 or comp == win23 or comp == win24:
    print("Computer wins")

  elif comp == win25 or comp == win26 or comp == win27 or comp == win28 or comp == win29 or comp == win30 or comp == win31 or comp == win32:
    print("Computer wins")

  elif comp == win33 or comp == win34 or comp == win35 or comp == win36 or comp == win37 or comp == win38 or comp == win39 or comp == win40:
    print("Computer wins")

  elif comp == win41 or comp == win42 or comp == win43 or comp == win44 or comp == win45 or comp == win46 or comp == win47 or comp == win48:
    print("Computer wins")  
  else:
    write("\nGame Draw! Nice Game")

game1()



