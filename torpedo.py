class Torpedo:
    """
    This class represents a torpedo object
    """
    RADIUS = 4

    def __init__(self, x, vx, y, vy, deg):
        """
        c-tor of the class
        :param x: x
        :param vx: speed on x-axis
        :param y: y
        :param vy: speed on y-axis
        :param deg: the direction of the torpedo in degrees
        """
        self.x = x
        self.vx = vx
        self.y = y
        self.vy = vy
        self.deg = deg
        self.life = 0  # This is a counter of rounds. After 200 rounds the torpedo will be unregistered

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

    def get_deg(self):
        """
        getter for deg
        :return: deg
        """
        return self.deg

    def get_radius(self):
        """
        returns the radius of a torpedo, which is constant
        :return: the radius of a torpedo
        """
        return self.RADIUS

    def get_torpedo_life(self):
        """
        getter for the number of lives (=rounds) of the torpedo
        :return: the number of rounds that the torpedo is "alive"
        """
        return self.life

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

    def set_life(self, life):
        """
        setter for life
        :param life: the new number of lives
        """
        self.life = life

    def draw_torpedo(self, screen):
        """
        draws the torpedo on the screen "screen"
        :param screen: the screen which the torpedo should be drawn on
        """
        screen.draw_torpedo(self, self.x, self.y, self.deg)

    def register_torpedo(self, screen):
        """
        registers the torpedo for a given screen
        :param screen: the screen which the torpedo should be registered to
        """
        screen.register_torpedo(self)

    def unregister_torpedo(self, screen):
        """
        unregister the torpedo from a given screen
        :param screen: the screen which the torpedo should be unregistered from
        """
        screen.unregister_torpedo(self)
