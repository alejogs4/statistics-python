from math import sqrt, pow
from distributions import norm
import scipy.stats as ss

# Cuando la desviacion poblacional es conocidad se recibe average (X barra) (s) que es la desviacion
# n que es tamano de la muestra y (z) que se define dependiendo del coeficiente de confianza deseado
# Seria 1.96 para un coeficiente de confianza del 95%
# 2.58 para un 99%
# 1.64 para 90%
def interval_poblational_average(average, s, n, z):
    standard = s / sqrt(n)
    minimun = average - z*standard
    maximun = average + z*standard
    return (minimun, maximun)

def interval_poblational_average_scipy(average, s, n, confidence_level):
  return ss.norm(average, s / (n**0.5)).interval(confidence_level)

def interval_poblational_average_t(average, deviation, sample_length, alpha):
  t = ss.t.interval(alpha, sample_length - 1)[1]
  standard = deviation / sqrt(sample_length)
  minimun = average - t*standard
  maximun = average + t*standard

  return (minimun, maximun)

def get_interval_p(n, n_special, z):
    p = n_special / n
    sp = sqrt((p * (1 - p)) / n)
    mini = p - z * sp
    maxi = p + z * sp
    return (mini, maxi)

def get_sample_length(z, s, error):
  return (pow(z, 2) * pow(s,2)) / pow(error, 2)

def get_sample_length_p_m(z, variance_p, average_m, average_p):
  return (pow(z, 2) * pow(variance_p, 2)) / (pow(average_m - average_p, 2))

def get_sample_length_p_p(z, proportion_p, proportion_m):
  pi = ( proportion_p ) * ( 1 - proportion_p )
  return (pow(z, 2) * pi) / pow( proportion_m - proportion_p, 2 )

def get_z(coefficient):
  return norm(1, 0, 0, coefficient / 2)

