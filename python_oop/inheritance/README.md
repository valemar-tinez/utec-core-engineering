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

## Ejercicio 4: Cuadrado #1

Implementación de una clase Square que hereda de Rectangle y representa un cuadrado mediante el atributo privado __size. El tamaño se valida utilizando el método heredado integer_validator(), garantizando que sea un número entero mayor que cero.

Se utiliza super().__init__() para inicializar el ancho y la altura del rectángulo con el mismo valor, reutilizando la funcionalidad de la clase padre. Se implementa el método area() para calcular la superficie del cuadrado y se hereda la representación en cadena definida en Rectangle.

## Ejercicio 5: Cuadrado #2

Implementación de una clase Square que hereda de Rectangle y representa un cuadrado mediante el atributo privado __size. Se mantiene la validación del tamaño con integer_validator(), la inicialización de las dimensiones mediante super().__init__() y el método area() para calcular su superficie.

Se incorpora el método especial __str__(), que sobrescribe la representación heredada de Rectangle y permite mostrar el cuadrado con el formato [Square] width/height. De esta manera, se aplican los conceptos de herencia, polimorfismo y sobrescritura de métodos.
