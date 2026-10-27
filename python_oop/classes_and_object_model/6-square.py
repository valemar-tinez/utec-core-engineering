#!/usr/bin/env python3
"""Módulo que define la clase Square con posición y representación."""


class Square:
    """Representa un cuadrado con tamaño y posición privados."""

    def __init__(self, size=0, position=(0, 0)):
        """Inicializa el cuadrado con tamaño y posición."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Devuelve el tamaño del cuadrado."""
        return self.__size

    @size.setter
    def size(self, value):
        """Valida y actualiza el tamaño del cuadrado."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Devuelve la posición del cuadrado."""
        return self.__position

    @position.setter
    def position(self, value):
        """Valida y actualiza la posición del cuadrado."""
        if (type(value) is not tuple or len(value) != 2
                or any(type(n) is not int or n < 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Devuelve el área del cuadrado."""
        return self.__size ** 2

    def my_print(self):
        """Imprime el cuadrado utilizando el carácter #."""
        print(self)

    def __str__(self):
        """Devuelve la representación del cuadrado como cadena."""
        if self.__size == 0:
            return ""

        lines = [" " * self.__position[0] + "#" * self.__size
                 for i in range(self.__size)]

        return "\n" * self.__position[1] + "\n".join(lines)
