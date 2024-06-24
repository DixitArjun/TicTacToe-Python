Board=[' 0 ',' 1 ',' 2 ',' 3 ',' 4 ',' 5 ',' 6 ',' 7 ',' 8 ']
x=5
def Get_input():
    while x==5:
        PA1=int(input("Enter the position:"))
        RealGame(PA1,' X ')
        PA1=int(input("Enter the position:"))
        RealGame(PA1,' O ')
        PA1=int(input("Enter the position:"))
        RealGame(PA1,' X ')
        PA1=int(input("Enter the position:"))
        RealGame(PA1,' O ')
        PA1=int(input("Enter the position:"))
        RealGame(PA1,' X ')
        if Board[0]==Board[3]==Board[6]==' X 'or Board[0]==Board[1]==Board[2]==' X 'or Board[0]==Board[4]==Board[8]==' X 'or Board[1]==Board[4]==Board[7]==' X 'or Board[2]==Board[5]==Board[8]==' X 'or Board[2]==Board[4]==Board[6]==' X 'or Board[3]==Board[4]==Board[5]==' X 'or Board[6]==Board[7]==Board[8]==' X ':
            print("Player1 Wins")
            start_over()
            break
        elif Board[0]==Board[3]==Board[6]==' O 'or Board[0]==Board[1]==Board[2]==' O 'or Board[0]==Board[4]==Board[8]==' O 'or Board[1]==Board[4]==Board[7]==' O 'or Board[2]==Board[5]==Board[8]==' O 'or Board[2]==Board[4]==Board[6]==' O 'or Board[3]==Board[4]==Board[5]==' O 'or Board[6]==Board[7]==Board[8]==' O ':
            print("Player2 Wins")
            start_over()
            break

        else:
            PA1=int(input("Enter the position:"))
            RealGame(PA1,' O ')
            if Board[0]==Board[3]==Board[6]==' X 'or Board[0]==Board[1]==Board[2]==' X 'or Board[0]==Board[4]==Board[8]==' X 'or Board[1]==Board[4]==Board[7]==' X 'or Board[2]==Board[5]==Board[8]==' X 'or Board[2]==Board[4]==Board[6]==' X 'or Board[3]==Board[4]==Board[5]==' X 'or Board[6]==Board[7]==Board[8]==' X ':
                print("Player1 Wins")
                start_over()
                break
            elif Board[0]==Board[3]==Board[6]==' O 'or Board[0]==Board[1]==Board[2]==' O 'or Board[0]==Board[4]==Board[8]==' O 'or Board[1]==Board[4]==Board[7]==' O 'or Board[2]==Board[5]==Board[8]==' O 'or Board[2]==Board[4]==Board[6]==' O 'or Board[3]==Board[4]==Board[5]==' O 'or Board[6]==Board[7]==Board[8]==' O ':
                print("Player2 Wins")
                start_over()
                break
            else:
                PA1=int(input("Enter the position:"))
                RealGame(PA1,' X ')
                if Board[0]==Board[3]==Board[6]==' X 'or Board[0]==Board[1]==Board[2]==' X 'or Board[0]==Board[4]==Board[8]==' X 'or Board[1]==Board[4]==Board[7]==' X 'or Board[2]==Board[5]==Board[8]==' X 'or Board[2]==Board[4]==Board[6]==' X 'or Board[3]==Board[4]==Board[5]==' X 'or Board[6]==Board[7]==Board[8]==' X ':
                    print("Player1 Wins")
                    start_over()
                    break
                elif Board[0]==Board[3]==Board[6]==' O 'or Board[0]==Board[1]==Board[2]==' O 'or Board[0]==Board[4]==Board[8]==' O 'or Board[1]==Board[4]==Board[7]==' O 'or Board[2]==Board[5]==Board[8]==' O 'or Board[2]==Board[4]==Board[6]==' O 'or Board[3]==Board[4]==Board[5]==' O 'or Board[6]==Board[7]==Board[8]==' O ':
                    print("Player2 Wins")
                    start_over()
                    break
                else:
                    PA1=int(input("Enter the position:"))
                    RealGame(PA1,' O ')
                    if Board[0]==Board[3]==Board[6]==' X 'or Board[0]==Board[1]==Board[2]==' X 'or Board[0]==Board[4]==Board[8]==' X 'or Board[1]==Board[4]==Board[7]==' X 'or Board[2]==Board[5]==Board[8]==' X 'or Board[2]==Board[4]==Board[6]==' X 'or Board[3]==Board[4]==Board[5]==' X 'or Board[6]==Board[7]==Board[8]==' X ':
                        print("Player1 Wins")
                        start_over()
                        break
                    elif Board[0]==Board[3]==Board[6]==' O 'or Board[0]==Board[1]==Board[2]==' O 'or Board[0]==Board[4]==Board[8]==' O 'or Board[1]==Board[4]==Board[7]==' O 'or Board[2]==Board[5]==Board[8]==' O 'or Board[2]==Board[4]==Board[6]==' O 'or Board[3]==Board[4]==Board[5]==' O 'or Board[6]==Board[7]==Board[8]==' O ':
                        print("Player2 Wins")
                        start_over()
                        break
                    else:
                        PA1=int(input("Enter the position:"))
                        RealGame(PA1,' X ')
                        print("Tie")
                        start_over()
    

def RealGame(C,K):
    Board[C]=K
    print('   |','   |')
    print(Board[0]+'|',Board[1]+'|',Board[2])
    print('   |','   |')
    print(' ------------')
    print('   |','   |')
    print(Board[3]+'|',Board[4]+'|',Board[5])
    print('   |','   |')
    print(' ------------')
    print('   |','   |')
    print(Board[6]+'|',Board[7]+'|',Board[8])
    print('   |','   |')

def ClearBoard():
    Board=[' 0 ',' 1 ',' 2 ',' 3 ',' 4 ',' 5 ',' 6 ',' 7 ',' 8 ']

def start_over():
    UserInp=input("Do you want to continue playing(Y or N):")
    UserI=UserInp.upper()
    if UserI=='Y':
        start_game()
    elif UserI=='N':
        print("Thank You")
    else:
        print("Inavlid Input! Try again.")
        start_over()

def start_game():
    GameInpu=input("Do you want to start the game(Y or N)?")
    GameIn=GameInpu.upper()
    if GameIn=='Y':
        global Board
        Board=[' 0 ',' 1 ',' 2 ',' 3 ',' 4 ',' 5 ',' 6 ',' 7 ',' 8 ']
        print('   |','   |')
        print(Board[0]+'|',Board[1]+'|',Board[2])
        print('   |','   |')
        print(' ------------')
        print('   |','   |')
        print(Board[3]+'|',Board[4]+'|',Board[5])
        print('   |','   |')
        print(' ------------')
        print('   |','   |')
        print(Board[6]+'|',Board[7]+'|',Board[8])
        print('   |','   |')
        print("***Player1 plays First***")
        Get_input()
    elif GameIn=='N':
        print("Thank You")
    else:
        print("Inavlid Input! Try again.")
        start_game()
