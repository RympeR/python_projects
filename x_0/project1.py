import os
import random
# import time


def print_desk():
    os.system("cls")
    global desk
    print(desk['1'], '|', desk['2'], '|', desk['3'])
    print('- - - - -')
    print(desk['4'], '|', desk['5'], '|', desk['6'])
    print('- - - - -')
    print(desk['7'], '|', desk['8'], '|', desk['9'])


def enemy_turn(mark, level=1):
    turn_over = False
    warning = False
    almost_win = False
    global desk
    global combos
    counter = 0
    mark_combo = ['', '', '']
    index = [0, 0, 0]
    while not turn_over:

        if level != 1:
            turn = random.randint(0, 8)
            for combo in combos:
                for count in combo:
                    mark_combo[counter] = desk[count]
                    index[counter] = int(count)
                    counter += 1

                if mark_combo.count(' ') == 1 and mark_combo.count(mark) == 2:
                    almost_win = True

                elif mark_combo.count(' ') == 1 and mark_combo.count(mark) == 0:
                    warning = True

                counter = 0

                if almost_win or warning:
                    try:
                        turn = index[mark_combo.index(' ')]
                    except Exception as e:
                        break
                    desk[str(turn)] = mark
                    turn_over = True
                    warning = False
                    almost_win = False

                if turn_over:

                    break
            else:
                while True:
                    turn = random.randint(0, 8)
                    if desk[list(desk.keys())[turn]] == ' ':
                        turn_over = True
                        desk[list(desk.keys())[turn]] = mark
                        print_desk()
                        print('here')
                        break
                    else:
                        continue

        else:
            turn = random.randint(0, 8)
            if desk[list(desk.keys())[turn]] == ' ':
                desk[list(desk.keys())[turn]] = mark
                turn_over = True
            else:
                continue


def game():
    enemy_marks = str()
    marks = ['x', '0']
    turns = 0
    global desk
    global combos
    input('Input mark [x,0]: ')
    your_mark = 'x'
    if your_mark == 'x':
        enemy_marks = '0'
    else:
        enemy_marks = 'x'

    while not check(turns, marks):
        turns += 1
        # if desk['1'] == 'x' and desk['2'] == '0' and desk['3'] == 'x' and desk['6'] == '0' and desk['8'] == 'x' and desk['9'] == '0':
        #     os.sys.exit()
        #     os.system("python3 project1.py")

        # enemy_turn('x', 2)
        # check(turns, marks)
        # print_desk()
        # turns += 1
        # enemy_turn('0', 2)
        # print_desk()
        # check(turns, marks)

        place = input("Input free place 1-9: ")
        while desk[place] != ' ':
            place = input("Input free place 1-9: ")
        if your_mark == 'x':
            desk[place] = your_mark
            # enemy_turn(your_mark,2)
            check(turns, marks)
            print_desk()
            turns += 1
            enemy_turn('0',2)
            check(turns, marks)
            print_desk()
        else:
            # desk[place] = your_mark
            enemy_turn('x',2)

            check(turns, marks)
            print_desk()
            turns += 1
            desk[place] = your_mark
            # enemy_turn(your_mark,2)

            check(turns, marks)

            print_desk()


def check(turns, marks):
    with open("stat.txt", 'a') as f:
        global x_win
        global y_win
        global desk
        global combos
        counter = 0
        draw_cond = False
        for combo in combos:
                for count in combo:
                    if (desk[count] != ' ' and desk[count] == marks[(turns) % 2]) or (desk[count] != ' ' and desk[count] == marks[(turns+1) % 2]):
                        counter += 1
                    else:
                        continue

                if counter == 3:
                    f.write(f"{marks[(turns) % 2]} wins!!")
                    f.write('\n')
                    print(f"{marks[(turns) % 2]} wins!!")
                    if marks[(turns) % 2] == 'x':
                        x_win += 1
                    else:
                        y_win += 1
                    # time.sleep(3)
                    os.system("cls")
                    # os.sys.exit()
                    return True
                else:
                    counter = 0
        for k in desk.values():
            if k != ' ':
                counter += 1
        if counter == 9:
            draw_cond = True

        if draw_cond:
            # os.system("clear")
            print("DRAW")
            # time.sleep(3)
            f.write("DRAW")
            f.write('\n')
            # f.write(print_desk())
            # os.sys.exit()
            os.system("cls")
            return True
        return False


desk = {'1': ' ', '2': ' ', '3': ' ',
        '4': ' ', '5': ' ', '6': ' ',
        '7': ' ', '8': ' ', '9': ' '}
combos = ['123', '456', '789',
          '147', '258', '369',
          '159','357']
x_win = 0
y_win = 0
if __name__ == "__main__":
    # game()
    for i in range(10000):
        game()
        for i in range(1, 9):
            desk[str(i)] = ' '
        print_desk()
    with open('stat.txt', 'a') as f:
        f.write('-------------------')
        f.write('\n')
        f.write('y')
        f.write('\n')
        f.write(y_win)
        f.write('\n')
        f.write('x')
        f.write('\n')
        f.write(x_win)
        f.write('\n')