#!/usr/bin/env python3
"""Módulo que define las clases BaseGeometry y Rectangle."""


class BaseGeometry:
    """Representa una clase base para figuras geométricas."""

    def area(self):
        """Indica que el cálculo del área no está implementado."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Valida que el valor sea un entero positivo."""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Representa un rectángulo con dimensiones privadas."""

    def __init__(self, width, height):
        """Inicializa y valida el ancho y la altura."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
