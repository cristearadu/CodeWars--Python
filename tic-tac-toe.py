#https://www.codewars.com/kata/tic-tac-toe-checker/train/python
def isSolved(board):
    def winner(bo,nb):
        if (bo[0][0] == nb and bo[0][1] == nb and bo[0][2] == nb) or (bo[1][0] == nb and bo[1][1] == nb and bo[1][2] == nb) or (bo[2][0] == nb and bo[2][1] == nb and bo[2][2] == nb):
            return True
        elif (bo[0][0] == nb and bo[1][1] == nb and bo[2][2] == nb) or (bo[0][2] == nb and bo[1][1] == nb and bo[2][0] == nb):
            return True
        elif (bo[0][0] == nb and bo[1][0] == nb and bo[2][0] == nb) or (bo[0][1] == nb and bo[1][1] == nb and bo[2][1] == nb) or (bo[0][2] == nb and bo[1][2] == nb and bo[2][2] == nb):
            return True
        else:
            return False
    def empty_B(board):
        empty = False
        for line in board:
            for i in line:
                if i == 0:
                    empty = True
        return empty
    
    if (winner(board,1)):
        return 1
    elif (winner(board,2)):
        return 2
    elif (empty_B(board)):
        return -1
    else:
        return 0
    
print(isSolved([[0, 0, 1],
         [0, 1, 2],
         [2, 1, 0]]))#False


