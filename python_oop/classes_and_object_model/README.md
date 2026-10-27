# Classes and Object Model

Ejercicios de Programación Orientada a Objetos en Python.

## Ejercicio 0: Mi primer cuadrado

Creación de una clase Square vacía.

## Ejercicio 1: Cuadrado con tamaño

Creación de una clase Square con un atributo privado.

## Ejercicio 2: Validación de tamaño

Creación de una clase Square con un atributo privado __size y validación del tamaño. El tamaño debe ser un número entero mayor o igual a cero.

## Ejercicio 3: Área de un cuadrado

Implementación de una clase Square con un atributo privado __size y validación del tamaño.Se agrega el método de instancia area(), que calcula y devuelve el área del cuadrado elevando el tamaño al cuadrado.

## Ejercicio 4: Acceder y actualizar un atributo privado

Implementación de una clase Square con un atributo privado __size y acceso controlado mediante getter y setter.

Se utiliza @property para consultar el tamaño y @size.setter para actualizarlo. El setter valida que el tamaño sea un número entero mayor o igual a cero.

El método area() devuelve el área del cuadrado.

## Ejercicio 5: Imprimir un cuadrado

Implementación de una clase Square con un atributo privado __size, acceso controlado mediante getter y setter, validación del tamaño y un método area() para calcular el área del cuadrado.

Se incorpora el método público my_print(), que imprime un cuadrado utilizando el carácter #, con tantas filas y columnas como indique su tamaño. Si el tamaño es cero, imprime una línea vacía.
 
## Ejercicio 6: Imprimir la instancia cuadrada 

Implementación de una clase Square con atributos privados __size y __position, acceso controlado mediante getters y setters, validación de valores y un método area() para calcular el área del cuadrado.

Se incorpora el método especial __str__() para representar el cuadrado como una cadena de caracteres #, considerando su posición horizontal y vertical. El método my_print() imprime esa representación y, si el tamaño es cero, muestra una línea vacía.
