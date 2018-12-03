from basic_car import *
from vector import Vector
from matplotlib import pyplot as plt
from random import *

n = 1

class Challenge:

    def __init__(self, AIfunc, level=0, amount=1, plot=True, maxDif = 0.5, dt = 0.05, timeout = 200, fieldSize=50):
        self.AIfunc = AIfunc
        self.level = level
        self.amount = amount
        self.plot = plot
        self.maxDif = maxDif
        self.dt = dt
        self.timeout = timeout
        self.fieldSize = fieldSize

    def run(self):
        score = []
        for x in range(self.amount):
            start = Vector(self.fieldSize * random(), self.fieldSize * random())
            if self.level == 0:
                goal = [Vector(self.fieldSize * random(), self.fieldSize * random())]
            direction = 2 * pi * random()
            speed = 6 * random()
            test_car = BasicCar(start, direction, speed)
            path = []
            if self.level == 0:
                time = 0
                while (test_car.pos-goal[0]).norm() > self.maxDif:
                    time += self.dt
                    test_car.sim(self.dt,*self.AIfunc(test_car.pos,test_car.speed,test_car.direction,goal,0))
                    path.append(test_car.pos)
                    if time > self.timeout:
                        break
                else:
                    print("SUCCES!")

            plt.plot(*list(zip(*path)))
            plt.plot(*goal[0],"ro")

            plt.show()

