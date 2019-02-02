# Arhivo para hacer pruebas de cada uno de los modulos
import descriptive
import dispersion
import probability
from distributions import binomial_distribution, acumulated_binomial, hypergeometric, acumulated_hypergeometric, poisson, exponential
from distributions import uniform

# print("A")
# print(binomial_distribution(7, 0.4, 5))
# print("B")
# print(binomial_distribution(7, 0.4, 0))
# print("C")
# print(binomial_distribution(7, 0.4, 7))

# print("Tres estudiantes o menos")
# print(acumulated_binomial([0,1,2,3], 7, 0.4))

# print("Probabilidad de que al seleccionar una muestra de tres caballos de 10 2 esten enfermos, sabiendo que 4 de los 10 caballos estan enfermos")
# print(hypergeometric(10, 4, 3, 2))

# print("Probabilidad de que de 3 ascensos no mas de 1 ascenso fuera para una mujer considerando que eran cuatro mujeres en un total de 9 personas posibles para ascenso")
# print(acumulated_hypergeometric(9, 4, 3, [0,1]))

# print("Poisson 1: probabilidad de que 4 estudiantes lleguen donde el profesor con un promedio de 5.2 cada 20 minutos")
# print(poisson(4, 5.2))
# print("Poisson 2: probabilidad de que almenos 4 estudiantes lleguen donde el profesor con un promedio de 5.2 cada 20 minutos")
# print(1 - poisson(4, 5.2))

# print(exponential(0.05, 12))

# # print(binomial_distribution(10, 0.8, 4))
# # print(binomial_distribution(10, 0.8, 0))
# # print(binomial_distribution(10, 0.8, 1))
# # print(acumulated_binomial([3,4,5,6],10, 0.8))

# print(uniform(16, 17.2, 14.5, 17.5))

from distributions import norm

print(1 - norm(36, 78, 0, 72))