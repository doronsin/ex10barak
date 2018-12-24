import math


class Asteroid:
    """
    This class represents an asteroid
    """

    ASTEROID_RADIUS_NORMALIZER = -5
    ASTEROID_RADIUS_FACTOR = 10

    def __init__(self, x, vx, y, vy, size):
        """
        c-tor of the class
        :param x: x
        :param vx: the speed on x-axis
        :param y: y
        :param vy: the speed on y-axis
        :param size: the size of the asteroid (number from 1 to 3)
        """
        self.x = x
        self.vx = vx
        self.y = y
        self.vy = vy
        self.size = size

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
        :return: vy
        """
        return self.vy

    def get_size(self):
        """
        getter for the size of the asteroid
        :return:
        """
        return self.size

    def get_radius(self):
        """
        returns the radius of the asteroid which is determined by its size
        :return: the radius of the asteroid
        """
        return self.size * Asteroid.ASTEROID_RADIUS_FACTOR + Asteroid.ASTEROID_RADIUS_NORMALIZER

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

    def draw_asteroid(self, screen):
        """
        draws the asteroid on the screen "screen"
        :param screen: the screen which the asteroid should be drawn on
        :return:
        """
        screen.draw_asteroid(self, self.x, self.y)

    def has_intersection(self, obj):
        """
        This function checks whether the asteroid hits another object. it can be a ship or a torpedo
        :param obj: a ship or torpedo
        :return: True if there is intersection, or False otherwise
        """
        distance = math.sqrt(math.pow(obj.get_x() - self.x, 2) + math.pow(obj.get_y() - self.y, 2))
        return distance <= self.get_radius() + obj.get_radius()

    def register_asteroid(self, screen):
        """
        registers the asteroid for a given screen
        :param screen: the screen which the asteroid should be registered to
        """
        screen.register_asteroid(self, self.size)

    def unregister_asteroid(self, screen):
        """
        unregister the asteroid from a given screen
        :param screen: the screen which the asteroid should be unregistered from
        """
        screen.unregister_asteroid(self)
