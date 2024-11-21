def check_winner():
    print("")


def draw_area():
    for i in area:
        print(*i)
    print()


area = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]
print("Добро пожаловать в крестики-нолики")
print("-----------------------")
draw_area()
for turn in range(1, 10):
    print(f"Ход: {turn}")
    if turn % 2 == 0:
        turn_char = "0"
        print("Ходят нолики")
    else:
        turn_char = "X"
        print("Ходят крестики")
    row = int(input("Введите номер строки (1, 2, 3) ")) - 1
    column = int(input("Введите номер столбца (1, 2, 3) ")) - 1
    if area[row][column] == "*":
        area[row][column] = turn_char
    else:
        print("Ячейка уже занята, вы пропускаете ход")
        continue
    draw_area()

    if check_winner() == "X":
        print("Победа крестиков")
        break
    if check_winner() == "X":
        print("Победа ноликов")
        break
    if check_winner() == "*" and turn == 9:
        print("Ничья")
