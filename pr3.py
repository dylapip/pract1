import os
import random

if not os.path.exists("stats"):
    os.makedirs("stats")

STATS_FILE = "stats/stat.txt"

def save_result(text):
    with open(STATS_FILE, "a", encoding="utf-8") as f:
        f.write(text + "\n")


def make_board(n):
    return [[" " for _ in range(n)] for _ in range(n)]


def show(board):
    n = len(board)
    for i in range(n):
        print(" | ".join(board[i]))
        if i < n - 1:
            print("-" * (n * 4 - 3))


def win(board, p):
    n = len(board)

    for row in board:
        if all(c == p for c in row):
            return True

    for c in range(n):
        if all(board[r][c] == p for r in range(n)):
            return True

    if all(board[i][i] == p for i in range(n)):
        return True

    if all(board[i][n - i - 1] == p for i in range(n)):
        return True

    return False


def draw(board):
    return all(c != " " for r in board for c in r)


def play_game():
    while True:
        try:
            size = int(input("размер поля (>=3): "))
            if size < 3:
                print("минимум 3")
                continue
            break
        except:
            print("введите число")

    player = random.choice(["X", "O"])
    print(f"первый ходит: {player}")

    board = make_board(size)

    while True:
        show(board)
        print(f"ход игрока {player}")

        try:
            r = int(input("строка: ")) - 1
            c = int(input("столбец: ")) - 1
        except:
            print("ошибка ввода")
            continue

        if not (0 <= r < size and 0 <= c < size):
            print("координаты вне поля")
            continue
        if board[r][c] != " ":
            print("клетка занята")
            continue

        board[r][c] = player

        if win(board, player):
            show(board)
            print(f"победил {player}!")
            save_result(f"победил {player}")
            break

        if draw(board):
            show(board)
            print("ничья!")
            save_result("ничья")
            break

        player = "O" if player == "X" else "X"


def main():
    while True:
        play_game()
        again = input("новая игра? (да/нет): ").lower()
        if again != "да":
            break


main()