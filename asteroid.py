import math

class Asteroid:

    def __init__(self, x, vx, y, vy, size):
        self.x = x
        self.vx = vx
        self.y = y
        self.vy = vy
        self.size = size

    def get_x(self):
        return self.x

    def get_vx(self):
        return self.vx

    def get_y(self):
        return self.y

    def get_vy(self):
        return self.vy

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.size*10 - 5

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def draw_asteroid(self, screen):
        screen.draw_asteroid(self, self.x, self.y)

    def has_intersection(self, obj):
        '''
        This function checks whether the asteroid hits another object. it can be a ship or a torpedo
        :param obj: a ship or torpedo
        :return: True or False
        '''
        distance = math.sqrt(math.pow(obj.get_x() - self.x,2) + math.pow(obj.get_y() - self.y,2))
        return distance <= self.get_radius() + obj.get_radius()

    def register_asteroid(self, screen, size):
        screen.register_asteroid(self, size)

    def unregister_asteroid(self,screen):
        screen.unregister_asteroid(self)

