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

drone.flip('l')
time.sleep(delay)

drone.flip('r')
time.sleep(delay)

drone.flip('f')
time.sleep(delay)

drone.flip('b')
time.sleep(delay)

drone.flip('bl')
time.sleep(delay)

drone.flip('rb')
time.sleep(delay)

drone.flip('fl')
time.sleep(delay)

drone.flip('fr')
time.sleep(delay)

drone.set_speed(10)
time.sleep(delay)

drone.up(50)
time.sleep(delay)

drone.down(50)
time.sleep(delay)

drone.forward(50)
time.sleep(delay)

drone.back(50)
time.sleep(delay)
