## Inheritance

Ejercicios de Programación Orientada a Objetos en Python, enfocados en herencia, polimorfismo y reutilización de código.

##  Ejercicio 1: Geometría básica

Implementación de una clase BaseGeometry que proporciona una estructura común para futuras figuras geométricas. Se define el método area(), que lanza una excepción indicando que el cálculo del área todavía no está implementado en la clase base.

Se incorpora el método integer_validator(), que verifica que un valor sea un número entero mayor que cero y genera las excepciones TypeError o ValueError cuando no cumple las condiciones. Esta validación podrá reutilizarse mediante herencia en otras clases geométricas.

Ejercicio 2: Rectángulo

Implementación de una clase Rectangle que hereda de BaseGeometry y representa un rectángulo mediante dos atributos privados, __width y __height, inicializados a través del método __init__().

Se reutiliza el método heredado integer_validator() para comprobar que ambas dimensiones sean números enteros mayores que cero, evitando duplicar la lógica de validación y aplicando el principio de reutilización de código mediante herencia.

## Ejercicio 3: Rectángulo completo

Implementación de una clase Rectangle que hereda de BaseGeometry y representa un rectángulo mediante los atributos privados __width y __height. Ambas dimensiones se inicializan en el constructor y se validan utilizando el método heredado integer_validator().

Se incorpora el método area() para calcular la superficie del rectángulo multiplicando el ancho por la altura, y el método especial __str__() para mostrar su representación mediante el formato [Rectangle] width/height. Esta implementación permite aplicar los conceptos de herencia y polimorfismo.
