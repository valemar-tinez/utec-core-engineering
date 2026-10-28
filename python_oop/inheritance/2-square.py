#!/usr/bin/env python3
"""Módulo que define la clase Square con representación propia."""


Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Representa un cuadrado que hereda de Rectangle."""

    def __init__(self, size):
        """Inicializa el cuadrado validando su tamaño."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Devuelve el área del cuadrado."""
        return self.__size ** 2

    def __str__(self):
        """Devuelve la representación del cuadrado como cadena."""
        return f"[Square] {self.__size}/{self.__size}"
