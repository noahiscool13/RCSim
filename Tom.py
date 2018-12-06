from math import *
n = 0


def ai_fun(pos, spd, dir, goal, cur):
    global n

    # n = 0




    if (dir % (2 * pi) < - 0.1 or dir % (2 * pi) > 0.1) and pos[0] < goal[cur][0]:
        print("goal is right of me")
        if dir % (2 * pi) > pi:
            return[0.2,-1]
        else:
            return[0.2,1]

    if (dir % (2 * pi) < ((1.5 * pi) - 0.1) or dir % (2 * pi) > ((1.5 * pi) + 0.1)) and pos[1] > goal[cur][1]:
        print("its below me")
        if dir % (2 * pi) > (1.5 * pi):
            return [0.2, 1]
        else:
            return [0.2, -1]

    if (dir % (2 * pi) < ((0.5 * pi) - 0.1) or dir % (2 * pi) > ((0.5 * pi) + 0.1)) and pos[1] < goal[cur][1]:
        print("its above me")
        if dir % (2 * pi) > (0.5 * pi):
            return [0.2, 1]
        else:
            return [0.2, -1]


    if (dir % (2 * pi) < (pi - 0.1) or dir % (2 * pi) > (pi + 0.1)) and pos[0] > goal[cur][0]:
        print("its left of me")
        if dir % (2 * pi) > pi:
            return[0.2,1]
        else:
            return[0.2,-1]















