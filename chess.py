import time
import sys


def get_init_chess():
    return {1: 1, 2: 1, 3: 1, 4: 0, 5: 0, 6: 0, 7: -1, 8: -1, 9: -1}

def move_chess(chess, orgpos, newpos):
    if chess[newpos] != 0:
        return 'Error, the target position is not empty'
    color = chess[orgpos]
    if color == 0:
        return 'Error, the original position is empty'
    chess[orgpos] = 0
    chess[newpos] = color
    return chess
class heuristic:
    def __int__(self):
        self.properchess = []
        self.chessrecord = []

    def heuristic(self,chess,level,count=0):
        white = []
        black = []
        empty = []

        for pos, color in chess:
            if color == 1:
                white.append(pos)
            elif color == -1:
                black.append(pos)
            else:
                empty.append(pos)
        white.sort()
        black.sort()
        empty.sort()
        win_situation = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]
        if white in win_situation:
            return chess, '1'
        elif black in win_situation:
            return chess, '-1'
        if level == 0:
            return chess
        else:
            level = level - 1
            count = count + 1
        if count % 2 == 1:
            for pos in white:
                for targetpos in empty:
                    self.chessrecord.append(chess)
                    res = move_chess(chess,pos,targetpos)
                    if isinstance(res,dict):
                        newchess, heuristic_res = heuristic(res, level, count)
                        if heuristic_res == '1':
                            self.properchess.append(chess)
                            return
                    else:
                        continue



def main():
    init_chess = get_init_chess()
    moveset = input('please input "F" if you want to move first or input "S" if you want computer to move first')
    inputcheck = True
    while inputcheck:
        if moveset == 'F' or moveset == 'f':
            movecase = -1
            inputcheck = False
        elif moveset == 'S' or moveset == 's':
            movecase = 1
            inputcheck = False
        else:
            moveset = input(
                'Wrong input commend! please input "F" if you want to move first or input "S" if you want computer to move first')

    heuristic_level = input('please input heuristic level of computer (maximum 3)')
    heuristic_level = int(heuristic_level)


if __name__ == '__main__':
    main()