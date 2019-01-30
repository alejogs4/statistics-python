from math import ceil
# Define que tan sesgado esta un conjunto de datos
# esto generalmente indica la presencia de valores atipicos
# valor < 0 sesgo negativo moda > mediana > media
# valor > 0 sesgo positivo moda < mediana < media
# valor == 0 simetria, esta distribuido de forma normal
# valores entre -0.37 y 0.37 se toman como simetricos
def pearson_coefficient(average, median, standard_deviation):
  return (3 * ( average - median )) / standard_deviation

def range(sample):
  max_value = max(sample)
  min_value = min(sample)

  return max_value - min_value

# Determina el grado de dispersion de un conjunto de datos relativo a su media
# dado que tanto la desviacion estandard como la media tienen las mismas unidades
# el coeficiente de variacion sirve para comparar la variabilidad de los datos de dos conjuntos de datos diferente
def coefficiente_variation(average, standard_deviation):
  return ( standard_deviation / average ) * 100

# Percentil define un valor que satisface que el s% dado de datos es menor o igual a ese valor
# y que el (100 - s%)% es mayor o igual a ese valor
# EJ para [1,2,3,4,5,6,7] el percentil 50 es 4
def percentile(percentage, sample):
  length = len(sample) - 1
  index = ((( length - 1 ) * percentage) / 100) + 1
  element_index = int(ceil(index))

  percentile_value = sample[element_index] + ( sample[element_index + 1] - sample[element_index] ) * ( index - element_index )

  return percentile_value

