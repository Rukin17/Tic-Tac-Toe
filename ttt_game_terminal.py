from random import randint, random

mas = [['_'] * 4 for i in range(4)]
mas[0][0] = ' '
abc_list = ['a', 'b', 'c']
x_o = ['X', 'O']

for col in range(1, 4):
    mas[col][0] = col

for row in range(1, 4):
    mas[0][row] = abc_list[row - 1]

for i in mas:
    print(' ' * 10, *i)

def move_comp(col: int, row: int, xo: str):
    mas[col][abc_list[row]] = xo

while True:
    first_move = x_o[randint(0, 1)]
    rand_move = randint(0, 1)
    if rand_move == 1:
        move = input(f'Ваш ход! Вы играете {first_move} Введите координаты клетки(Пример: b1): ')
        mas[int(move[1])][abc_list.index(move[0]) + 1] = first_move
        for i in mas:
            print(' ' * 10, *i)
    else:
        col = randint(1, 3)
        row = randint(1, 4)