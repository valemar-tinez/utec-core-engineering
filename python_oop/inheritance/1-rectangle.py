#!/usr/bin/env python3
"""Módulo que define la clase Rectangle."""


BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Representa un rectángulo con dimensiones privadas."""

    def __init__(self, width, height):
        """Inicializa el rectángulo validando sus dimensiones."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
