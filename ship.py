

class Ship:
    RADIUS = 1
    LIFE = 3

    def __init__(self, x, vx, y, vy, deg):

        self.x = x
        self.vx = vx
        self.y = y
        self.vy = vy
        self.deg = deg
        self.life = self.LIFE


    def get_x(self):
        return self.x

    def get_vx(self):
        return self.vx

    def get_y(self):
        return self.y

    def get_vy(self):
        return self.vy

    def get_deg(self):
        return self.deg

    def get_radius(self):
        return self.RADIUS

    def get_life(self):
        return self.life

    def set_deg(self, i):
        self.deg = i

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def set_life(self, n):
        self.life += n

    def draw_ship(self, screen):
        screen.draw_ship(self.x, self.y, self.deg)

    def set_vx(self, new_speed_x):
        self.vx = new_speed_x

    def set_vy(self, new_speed_y):
        self.vy = new_speed_y





