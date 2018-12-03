from vector import Vector
from math import *

from matplotlib import pyplot as plt

DT = 0.1


class BasicCar:

    def __init__(self, pos=Vector(), direction=0, speed=0, steer=0):
        self.topSpeed = 7  # Top speed straight path in m/s
        self.turnTopSpeed = 4       # Top speed while max turning in m/s
        self.acceleration = 5       # Acceleration in m/s**2
        self.slowCorner = 1.5       # Circle diameter at slow speed in m
        self.cornerPenalty = 2.1    # Extra diameter at max speed in m
        self.cornerGradient = 0.5   # Slowdown in corners in parts of max speed
        self.weelRotateTime = 0.2   # Time to turn the steering in s
        self.friction = 2           # Friction in m/s**2

        self.pos = pos
        self.direction = direction
        self.speed = speed
        self.steer = steer

    def sim(self, dt, power, steer_goal):

        assert -1 <= power <= 1
        assert -1 <= steer_goal <= 1

        # Update speed

        self.speed -= self.friction * dt * self.speed

        self.speed += power * (self.acceleration + self.friction) * dt
        if self.speed > self.topSpeed - self.topSpeed * self.cornerGradient * abs(self.steer):
            self.speed = self.topSpeed - self.topSpeed * self.cornerGradient * abs(self.steer)
        elif self.speed < 0:
            self.speed = 0

        # Update steering
        if self.steer < steer_goal:
            self.steer = min(self.steer + dt / self.weelRotateTime, steer_goal)
        else:
            self.steer = max(self.steer - dt / self.weelRotateTime, steer_goal)

        # Update direction
        cornerSize = self.slowCorner + (self.speed/(self.topSpeed - self.topSpeed * self.cornerGradient * abs(self.steer))) * self.cornerPenalty


        circleSize = pi * cornerSize



        turn = self.speed * dt / circleSize * 2 * pi
        self.direction += self.steer * turn

        # Update possition
        self.pos += Vector(self.speed * dt, 0).rotate(self.direction)
        #print(self.direction)

if __name__ == '__main__':
    car = BasicCar(speed=0)

    l = []
    s = []
    st = []
    for x in range(200):
        # print(car.pos)
        l.append(car.pos)
        s.append(car.speed)
        st.append(sin(x/500))
        car.sim(DT, x/200, 1-x/100)

    plt.plot(*list(zip(*l)))

    plt.show()

    plt.plot(s)

    #plt.show()

    plt.plot(st)

    plt.show()
