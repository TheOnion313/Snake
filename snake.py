import aple
import main
import snake_unit


class Snake(object):

    def __init__(self, x, y):
        self.units = []
        self.head = snake_unit.SnakeUnit(x, y)
        for i in range(main.INIT_LENGTH - 1):
            y += main.SNAKE_SIZE
            self.units.append(snake_unit.SnakeUnit(x, y))
        self.velx = 0
        self.vely = -main.SNAKE_VEL
        self.dead = False

    def update(self, apple):

        for i in range(len(self.units) - 1, 0, -1):
            self.units[i].x, self.units[i].y = self.units[i - 1].x, self.units[i - 1].y

        if not self.dead:
            self.units[0].x, self.units[0].y = self.head.x, self.head.y

        self.head.x += self.velx
        self.head.y += self.vely

        for unit in self.units:
            if unit.x == self.head.x and unit.y == self.head.y:
                self.dead = True

        if self.head.x > main.width or self.head.x < 0 or self.head.y > main.height or self.head.y < 0:
            self.dead = True

        for unit in self.units:
            unit.show()

        new_apple = False
        if self.head.x == apple.x and self.head.y == apple.y:
            self.units.append(snake_unit.SnakeUnit(self.units[-1].x, self.units[-1].x))
            new_apple = True
        self.head.show()


        return new_apple