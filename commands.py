import socket


def clamp(n, smallest, largest):
    return max(smallest, min(n, largest))


class Tello:

    def __init__(self, interface):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setsockopt(socket.SOL_SOCKET, 25, interface)
        self.tello_address = ('192.168.10.1', 8889)

    def takeoff(self):
        """
        Auto takeoff
        """
        self.sock.sendto('command'.encode(), 0, self.tello_address)
        self.sock.sendto('takeoff'.encode(), 0, self.tello_address)

    def land(self):
        """
        Auto landing
        """
        self.sock.sendto('command'.encode(), 0, self.tello_address)
        self.sock.sendto('land'.encode(), 0, self.tello_address)

    def up(self, xx):
        """
        Tello fly upward with distance

        :param xx: distance (20-500 cm)
        """
        xx = clamp(int(xx), 20, 500)
        self.sock.sendto('command'.encode(), 0, self.tello_address)
        self.sock.sendto(' '.join(['up', str(xx)]).encode(), 0, self.tello_address)

    def down(self, xx):
        """
        Tello fly downward with distance

        :param xx: distance (20-500 cm)
        """
        xx = clamp(int(xx), 20, 500)
        self.sock.sendto('command'.encode(), 0, self.tello_address)
        self.sock.sendto(' '.join(['down', str(xx)]).encode(), 0, self.tello_address)

    def left(self, xx):
        """
        Tello fly left with distance

        :param xx: distance (20-500 cm)
        """
        xx = clamp(int(xx), 20, 500)
        self.sock.sendto('command'.encode(), 0, self.tello_address)
        self.sock.sendto(' '.join(['left', str(xx)]).encode(), 0, self.tello_address)

    def right(self, xx):
        """
        Tello fly right with distance

        :param xx: distance (20-500 cm)
        """
        xx = clamp(int(xx), 20, 500)
        self.sock.sendto('command'.encode(), 0, self.tello_address)
        self.sock.sendto(' '.join(['right', str(xx)]).encode(), 0, self.tello_address)

    def forward(self, xx):
        """
        Tello fly forward with distance

        :param xx: distance (20-500 cm)
        """
        xx = clamp(int(xx), 20, 500)
        self.sock.sendto('command'.encode(), 0, self.tello_address)
        self.sock.sendto(' '.join(['forward', str(xx)]).encode(), 0, self.tello_address)

    def back(self, xx):
        """
        Tello fly backward with distance

        :param xx: distance (20-500 cm)
        """
        xx = clamp(int(xx), 20, 500)
        self.sock.sendto('command'.encode(), 0, self.tello_address)
        self.sock.sendto(' '.join(['back', str(xx)]).encode(), 0, self.tello_address)

    def cw(self, xx):
        """
        Tello rotate clockwise

        :param xx: angle (1-360 deg)
        """
        xx = clamp(int(xx), 1, 360)
        self.sock.sendto('command'.encode(), 0, self.tello_address)
        self.sock.sendto(' '.join(['cw', str(xx)]).encode(), 0, self.tello_address)

    def ccw(self, xx):
        """
        Tello rotate counter-clockwise

        :param xx: angle (1-360 deg)
        """
        xx = clamp(int(xx), 1, 360)
        self.sock.sendto('command'.encode(), 0, self.tello_address)
        self.sock.sendto(' '.join(['ccw', str(xx)]).encode(), 0, self.tello_address)

    def flip(self, xx):
        """
        Tello flip

        :param xx: direction l = (left), r = (right), f = (forward), b = (back),
            bl = (back/left), rb = (back/right), fl = (front/left), fr = (front/right)
        """
        if xx in ['l', 'r', 'f', 'b', 'bl', 'rb', 'fl', 'fr']:
            self.sock.sendto('command'.encode(), 0, self.tello_address)
            self.sock.sendto(' '.join(['flip', xx]).encode(), 0, self.tello_address)

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
