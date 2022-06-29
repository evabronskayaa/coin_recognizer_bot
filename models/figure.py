from abc import ABC


class Object(ABC):
    @property
    def name(self):
        pass


class Rectangle(Object):
    @Object.name.getter
    def name(self):
        return "прямоугольник"


class Circle(Object):
    @Object.name.getter
    def name(self):
        return "круг"


class Triangle(Object):
    @Object.name.getter
    def name(self):
        return "треугольник"