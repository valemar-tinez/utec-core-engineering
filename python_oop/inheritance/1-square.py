#!/usr/bin/env python3
"""Módulo que define la clase Square heredada de Rectangle."""


Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Representa un cuadrado con tamaño privado."""

    def __init__(self, size):
        """Inicializa el cuadrado validando su tamaño."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Devuelve el área del cuadrado."""
        return self.__size ** 2
