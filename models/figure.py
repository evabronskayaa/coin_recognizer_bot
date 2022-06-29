from abc import ABC


class Figure(ABC):
    @property
    def name(self):
        pass


class Rectangle(Figure):
    @Figure.name.getter
    def name(self):
        return 'прямоугольник'


class Circle(Figure):
    @Figure.name.getter
    def name(self):
        return 'круг'


class Triangle(Figure):
    @Figure.name.getter
    def name(self):
        return 'треугольник'