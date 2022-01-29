import time
from commands import Tello


drone1 = Tello('wlp2s0'.encode())
drone2 = Tello(''.encode())
delay = 4

drone1.takeoff()
drone2.takeoff()
time.sleep(delay)

drone1.up(50)
drone2.up(50)
time.sleep(delay)

drone1.down(50)
drone2.down(50)
time.sleep(delay)

drone1.forward(50)
drone2.forward(50)
time.sleep(delay)

drone1.back(50)
drone2.back(50)
time.sleep(delay)

drone1.left(50)
drone2.left(50)
time.sleep(delay)

drone1.right(50)
drone2.right(50)
time.sleep(delay)

drone1.cw(90)
drone2.cw(90)
time.sleep(delay)

drone1.ccw(180)
drone2.ccw(180)
time.sleep(delay)

drone1.cw(90)
drone2.cw(90)
time.sleep(delay)

drone1.flip('l')
drone2.flip('l')
time.sleep(delay)

drone1.flip('r')
drone2.flip('r')
time.sleep(delay)

drone1.flip('f')
drone2.flip('f')
time.sleep(delay)

drone1.flip('b')
drone2.flip('b')
time.sleep(delay)

drone1.flip('bl')
drone2.flip('bl')
time.sleep(delay)

drone1.flip('rb')
drone2.flip('rb')
time.sleep(delay)

drone1.flip('fl')
drone2.flip('fl')
time.sleep(delay)

drone1.flip('fr')
drone2.flip('fr')
time.sleep(delay)

drone1.set_speed(10)
drone2.set_speed(10)
time.sleep(delay)

drone1.up(50)
drone2.up(50)
time.sleep(delay)

drone1.down(50)
drone2.down(50)
time.sleep(delay)

drone1.forward(50)
drone2.forward(50)
time.sleep(delay)

drone1.back(50)
drone2.back(50)
time.sleep(delay)
