from functools import reduce
from statistics import mode
from functional import foreach
from math import sqrt

# Consigue el valor medio de un conjunto de datos
def median(sample):
  length = len(sample) - 1
  if (length % 2 == 0):
    return (sample[ length / 2 ] + sample[ (length / 2) + 1 ]) / 2

  return  sample[ (length + 1) / 2 ]

# Consigue el promedio de un conjunto de datos
def average(sample):
  _sum = reduce(lambda a,b: a + b, sample)  
  length = len(sample)
  
  return _sum / length

# Consigue el promedio teniendo en cuenta el peso de cada elemento
def weighted_average(sample):
  weights = map(lambda data: data['weight'], sample)
  weights_reduced = reduce(lambda a, b: a + b, weights)

  average = 0
  for data in sample:
    average = average + ( data.get('data') * data.get('weight') )

  return average / weights_reduced
  
# Determina la varianza de un conjunto de datos
def variance(sample):
  sample_average = average(sample)
  length = float( len(sample) )

  variance_calc = 0
  for i in sample:
    variance_calc += (i - sample_average) ** 2
  
  return variance_calc / (length - 1)

# Determina la desviacion estandard de un conjunto de datos
def standard_deviation(sample):
  sample_variance = variance(sample)
  return sqrt(sample_variance)


