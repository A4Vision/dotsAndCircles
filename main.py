import collections

from shapes import circle, grid
from shapes import point
from contants import RADIUS
import numpy as np
from matplotlib import pyplot as plt


def find_possibles_shapes():
    fig, ax = plt.subplots()
    g = grid.Grid(50, 250, 1)
    all_points_sets = set()
    circles = set()

    for center_x in np.arange(RADIUS, RADIUS + 1, 0.05):
        print("hello3", center_x)
        for center_y in np.arange(RADIUS, RADIUS + 1, 0.05):
            center = point.Point(center_x, center_y, 'blue')
            c = circle.Circle(center, RADIUS)
            points = c.contained_points(g)
            frozen_points = frozenset(points)
            if frozen_points not in all_points_sets:
                all_points_sets.add(frozen_points)
                circles.add(c)
                c.draw(fig, ax)
    print(len(circles))
    mif = collections.Counter(map(len, all_points_sets))
    print(mif)
    diff = max(mif.keys()) - min(mif.keys())
    print(diff)
    print(min(mif.keys()))
    ax.set_ylim(0, 50)
    ax.set_xlim(0, 30)
    g.draw(fig, ax)
    print("hello4")
    plt.show()


def main():
    print("hello")
    find_possibles_shapes()
    print("hello2")


if __name__ == '__main__':
    main()
