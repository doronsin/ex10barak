from screen import Screen
import sys
import random
import math
# this names is for preventing shadowing of those imports in the next functions
import ship as sh
import asteroid as ast
import torpedo as tor

DEFAULT_ASTEROIDS_NUM = 5
DEG_TO_RAD_COEFFICIENT = 0.0174532925


class GameRunner:
    """
    This class responsible of running the game of asteroids and ships
    """
    ASTEROID_STARTING_SIZE = 3
    SCORE_DICT = {3: 20, 2: 50, 1: 100}  # keys: size of asteroid destroyed, values: the score "reward"
    BLOW_ASTEROID_DICT = {3: 2, 2: 1, 1: 0}  # keys: size of current asteroid, values: the size of the new asteroids
    NUMBER_OF_ASTEROIDS_AFTER_TORPEDO_HIT = 2
    TORPEDO_LIFE = 200
    MAX_TORPEDO = 10

    def __init__(self, asteroids_amount=DEFAULT_ASTEROIDS_NUM):
        """
        c-tor of the GameRunner class
        :param asteroids_amount: the number of asteroids in the game
        """
        self.__screen = Screen()
        self.__screen_max_x = Screen.SCREEN_MAX_X
        self.__screen_max_y = Screen.SCREEN_MAX_Y
        self.__screen_min_x = Screen.SCREEN_MIN_X
        self.__screen_min_y = Screen.SCREEN_MIN_Y
        self.__asteroids = []
        self.__torpedos = []
        self.__score = 0

        # place the ship on the screen in a random location
        self.__ship = self.create_ship()

        # Here we are creating the asteroids
        self.create_asteroids(asteroids_amount)

    def create_ship(self):
        ship_xy_location = self.random_location_xy()
        ship = sh.Ship(ship_xy_location[0], 0, ship_xy_location[1], 0, 0)
        ship.draw_ship(self.__screen)
        return ship

    def create_asteroids(self, asteroids_amount):
        for i in range(asteroids_amount):
            aster_xy_location = self.random_location_xy()  # assigning random location
            # Checking that the asteroid's location is not the same as the ship's location
            if aster_xy_location != (self.__ship.get_x(), self.__ship.get_y()):
                aster_vx = random.randint(1, 4)
                aster_vy = random.randint(1, 4)
                # Building, registering and drawing the asteroid
                self.__asteroids.append(ast.Asteroid(aster_xy_location[0], aster_vx, aster_xy_location[1], aster_vy,
                                                     self.ASTEROID_STARTING_SIZE))
                self.__asteroids[i].register_asteroid(self.__screen)
                self.__asteroids[i].draw_asteroid(self.__screen)

    def random_location_xy(self):
        """
        returns a new random location in the board
        :return: new random location in the board
        """
        return random.randint(self.__screen_min_x,
                              self.__screen_max_x), random.randint(self.__screen_min_y, self.__screen_max_y)

    def run(self):
        """
        this function runs the game
        """
        self._do_loop()
        self.__screen.start_screen()

    def _do_loop(self):
        # You don't need to change this method!
        self._game_loop()

        # Set the timer to go off again
        self.__screen.update()
        self.__screen.ontimer(self._do_loop, 5)

    def move_object(self, obj):
        """
        This function responsible to change the location of an object
        :param obj: can be an asteroid, a ship or a torpedo
        """
        speed_x = obj.get_vx()
        speed_y = obj.get_vy()
        delta_x = self.__screen_max_x - self.__screen_min_x
        delta_y = self.__screen_max_y - self.__screen_min_y
        new_coor_x = (speed_x + obj.get_x() - self.__screen_min_x) % delta_x + self.__screen_min_x
        new_coor_y = (speed_y + obj.get_y() - self.__screen_min_y) % delta_y + self.__screen_min_y
        obj.set_x(new_coor_x)
        obj.set_y(new_coor_y)

    def accelerate_ship(self, ship):
        """
        This function responsible to accelerate the ship's speed
        """
        deg_in_rad = DEG_TO_RAD_COEFFICIENT * self.__ship.get_deg()
        new_speed_x = self.__ship.get_vx() + math.cos(deg_in_rad)
        new_speed_y = self.__ship.get_vy() + math.sin(deg_in_rad)
        ship.set_vx(new_speed_x)
        ship.set_vy(new_speed_y)

    def rotate_ship(self, direction):
        """
        This function responsible to rotate the ship
        :param direction: str: 'right' or 'left'
        :return:
        """
        if direction == 'right':
            i = self.__ship.get_deg() - 7
        else:
            i = self.__ship.get_deg() + 7
        self.__ship.set_deg(i)

    def asteroid_ship_intersection(self, asteroid):
        """
        This function is called when a ship hit an asteroid. It creates a massage, reduces ships life and unregister the
        asteroid
        """
        self.__screen.show_message('Ship - Asteroid intersection', 'BOOM')
        self.__screen.remove_life()
        self.__ship.set_life(self.__ship.get_life() - 1)
        asteroid.unregister_asteroid(self.__screen)
        self.__asteroids.remove(asteroid)

    def create_torpedo(self):
        """
        This function create and register a torpedo
        """
        # It only create the torpedo if there are less then 10 torpedos in self.torpedo list
        if len(self.__torpedos) < self.MAX_TORPEDO:
            torpedo_x = self.__ship.get_x()
            torpedo_y = self.__ship.get_y()
            deg_in_rad = DEG_TO_RAD_COEFFICIENT * self.__ship.get_deg()
            torpedo_vx = self.__ship.get_vx() + 2 * math.cos(deg_in_rad)
            torpedo_vy = self.__ship.get_vy() + 2 * math.sin(deg_in_rad)
            new_torpedo = tor.Torpedo(torpedo_x, torpedo_vx, torpedo_y, torpedo_vy, self.__ship.get_deg())
            self.__torpedos.append(new_torpedo)
            new_torpedo.register_torpedo(self.__screen)

    def draw_torpedo(self, torpedo):
        """
        Draw the torpedo on the screen for 200 rounds. After that delete it
        """
        if torpedo.life <= self.TORPEDO_LIFE:
            self.move_object(torpedo)
            torpedo.draw_torpedo(self.__screen)
            torpedo.set_life(torpedo.get_torpedo_life() + 1)
        else:
            torpedo.unregister_torpedo(self.__screen)
            self.__torpedos.remove(torpedo)

    def asteroid_torpedo_intersection(self, torpedo, asteroid):
        """
        This function is called when a torpedo hits an asteroid. It is updating the score, unregister the asteroid and
        call the blow() function (see below)
        """
        self.__score += self.SCORE_DICT[asteroid.get_size()]
        self.__screen.set_score(self.__score)
        self.blow(asteroid, torpedo)
        asteroid.unregister_asteroid(self.__screen)
        self.__asteroids.remove(asteroid)
        self.__screen.unregister_torpedo(torpedo)
        self.__torpedos.remove(torpedo)

    def blow(self, asrto, torp):
        """
        This function responsible to blow an asteroid to two smaller ones after it has been hit by a torpedo
        """
        new_size = self.BLOW_ASTEROID_DICT[asrto.get_size()]
        x = asrto.get_x()
        vx = (torp.get_vx() + asrto.get_vx()) / math.sqrt(math.pow(asrto.get_vx(), 2) + math.pow(asrto.get_vy(), 2))
        y = asrto.get_y()
        vy = (torp.get_vy() + asrto.get_vy()) / math.sqrt(math.pow(asrto.get_vx(), 2) + math.pow(asrto.get_vy(), 2))
        if new_size > 0:  # if the new size is 0 then the function wont create more asteroids
            new_asteroid1 = ast.Asteroid(x, vx, y, vy, new_size)
            new_asteroid2 = ast.Asteroid(x, -vx, y, -vy, new_size)
            self.__asteroids.append(new_asteroid1)
            new_asteroid1.register_asteroid(self.__screen)
            self.__asteroids.append(new_asteroid2)
            new_asteroid2.register_asteroid(self.__screen)

    def is_not_empty_space(self, ship_xy_location):
        """
        This is a util function for teleport_ship() function.
        :param ship_xy_location:
        :return: True if the ship will land at a place with asteroid, false otherwise
        """
        for i in self.__asteroids:
            astr_xy_location = i.get_x(), i.get_y()
            if ship_xy_location == astr_xy_location:
                return True
        return False

    def teleport_ship(self, ship):
        """
        This function responsible to find an empty location of a ship and sent it there
        """
        ship_xy_location = self.random_location_xy()  # assign a new location
        while self.is_not_empty_space(ship_xy_location):  # check if the location is free
            ship_xy_location = self.random_location_xy()  # if it is not empty assign a new location until its free

        # once you find an empty space change the location of the ship and move there.
        x, y = ship_xy_location
        ship.set_x(x)
        ship.set_y(y)
        self.move_object(self.__ship)

    def check_if_end(self):
        """
        This function check if one of the conditions to end the game is valid
        """
        if len(self.__asteroids) == 0:
            self.__screen.show_message('win', 'WELL DONE, YOU WON')
            self.end_game()
        elif self.__ship.get_life() == 0:
            self.__screen.show_message('lost', 'GAVE OVER')
            self.end_game()
        elif self.__screen.should_end():
            self.__screen.show_message('user_quit', 'SEE YOU SOON')
            self.end_game()

    def end_game(self):
        """
        This function end the game
        """
        self.__screen.end_game()
        sys.exit(0)

    def _game_loop(self):

        if self.__screen.is_right_pressed():
            self.rotate_ship('right')

        if self.__screen.is_left_pressed():
            self.rotate_ship('left')

        if self.__screen.is_up_pressed():
            self.accelerate_ship(self.__ship)

        if self.__screen.is_space_pressed():
            self.create_torpedo()

        if self.__screen.is_teleport_pressed():
            self.teleport_ship(self.__ship)

        for torpedo in self.__torpedos:
            self.draw_torpedo(torpedo)

        self.move_object(self.__ship)
        self.__ship.draw_ship(self.__screen)

        # This part of the code deals with asterodis: It loops over the asteroids, moves and draw them

        for asteroid in self.__asteroids:
            self.move_object(asteroid)
            asteroid.draw_asteroid(self.__screen)
            if asteroid.has_intersection(self.__ship):  # check for intersection between asteroid and ship
                self.asteroid_ship_intersection(asteroid)
                break
            for torpedo in self.__torpedos:  # check for intersection between asteroid and torpedo
                if asteroid.has_intersection(torpedo):
                    self.asteroid_torpedo_intersection(torpedo, asteroid)

        self.check_if_end()


def main(amount):
    runner = GameRunner(amount)
    runner.run()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(DEFAULT_ASTEROIDS_NUM)
