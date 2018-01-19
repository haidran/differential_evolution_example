# Differential Evolution Example

Ejemplo de algoritmo evolutivo diferencial para la minimización de la función de esfera.

## Dependencias

Para ejecutar el programa se debe disponer de **Python 3** en el sistema. Casi todos los sistemas operativos modernos incluyen este intérprete de código por defecto.

Por el momento, no se requiere ningún programa ni biblioteca adicional.

## Ejecución

Para lanzar el programa, basta con clonar este repositorio y ejecutar *sphere.py* junto con sus parámetros en la consola:

```
./sphere.py NP F CR D MIN MAX N_GENERATIONS 
```

Para obtener una descripción de los parámetros, puede utilizarse:

```
./sphere.py --help
````

## Parámetros

Se pueden pasar argumentos al programa para ajustar el tamaño del problema, las características del algoritmo y el número de procesos evolutivos que se ejecutan en total.

- **NP**: Tamaño de la población.
- **F**: Peso de las diferencias entre los individuos de cara a la fase de mutación.
- **CR**: Probabilidad de que se introduzcan mutaciones en el individuo durante la fase de cruce.
- **D**: Dimensión del problema (en este caso, número de variables de la función de esfera).
- **MIN**: Valor mínimo que pueden alcanzar los parámetros de los individuos para reducir el espacio del problema.
- **MAX**: Valor máximo que pueden alcanzar los parámetros de los individuos para reducir el espacio del problema.
- **N_GENERATIONS**: Número de la generación en la que se detendrá la evolución.