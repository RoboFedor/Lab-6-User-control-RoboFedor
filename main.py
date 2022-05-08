""" Lab 7 - User Control """
import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class GameObject:
    def __init__(self, size, color, x, y):
        self.size = size
        self.color = color
        self.x = x
        self.y = y

    def update(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pass


class Ball(GameObject):
    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.size, self.color)


class Square(GameObject):
    def __init__(self, size, color, x, y, speed_x, speed_y) -> None:
        super(Square, self).__init__(size, color, x, y)
        self.speed_x = speed_x
        self.speed_y = speed_y

    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.size, self.size, self.color)

    def update(self, x=None, y=None):
        super(Square, self).update(self.x + self.speed_x, self.y + self.speed_y)


# !TODO Добавить звуковые эффекты
class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")

        arcade.set_background_color((240, 240, 255))

        self.ball = Ball(70, arcade.color.GOLD, 200, 200)

        self.square = Square(70, arcade.color.BLUE_VIOLET, 300, 500, 0, 0)
        self.squares = [self.square]

        self.game_objects = [self.ball, self.square]

    def on_key_press(self, symbol: int, modifiers: int):
        for square in self.squares:
            if symbol == arcade.key.LEFT:
                square.speed_x = -5
            if symbol == arcade.key.RIGHT:
                square.speed_x = 5
            if symbol == arcade.key.UP:
                square.speed_y = 5
            if symbol == arcade.key.DOWN:
                square.speed_y = -5

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        self.ball.update(x, y)

    def on_key_release(self, symbol: int, modifiers: int):
        for square in self.squares:
            if symbol == arcade.key.LEFT:
                square.speed_x = 0
            if symbol == arcade.key.RIGHT:
                square.speed_x = 0
            if symbol == arcade.key.UP:
                square.speed_y = 0
            if symbol == arcade.key.DOWN:
                square.speed_y = 0

    def on_draw(self):
        arcade.start_render()
        for obj in self.game_objects:
            obj.draw()

    def on_update(self, delta_time):
        for square in self.squares:
            square.update()


def main():
    window = MyGame()
    window.run()


main()
