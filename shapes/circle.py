import numpy as np
from matplotlib import pyplot as plt

from contants import RADIUS
from shapes import drawable


class Circle(drawable.Drawable):
    def __init__(self, center, radius):
        self._radius = radius
        self._center = center

    def draw(self, fig, ax):
        # circle = plt.Circle((self._center.getX(), self._center.getY()), self._radius, color='red')
        around_circle = plt.Circle((self._center.getX(), self._center.getY()), self._radius, color=self._center.get_color(), fill=False)
        self._center.draw(fig, ax)
        # ax.add_artist(circle)
        ax.add_artist(around_circle)

    def shift(self, x, y):
        self._center.shift(x, y)

    def contained_points(self, g):
        xs, ys = g.get_lattice()
        diff_x = xs - self._center.getX()
        diff_y = ys - self._center.getY()
        return ((diff_x ** 2 + diff_y ** 2) ** 0.5 <= RADIUS).nonzero()[0]

