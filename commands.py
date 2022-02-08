import socket
import time
import re


def clamp(n, smallest, largest):
    return max(smallest, min(n, largest))


class Tello:

    def __init__(self, interface):
        self.interface = interface
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setsockopt(socket.SOL_SOCKET, 25, self.interface)
        self.tello_address = ('192.168.10.1', 8889)

        self.buf_size = 1024
        self.resend_delay = 0.1
        self.timeout = 4

    def send_message(self, message):
        start_time = time.time()
        while True:
            self.sock.sendto(message.encode(), 0, self.tello_address)
            print(self.interface, 'send', message)
            data = self.sock.recv(self.buf_size)
            response = data.decode(encoding='utf-8', errors='ignore')
            print(self.interface, 'get', response)

            if response == 'ok':
                print(self.interface, 'status', 'OK')
                break
            elif time.time() - start_time > self.timeout:
                print(self.interface, 'status', 'TIMEOUT')
                break
            elif re.match('error', response):
                print(self.interface, 'status', 'ERROR')
                continue
            else:
                print(self.interface, 'status', 'UNRECOGNIZED')

            time.sleep(self.resend_delay)

    def send_command(self, command):
        self.send_message('command')
        self.send_message(command)

    def takeoff(self):
        """
        Auto takeoff
        """
        self.send_command('takeoff')

    def land(self):
        """
        Auto landing
        """
        self.send_command('land')

    def up(self, xx):
        """
        Tello fly upward with distance

        :param xx: distance (20-500 cm)
        """
        xx = clamp(int(xx), 20, 500)
        self.send_command(' '.join(['up', str(xx)]))

    def down(self, xx):
        """
        Tello fly downward with distance

        :param xx: distance (20-500 cm)
        """
        xx = clamp(int(xx), 20, 500)
        self.send_command(' '.join(['down', str(xx)]))

    def left(self, xx):
        """
        Tello fly left with distance

        :param xx: distance (20-500 cm)
        """
        xx = clamp(int(xx), 20, 500)
        self.send_command(' '.join(['left', str(xx)]))

    def right(self, xx):
        """
        Tello fly right with distance

        :param xx: distance (20-500 cm)
        """
        xx = clamp(int(xx), 20, 500)
        self.send_command(' '.join(['right', str(xx)]))

    def forward(self, xx):
        """
        Tello fly forward with distance

        :param xx: distance (20-500 cm)
        """
        xx = clamp(int(xx), 20, 500)
        self.send_command(' '.join(['forward', str(xx)]))

    def back(self, xx):
        """
        Tello fly backward with distance

        :param xx: distance (20-500 cm)
        """
        xx = clamp(int(xx), 20, 500)
        self.send_command(' '.join(['back', str(xx)]))

    def cw(self, xx):
        """
        Tello rotate clockwise

        :param xx: angle (1-360 deg)
        """
        xx = clamp(int(xx), 1, 360)
        self.send_command(' '.join(['cw', str(xx)]))

    def ccw(self, xx):
        """
        Tello rotate counter-clockwise

        :param xx: angle (1-360 deg)
        """
        xx = clamp(int(xx), 1, 360)
        self.send_command(' '.join(['ccw', str(xx)]))

    def flip(self, xx):
        """
        Tello flip

        :param xx: direction l = (left), r = (right), f = (forward), b = (back),
            bl = (back/left), rb = (back/right), fl = (front/left), fr = (front/right)
        """
        if xx in ['l', 'r', 'f', 'b', 'bl', 'rb', 'fl', 'fr']:
            self.send_command(' '.join(['flip', xx]))

    def set_speed(self, xx):
        """
        Set current speed

        :param xx: speed (1-100 cm/s)
        """
        xx = clamp(int(xx), 1, 100)
        self.sock.sendto('command'.encode(), 0, self.tello_address)
        self.sock.sendto(' '.join(['speed', str(xx)]).encode(), 0, self.tello_address)

    def read_speed(self):
        """
        Get current speed

        :return: xx = speed (cm/s)
        """
        self.sock.sendto('command'.encode(), 0, self.tello_address)
        self.sock.sendto('Speed?'.encode(), 0, self.tello_address)

        # ToDo

        return 0

    def read_battery(self):
        """
        Get current battery percentage

        :return: xx = battery percentage (0 - 100%)
        """
        self.sock.sendto('command'.encode(), 0, self.tello_address)
        self.sock.sendto('Battery?'.encode(), 0, self.tello_address)

        # ToDo

        return 0

    def read_time(self):
        """
        Get current flight time

        :return: xx = flight time (sec)
        """
        self.sock.sendto('command'.encode(), 0, self.tello_address)
        self.sock.sendto('Time?'.encode(), 0, self.tello_address)

        # ToDo

        return 0
