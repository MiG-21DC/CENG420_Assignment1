def get_init_chess():
    return {1: 1, 2: 1, 3: 1, 4: 0, 5: 0, 6: 0, 7: -1, 8: -1, 9: -1}

def heuristic_judge(white):
    heuristic_counter = 0
    win_situation = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for judge in win_situation:
        heuristic_difference = set(white).difference(judge)
        heuristic_difference = list(heuristic_difference)
        heuristic_difference_len = len(heuristic_difference)
        # heuristic_difference = heuristic_difference[0]

        if heuristic_difference_len == 0:
            return 'DO IT'
        else:
            heuristic_counter = heuristic_counter + heuristic_difference_len

    return heuristic_counter

def heruistic(chess=get_init_chess()):

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
    print '**********************'
    print white
    print black
    print empty
    res = 99

    # win_situation = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]

    for orgpos in white:
        for movepos in empty:
            print white
            print orgpos
            print movepos
            newwhite = []
            newwhite.extend(white)
            newempty = []
            newempty.extend(empty)
            try:
                newwhite.remove(orgpos)
            except Exception,e:
                print white, newwhite, orgpos
                continue
            newwhite.append(movepos)
            newwhite.sort()
            newempty.remove(movepos)
            newempty.append(orgpos)
            newempty.sort()
            newres = heuristic_judge(newwhite)
            if isinstance(res,str):
                for i in range(1, 10):
                    if i in newwhite:
                        newchess[i] = 1
                    if i in newempty:
                        newchess[i] = 0
                    if i in black:
                        newchess[i] = -1
                return newchess
            if res > newres:
                suggestwhite = newwhite
                suggestempty = newempty
                res = newres
            else:
                continue

    for i in range(1, 10):
        if i in suggestwhite:
            newchess[i] = 1
        if i in suggestempty:
            newchess[i] = 0
        if i in black:
            newchess[i] = -1
    return newchess

def main():
    chess = {1:1,2:-1,3:1,4:0,5:1,6:0,7:-1,8:-0,9:-1}
    newchess = heruistic(chess)
    print newchess


if __name__ == '__main__':
    main()