class Ship:
    """
    This class represents a Ship object
    """
    RADIUS = 1
    LIFE = 3

    def __init__(self, x, vx, y, vy, deg):
        """
        c-tor of the class
        :param x: x
        :param vx: speed in the x-axis
        :param y: y
        :param vy: speed in the y-axis
        :param deg: direction of the ship in degrees
        """
        self.__x = x
        self.__vx = vx
        self.__y = y
        self.__vy = vy
        self.__deg = deg
        self.__life = self.LIFE

    def get_x(self):
        """
        getter for x
        :return: x
        """
        return self.__x

    def get_vx(self):
        """
        getter for vx
        :return: vx
        """
        return self.__vx

    def get_y(self):
        """
        getter for y
        :return: y
        """
        return self.__y

    def get_vy(self):
        """
        getter for vy
        :return: y
        """
        return self.__vy

    def get_deg(self):
        """
        getter for deg
        :return: deg
        """
        return self.__deg

    def get_radius(self):
        """
        returns the radius of the ship, which is constant
        :return:
        """
        return Ship.RADIUS

    def get_life(self):
        """
        returns the number of lives remained to the ship
        :return:
        """
        return self.__life

    def set_deg(self, deg):
        """
        setter for deg
        :param deg: the new deg
        """
        self.__deg = deg

    def set_x(self, x):
        """
        setter for x
        :param x: the new x
        """
        self.__x = x

    def set_y(self, y):
        """
        setter for y
        :param y: the new y
        """
        self.__y = y

    def set_life(self, n):
        """
        setter for the life
        :param n: the new number of lives
        """
        self.__life = n

    def draw_ship(self, screen):
        """
        draws the ship on the screen "screen"
        :param screen: the screen which the ship should be drawn on
        """
        screen.draw_ship(self.__x, self.__y, self.__deg)

    def set_vx(self, new_speed_x):
        """
        setter for vx
        :param new_speed_x: the new vx
        """
        self.__vx = new_speed_x

    def set_vy(self, new_speed_y):
        """
        setter for vy
        :param new_speed_y: the new vy
        :return:
        """
        self.__vy = new_speed_y
