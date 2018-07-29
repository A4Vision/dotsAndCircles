from shapes import drawable


class Point(drawable.Drawable):
    def __init__(self, x, y, color):
        self._x = x
        self._y = y
        self._color = color

    def draw(self, fig, ax):
        ax.plot([self._x], [self._y], '.', color=self._color)

    def shift(self, x, y):
        self._x += x
        self._y += y

    def getX(self):
        return self._x

    def getY(self):
        return self._y

    def get_color(self):
        return self._color