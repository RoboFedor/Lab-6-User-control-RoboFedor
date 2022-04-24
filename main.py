""" Lab 7 - User Control """

import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


# !TODO class Ball
class Ball:

    def __init__(self, size, color,x,y) -> None:
        size = size
        color = color
        self.x=x
        self.y=y
    def draw(self):
        arcade.draw_circle_filled(self.x,self.y,35,(1,150,120))
    def update(self,x,y):
        self.x=x
        self.y=y






class Square:

    def __init__(self, size, color,x,y,speed_x,speed_y) -> None:
        self.size = size
        self.color = color
        self.x = x
        self.y = y
        self.speed_x=speed_x
        self.speed_y=speed_y
    def draw(self):
        arcade.draw_rectangle_filled(self.x,self.y,80,80,(140,120,100))
    def on_update(self):
        self.x=self.x+self.speed_x
        self.y=self.y+self.speed_y

# !TODO class Square


# !TODO Добавить звуковые эффекты
class MyGame(arcade.Window):
    """ Our Custom Window Class"""
    def on_key_press(self, symbol: int, modifiers: int):
        if symbol==arcade.key.LEFT:
            self.square.speed_x=-5
        if symbol==arcade.key.RIGHT:
            self.square.speed_x=5
        if symbol==arcade.key.UP:
            self.square.speed_y=5
        if symbol==arcade.key.DOWN:
            self.square.speed_y=-5

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        self.ball.update(x,y)
        print("car")

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.LEFT:
            self.square.speed_x = 0
        if symbol == arcade.key.RIGHT:
            self.square.speed_x = 0
        if symbol == arcade.key.UP:
            self.square.speed_y = 0
        if symbol == arcade.key.DOWN:
            self.square.speed_y = 0

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")

        arcade.set_background_color((240,240,255))

        # !TODO создать объекты этих двух классов
        self.ball = Ball(70, arcade.color.GOLD,200,200)
        self.square = Square(70, arcade.color.BLUE_VIOLET,300,500,0,0)

    def on_draw(self):
        arcade.start_render()
        self.ball.draw()
        self.square.draw()

    def on_update(self, delta_time):
        self.square.on_update()

    # !TODO on_mouse_motion - должен двигать круг

    # !TODO on_key_press, on_key_release - должны двигать квадрат (учесть выход за границы экрана)


def main():
    window = MyGame()
    arcade.run()


main()
