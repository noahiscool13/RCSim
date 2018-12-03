from Tom import ai_fun
from challenge import Challenge

if __name__ == '__main__':
    ch = Challenge(ai_fun, fieldSize=50, maxDif=1, timeout=100)
    ch.run()
