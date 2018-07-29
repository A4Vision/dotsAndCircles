import abc


class Drawable(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def draw(self, fig, ax):
        pass


