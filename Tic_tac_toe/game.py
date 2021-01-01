import random

cells = "_________"
cells = cells.replace('_',' ')
cells = list(cells)

#create matrix 3*3
table = [[cells[j + 3 * i] for j in range(3)] for i in range(3)]

table_t = [[cells[3 * j + i] for j in range(3)] for i in range(3)]


def matrix_output(table):
    print('---------')
    for i in range(len(table)):
        print('|', end=' ')
        for j in range(len(table[i])):
            print(table[i][j], end=' ')
        print('|')
    return '---------'

print(matrix_output(table))

def check_input(f, s, table):
    if not f.isdigit() or not s.isdigit():
        print("You should enter numbers!")
        check = False
        return check
    else:
        if int(f) > 3 or int(s) > 3:
            print("Coordinates should be from 1 to 3!")
            check = False
            return check
        elif table[int(f) - 1][int(s) - 1] != " ":
            print("This cell is occupied! Choose another one!")
            check = False
            return check
        else:
            check = True
            return check

def cell_occupied(f, l):
    if table[f][l] == " ":
        return False
    else:
        return True

def computer_move():
    cu_move1 = random.randint(0, 2)
    cu_move2 = random.randint(0, 2)

    if cell_occupied(cu_move1, cu_move2):
        computer_move()
    else:
        table[cu_move1][cu_move2] = "O"

def sum_check():
    sum_X = 0
    sum_O = 0

    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] == "X":
                sum_X += 1
            elif table[i][j] == "O":
                sum_O += 1
    if sum_X > sum_O:
        return True
    else:
        return False

def full():
    count = 0
    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] == " ":
                count +=1

    if count > 0:
        return False
    else:
        return True

def check_winner(table_t):
    if full():
        print("Draw")
    else:
        if table[0] == ["X", "X", "X"]:
            return "X wins"
        elif table[1] == ["X", "X", "X"]:
            return "X wins"
        elif table[2] == ["X", "X", "X"]:
            return "X wins"
        elif table[0] == ["O", "O", "O"]:
            return "O wins"
        elif table[1] == ["O", "O", "O"]:
            return "O wins"
        elif table[2] == ["O", "O", "O"]:
            return "O wins"
        elif table_t[0] == ["X", "X", "X"]:
            return "X wins"
        elif table_t[1] == ["X", "X", "X"]:
            return "X wins"
        elif table_t[2] == ["X", "X", "X"]:
            return "X wins"
        elif table_t[0] == ["O", "O", "O"]:
            return "O wins"
        elif table_t[1] == ["O", "O", "O"]:
            return "O wins"
        elif table_t[2] == ["O", "O", "O"]:
            return "O wins"
        elif table[0][0] == "X" and table[1][1] == "X" and table[2][2] == "X":
            return "X wins"
        elif table[0][2] == "X" and table[1][1] == "X" and table[2][0] == "X":
            return "X wins"
        elif table[0][0] == "O" and table[1][1] == "O" and table[2][2] == "O":
            return "O wins"
        elif table[0][2] == "O" and table[1][1] == "O" and table[2][0] == "O":
            return "O wins"
        else:
            return 1



def menu():
    global first, second
    count = 0
    check = False
    sum_ch = False

    while True:
        if sum_check():
            computer_move()
            print('Making move level "easy"')
            print(matrix_output(table))
            # table[int(first) - 1][int(second) - 1] = "O"
        else:
            try:
                print("Enter the coordinates: ", end="")
                first,second = input().split()
            except:
                print("You should enter numbers! ")
            else:
                check = check_input(first, second, table)
            if check:
                table[int(first) - 1][int(second) - 1] = "X"
                print(matrix_output(table))
            else:
                menu()
        table_t = [list(i) for i in zip(*table)]
        winner = check_winner(table_t)
        if winner != 1:
            print(winner)
            break
        else:
            menu()
        break
    return

menu()