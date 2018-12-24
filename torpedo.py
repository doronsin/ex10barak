

class Torpedo:
    RADIUS = 4

    def __init__(self, x, vx, y, vy, deg):
        self.x = x
        self.vx = vx
        self.y = y
        self.vy = vy
        self.deg = deg
        self.life = 0 # This is a counter of rounds. After 200 rounds the torpedo will be unregistered

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

    def get_torpedo_life(self):
        return self.life

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def set_life(self, life):
        self.life = life

    def draw_torpedo(self, screen):
        screen.draw_torpedo(self, self.x, self.y, self.deg)

    def register_torpedo(self, screen):
        screen.register_torpedo(self)

    def unregister_torpedo(self, screen):
        screen.unregister_torpedo(self)
