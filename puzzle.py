import random
from os import system

def print_grid(d):
        print('+-----+-----+-----+-----+')
        print('|%s|%s|%s|%s|' % (d[0][0], d[0][1], d[0][2], d[0][3]))
        print('+-----+-----+-----+-----+')
        print('|%s|%s|%s|%s|' % (d[1][0], d[1][1], d[1][2], d[1][3]))
        print('+-----+-----+-----+-----+')
        print('|%s|%s|%s|%s|' % (d[2][0], d[2][1], d[2][2], d[2][3]))
        print('+-----+-----+-----+-----+')
        print('|%s|%s|%s|%s|' % (d[3][0], d[3][1], d[3][2], d[3][3]))
        print('+-----+-----+-----+-----+')

def isSolvable(X):
    i,ctr = 0,0
    j=0
    for i in range(15):
        j=i
        for j in range(14-i):
            if int(X[i]) > int(X[i+j+1]):
                ctr+=1
    if ctr % 2 == 0:
        return 0
    else:
        return 1

def upSwap(x,y):
    swap = 0
    if x<1:
        print('Out of bounds')
        return x
    swap = to_solve[x-1][y]
    to_solve[x-1][y] = to_solve[x][y]
    to_solve[x][y]=swap
    print_grid(to_solve)
    return x-1

def downSwap(x,y):
    swap = 0
    if x>2:
        print('Out of bounds')
        return x
    swap = to_solve[x+1][y]
    to_solve[x+1][y] = to_solve[x][y]
    to_solve[x][y]=swap
    print_grid(to_solve)
    return x+1

def leftSwap(x,y):
    swap = 0
    if y<1:
        print('Out of bounds')
        return y
    swap = to_solve[x][y-1]
    to_solve[x][y-1] = to_solve[x][y]
    to_solve[x][y]=swap
    print_grid(to_solve)
    return y-1

def rightSwap(x,y):
    swap = 0
    if y>2:
        print('Out of bounds')
        return y
    swap = to_solve[x][y+1]
    to_solve[x][y+1] = to_solve[x][y]
    to_solve[x][y]=swap
    print_grid(to_solve)
    return y+1

def checkSolved():
    for i in range(4):
        for j in range(4):
            if to_solve[i][j].strip() != check[i][j]:
                return 0
    print("Congratulations! You have won!!")
    return 1

check = [['1','2','3','4'],['5','6','7','8'],['9','10','11','12'],['13','14','15','']]

to_shuffle = ['  1  ','  2  ','  3  ','  4  ','  5  ','  6  ','  7  ','  8  ','  9  ',' 10  ',' 11  ',' 15  ',' 13  ',' 14  ',' 12  ']
random.shuffle(to_shuffle)
sol_stat = isSolvable(to_shuffle)
to_shuffle.append('     ')

i_grid,j_grid = 3,3

to_solve = [[None for _ in range(4)] for _ in range(4)]
ctr=0
for i in range(4):
    for j in range(4):
        to_solve[i][j]=to_shuffle[ctr]
        ctr+=1

choice = None

print("So uh, we gonna play a damn game. Standard wsad to swap the space! u if unsolvable\nGo go go!\n")
print_grid(to_solve)
print(sol_stat)


while True:
    choice = input()
    system('clear')
    if choice == 'w':
        i_grid=upSwap(i_grid,j_grid)
    if choice == 's':
        i_grid=downSwap(i_grid,j_grid)
    if choice == 'a':
        j_grid=leftSwap(i_grid,j_grid)
    if choice == 'd':
        j_grid=rightSwap(i_grid,j_grid)
    if sol_stat == 1 and choice == 'u':
        print("Congratulations! You have won!!")
        input()
        exit()
    if sol_stat == 0 and choice == 'u':
        print("Nuh-huh. The game IS solvable. Try again bitch\n")
        print_grid(to_solve)
    if checkSolved()==1:
        input()
        exit()