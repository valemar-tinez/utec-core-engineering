#!/usr/bin/env python3
"""Módulo que define la clase Rectangle con área y representación."""


BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Representa un rectángulo con dimensiones privadas."""

    def __init__(self, width, height):
        """Inicializa el rectángulo validando sus dimensiones."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Devuelve el área del rectángulo."""
        return self.__width * self.__height

    def __str__(self):
        """Devuelve la representación del rectángulo como cadena."""
        return f"[Rectangle] {self.__width}/{self.__height}"
