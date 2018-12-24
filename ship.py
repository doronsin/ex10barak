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
        self.x = x
        self.vx = vx
        self.y = y
        self.vy = vy
        self.deg = deg
        self.life = self.LIFE

    def get_x(self):
        """
        getter for x
        :return: x
        """
        return self.x

    def get_vx(self):
        """
        getter for vx
        :return: vx
        """
        return self.vx

    def get_y(self):
        """
        getter for y
        :return: y
        """
        return self.y

    def get_vy(self):
        """
        getter for vy
        :return: y
        """
        return self.vy

    def get_deg(self):
        """
        getter for deg
        :return: deg
        """
        return self.deg

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
        return self.life

    def set_deg(self, deg):
        """
        setter for deg
        :param deg: the new deg
        """
        self.deg = deg

    def set_x(self, x):
        """
        setter for x
        :param x: the new x
        """
        self.x = x

    def set_y(self, y):
        """
        setter for y
        :param y: the new y
        """
        self.y = y

    def set_life(self, n):
        """
        setter for the life
        :param n: the new number of lives
        """
        self.life = n

    def draw_ship(self, screen):
        """
        draws the ship on the screen "screen"
        :param screen: the screen which the ship should be drawn on
        """
        screen.draw_ship(self.x, self.y, self.deg)

    def set_vx(self, new_speed_x):
        """
        setter for vx
        :param new_speed_x: the new vx
        """
        self.vx = new_speed_x

    def set_vy(self, new_speed_y):
        """
        setter for vy
        :param new_speed_y: the new vy
        :return:
        """
        self.vy = new_speed_y
