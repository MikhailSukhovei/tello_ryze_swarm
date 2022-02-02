import time
from commands import Tello


drone1 = Tello('wlp2s0'.encode())
drone2 = Tello(''.encode())
drone3 = Tello(''.encode())
drone4 = Tello(''.encode())
delay = 4

drone1.takeoff()
drone2.takeoff()
drone3.takeoff()
drone4.takeoff()
time.sleep(delay)

drone1.up(50)
drone2.up(50)
drone3.up(50)
drone4.up(50)
time.sleep(delay)

drone1.down(50)
drone2.down(50)
drone3.down(50)
drone4.down(50)
time.sleep(delay)

drone1.forward(50)
drone2.forward(50)
drone3.forward(50)
drone4.forward(50)
time.sleep(delay)

drone1.back(50)
drone2.back(50)
drone3.back(50)
drone4.back(50)
time.sleep(delay)

drone1.left(50)
drone2.left(50)
drone3.left(50)
drone4.left(50)
time.sleep(delay)

drone1.right(50)
drone2.right(50)
drone3.right(50)
drone4.right(50)
time.sleep(delay)

drone1.cw(90)
drone2.cw(90)
drone3.cw(90)
drone4.cw(90)
time.sleep(delay)

drone1.ccw(180)
drone2.ccw(180)
drone3.ccw(180)
drone4.ccw(180)
time.sleep(delay)

drone1.cw(90)
drone2.cw(90)
drone3.cw(90)
drone4.cw(90)
time.sleep(delay)

drone1.flip('f')
drone2.flip('f')
drone3.flip('f')
drone4.flip('f')
time.sleep(delay)

drone1.land()
drone2.land()
drone3.land()
drone4.land()
