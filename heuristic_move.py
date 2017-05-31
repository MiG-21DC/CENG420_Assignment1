"""
CENG 420 Assignment 1 Question 1.4

**********************************************
Group UNKNOWN
Andres Aburto   V00778603
Kunyu Zhang     V00784674
Xiang Xu        V00768356
Yangguang Liu   V00782918
**********************************************

****************************************************IMPORTANT****************************************************
This program is writen under Python 2.7, please make sure you have suitable Python version installed.

This program do the heuristic approach to realize a computer which is able to play sega game with players.

In this program, 9 blocks is named as 1 to 9, e.g.
1   2   3
4   5   6
7   8   9

The white chess is represented by 1, the black chess is represented by -1, and the empty space is represented as 0.
Thus the initial state of the chess is:
1   1   1
0   0   0
-1  -1  -1

There are nine goal states for white chess to win the game: three vertical lines, three horizontal lines and two
diagonal lines. Thus, the goal states of white chess represented by block coordinates are [1,2,3], [4,5,6], [7,8,9],
[1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7].

There are 2 steps of heuristic level that can be chosen. If only realize first heuristic level, the program will only
calculate the best movement of white chess. The heuristic algorithm is that there are 3 white chess and 3 empty space,
so there should be 3 x 3 = 9 possible movement for white chess. For each possible movement, the difference between
white chess and each goal states h(n) will be compared. The difference will be summed for all 8 goal states for one
movement as there final h(n). The movement with lowest h(n) is considered to be the best movement for white chess. If a
movement can result the white chess to meet the goal states, the program will stop immediately and output the winning
movement.

However the first heuristic level will not consider the movement of black chess. To implement a better heuristic search
AI, a second level of heuristic calculation can be chosen. This allows program to predict the next step of black chess.
Once the next black chess movement is able to reach the goal or has the best heuristic search approaching (the lowest
h(n) for black chess) to the goals, the program will take another movement for the first white chess. 

"""


#   Print chess in square format
def print_chess(chess):
    for key in chess:
        value = chess[key]
        if key % 3 != 0:
            print str(value)+'\t',
        else:
            print str(value)
    return


#   Set initial states
def get_init_chess():
    return {1: 1, 2: 1, 3: 1, 4: 0, 5: 0, 6: 0, 7: -1, 8: -1, 9: -1}


#   Do heuristic search on potential movement and calculated its h(n) for white or black chess
def heuristic_judge(white):
    heuristic_counter = 0   # The sum of h(n)
    win_situation = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for judge in win_situation:
        heuristic_difference = set(white).difference(judge)
        heuristic_difference = list(heuristic_difference)
        heuristic_difference_len = len(heuristic_difference)    # The difference of movement and each goal statements

        if heuristic_difference_len == 0:
            return 'DO IT'
        else:
            heuristic_counter = heuristic_counter + heuristic_difference_len

    return heuristic_counter


#   The second level of heuristic search which consider the potential movement of black chess
def heuristic_black(white, empty, black):
    white.sort()
    black.sort()
    empty.sort()
    
    for orgpos in black:
        for movepos in empty:
            newblack = []
            newblack.extend(black)
            newempty = []
            newempty.extend(empty)
            try:
                newblack.remove(orgpos)
            except Exception,e:
                print white, newblack, orgpos
                continue
            newblack.append(movepos)
            newblack.sort()
            newempty.remove(movepos)
            newempty.append(orgpos)
            newempty.sort()
            newres = heuristic_judge(newblack)
            if isinstance(newres, str):
                return 'DONT DO IT'
            else:
                continue

    return 0
    

#   Go through all possible movements of white or black chess and call for the heuristic algorithm
def heuristic(chess=get_init_chess(), level=2):

    white = []
    black = []
    empty = []
    newchess = {}
    for pos in chess:
        color = chess[pos]
        if color == 1:
            white.append(pos)
        elif color == -1:
            black.append(pos)
        else:
            empty.append(pos)

    white.sort()
    black.sort()
    empty.sort()
    res = 99

    for orgpos in white:
        for movepos in empty:
            newwhite = []
            newwhite.extend(white)
            newempty = []
            newempty.extend(empty)
            try:
                newwhite.remove(orgpos)
            except Exception, e:
                print white, newwhite, orgpos
                print Exception, e
                continue
            newwhite.append(movepos)
            newwhite.sort()
            newempty.remove(movepos)
            newempty.append(orgpos)
            newempty.sort()
            newres = heuristic_judge(newwhite)
            if isinstance(newres, str):
                for i in range(1, 10):
                    if i in newwhite:
                        newchess[i] = 1
                    if i in newempty:
                        newchess[i] = 0
                    if i in black:
                        newchess[i] = -1
                return newchess, 'win'
            if res > newres:
                if level == 1:
                    suggestempty = []
                    suggestwhite = []
                    suggestwhite.extend(newwhite)
                    suggestempty.extend(newempty)
                    res = newres
                elif level == 2:
                    blackres = heuristic_black(newwhite, newempty, black)
                    if blackres == 'DONT DO IT':
                        continue
                    else:
                        suggestempty = []
                        suggestwhite = []
                        suggestwhite.extend(newwhite)
                        suggestempty.extend(newempty)
                        res = newres
            else:
                continue

    if suggestempty == [] or suggestwhite == []:
        return chess, 'lose'
    for i in range(1, 10):
        if i in suggestwhite:
            newchess[i] = 1
        if i in suggestempty:
            newchess[i] = 0
        if i in black:
            newchess[i] = -1
    return newchess, 'continue'


def main():
    # chess = {1:1,2:-1,3:1,4:0,5:1,6:0,7:-1,8:0,9:-1}
    chess = get_init_chess()
    end_flag = True
    level = input('Please enter a heuristic level (1 or 2)')
    try:
        level = int(level)
    except:
        level = 100

    while level != 1 and level != 2:
        level = input('Wrong commend. Please enter a heuristic level (1 or 2)')
        try:
            level = int(level)
        except:
            level = 100
    # level = int(level)
    win_situation = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    while end_flag:
        newchess, flag = heuristic(chess, level)
        print_chess(newchess)
        chess = newchess
        if flag == 'win':
            print 'You Lose'
            end_flag = False
            continue
        # elif flag == 'lose':
        #     # print 'You Win'
        #     # end_flag = False
        #     continue
        orgposition = input('Please input the original coordinate of black chess (1 - 9)')
        try:
            orgposition = int(orgposition)
        except:
            orgposition = 100
        while chess[orgposition] != -1:
            orgposition = input('Wrong commend. Please input the original coordinate of black chess (1 - 9)')
            try:
                orgposition = int(orgposition)
            except:
                orgposition = 100
                
        moveposition = input('Please input the coordinate of black chess you want to move to (1 - 9)')
        try:
            moveposition = int(moveposition)
        except:
            moveposition = 100
        while chess[moveposition] != 0:
            moveposition = input('Wrong commend. Please input the coordinate of black chess you want to move to (1 - 9)')
            try:
                moveposition = int(moveposition)
            except:
                moveposition = 100

        chess[orgposition] = 0
        chess[moveposition] = -1

        white = []
        black = []
        empty = []
        for pos in chess:
            color = chess[pos]
            if color == 1:
                white.append(pos)
            elif color == -1:
                black.append(pos)
            else:
                empty.append(pos)

        white.sort()
        black.sort()
        empty.sort()

        if black in win_situation:
            print_chess(newchess)
            print 'You Win'
            end_flag = False

if __name__ == '__main__':
    main()