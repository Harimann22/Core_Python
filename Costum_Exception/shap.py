from abc import ABC, abstractmethod


class Shape(ABC):
    # @staticmethod
    def __init__(self, color, bw):
        self.__color = color
        self.__bw = bw

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def get_bw(self):
        return self.__bw

    @classmethod
    def area(self):
        return-1

    @abstractmethod
    def mass(self):
        return
