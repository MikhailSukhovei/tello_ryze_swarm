import time
from commands import Tello


drone = Tello('wlp2s0'.encode())
delay = 4

drone.takeoff()
time.sleep(delay)

drone.up(50)
time.sleep(delay)

drone.down(50)
time.sleep(delay)

drone.forward(50)
time.sleep(delay)

drone.back(50)
time.sleep(delay)

drone.left(50)
time.sleep(delay)

drone.right(50)
time.sleep(delay)

drone.cw(90)
time.sleep(delay)

drone.ccw(180)
time.sleep(delay)

drone.cw(90)
time.sleep(delay)

drone.flip('f')
time.sleep(delay)

drone.land()
