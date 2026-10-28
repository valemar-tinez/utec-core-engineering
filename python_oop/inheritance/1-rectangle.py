#!/usr/bin/env python3
"""Módulo que define la clase Rectangle heredada de BaseGeometry."""

from base_geometry import BaseGeometry


class Rectangle(BaseGeometry):
    """Representa un rectángulo con ancho y altura privados."""

    def __init__(self, width, height):
        """Inicializa el rectángulo validando sus dimensiones."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
