n = 1

def ai_fun(pos, spd, dir, goal, cur):
    global n

    n -= 0.0002

    return [0.2, max(n, 0)]