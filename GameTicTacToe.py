import random
import numpy as np


class TicTacToe:
    def __init__(self, player1, player2):
        self.arr = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        self.player1 = player1
        self.player2 = player2

    def tic_tac_toe_play(self, player):
        arr1 = random.choice(self.arr)
        #ind = np.random.choice(3, size=1, replace=False)
        #arr1 = self.arr[ind, :]
        a1 = random.randint(0, len(arr1) - 1)
        if player == self.player1:
            if arr1[a1] == 0:
                arr1[a1] = 1
                return None
            else:
                for i in range(0, 3):
                    for j in range(0, 3):
                        arr1 = (self.arr[i])
                        a1 = j
                        if arr1[a1] == 0:
                            arr1[a1] = 1
                            return None
        if player == self.player2:
            if arr1[a1] == 0:
                arr1[a1] = 2
                return None
            else:
                for i in range(0, 3):
                    for j in range(0, 3):
                        arr1 = (self.arr[i])
                        a1 = j
                        if arr1[a1] == 0:
                            arr1[a1] = 2
                            return None

    def check_row(self, count, player, row):
        if player == 'player1':
            value = 1
        else:
            value = 2
        for j in range(0, len(self.arr)):
            if self.arr[row, j] == value:
                print(self.arr[row, j])
            else:
                break
            count = count + 1
        if count == 3:
            print("winner {}".format(player))
            exit()

    def check_col(self, count, player, col):
        if player == 'player1':
            value = 1
        else:
            value = 2
        for j in range(0, len(self.arr)):
            if self.arr[j, col] == value:
                print(self.arr[j, col])
            else:
                break
            count = count + 1
        if count == 3:
            print("winner {}".format(player))
            exit()

    def diagonal_right_left(self, count, player, col):
        if player == 'player1':
            value = 1
        else:
            value = 2
        for j in range(col, len(self.arr)):
            if self.arr[j, j] == value:
                print(self.arr[j, j])
            else:
                break
            count = count + 1
        if count == 3:
            print("winner {}".format(player))
            exit()

    def diagonal_left_right(self, count, player):
        if player == 'player1':
            value = 1
        else:
            value = 2
        if self.arr[2, 0] == value:
            print(self.arr[2, 0])
            count = count + 1
        if self.arr[1, 1] == value:
            print(self.arr[1, 1])
            count = count + 1
        if self.arr[0, 2] == value:
            print(self.arr[0, 2])
            count = count + 1
        if count == 3:
            print("winner {}".format(player))
            exit()

    def check_col_row_value(self, count, player):
        self.check_row(count, player, row=0)
        self.check_row(count, player, row=1)
        self.check_row(count, player, row=2)
        self.check_col(count, player, col=0)
        self.check_col(count, player, col=1)
        self.check_col(count, player, col=2)
        self.diagonal_right_left(count, player, col=0)
        self.diagonal_left_right(count, player)


a = TicTacToe('player1', 'player2')
a.tic_tac_toe_play('player1')
print(a.arr)
a.check_col_row_value(count=0, player='player1')
a.tic_tac_toe_play('player2')
print(a.arr)
a.check_col_row_value(count=0, player='player2')
a.tic_tac_toe_play('player1')
print(a.arr)
a.check_col_row_value(count=0, player='player1')
a.tic_tac_toe_play('player2')
print(a.arr)
a.check_col_row_value(count=0, player='player2')
a.tic_tac_toe_play('player1')
print(a.arr)
a.check_col_row_value(count=0, player='player1')
a.tic_tac_toe_play('player2')
print(a.arr)
a.check_col_row_value(count=0, player='player2')
a.tic_tac_toe_play('player1')
print(a.arr)
a.check_col_row_value(count=0, player='player1')
a.tic_tac_toe_play('player2')
print(a.arr)
a.check_col_row_value(count=0, player='player2')
a.tic_tac_toe_play('player1')
print(a.arr)
a.check_col_row_value(count=0, player='player1')
print("Match is draw")