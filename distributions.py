from math import factorial, pow, e, fabs, pi, sqrt
from probability import combination
import scipy.integrate as integrate
from functools import reduce

# Define binomial se usa cuando se tiene un tamano de muestra una probabilidad de exito y valor a encontrar probabilidad
# Por ejemplo probabilidad que de 30 personas(length) 8 (number_succes) con un porcentaje de exito del 0.5 (succes probability)
def binomial_distribution(length, succes_probability, number_succes):
  div = factorial(length) / (factorial(number_succes) * factorial(length - number_succes)) 
  multiply = pow(succes_probability, number_succes) * pow(1 - succes_probability, length - number_succes)

  return  div * multiply

# Se toma cuando en la distrubucion binomial se pide encontrar la probabilidad de algun rango, por ejemplo x < 3
# se pone [0,1,2,3]
def acumulated_binomial(cases, length, succes_probability):
  cases_binomial = map(lambda x: binomial_distribution(length, succes_probability, float(x)), cases)
  probability = reduce(lambda a,b: a + b, cases_binomial)

  return probability


def hypergeometric(length, sample_especial, sample_length, x):
  first = float(combination(sample_especial, x))
  second = float(combination(length - sample_especial, sample_length - x))
  third = float(combination(length, sample_length))

  return first * second / third

def acumulated_hypergeometric(length, sample_especial, sample_length, cases):
  cases_hypergeometric = map(lambda x: hypergeometric(length, sample_especial, sample_length, x), cases)
  probability = reduce(lambda a,b: a + b, cases_hypergeometric)
  return probability

def poisson(x, average):
  return (pow(average, x) * pow(e, -average)) / factorial(x)

def exponential(gap, average):
  return 1 - pow(e, -average * gap)

def uniform(x1, x2, greather, less):
  return fabs((x2 - x1) / (greather - less))

def norm(deviation, average, x1, x2):
  inte = integrate.quad(lambda x : pow(e,-0.5 * (pow(x - average, 2) / pow(deviation, 2)) ), x1, x2)
  result = inte[0]
  constant = 1 / (sqrt(2 * pi) * deviation)

  return constant * result

def get_z(x_, average, deviation, n):
    return (x_ - average) / (deviation / sqrt(n))

def when_get_x(average, deviation, percent):
  from scipy.stats import norm
  return norm(average, deviation).ppf(percent)
  

