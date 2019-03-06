from math import sqrt, pow
from distributions import norm
# Se usa esto cuando se quiere obtner el valor de z
# En una prueba de dos colas, permitiendo tomar una decision
# Tambien puede ser usado para conseguir el valor de t
def get_z_two_queues(sample_mean, population_mean_null, deviation, length):
  standard_error = deviation / sqrt( length )

  return (sample_mean - population_mean_null) / standard_error



def get_p(sample_mean, population_mean_null, deviation, length, one = True):
  z = get_z_two_queues(sample_mean, population_mean_null, deviation, length)
  size = norm(1, 0, 0, z)
  if (one):
    return 0.5 - size
  return ( 0.5 - size ) * 2

def proof_pi(proportion_sample, proportion_population, length):
  error = sqrt( (proportion_population * ( 1- proportion_population )) / length )
  return (proportion_sample - proportion_population) / error

def proof_diff_means(mean1, mean2, z, variance1, variance2, n1, n2):
  error = sqrt( (variance1 / n1) + (variance2 / n2) )
  difference = mean1 - mean2

  minimun = difference - z * error
  maximun = difference + z * error

  return ( minimun, maximun )

def proof_diff_means_t(variance1, variance2, n1, n2, mean1, mean2, t):
  sp = ( (variance1 * (n1 - 1)) + variance2*(n2 - 1) ) / (n1 + n2 - 2)
  difference = mean1 - mean2
  error = sqrt( (sp / n1) + (sp / n2) )
  
  minimun = difference - t*error
  maximun = difference + t*error

  return minimun, maximun

def proof_diff_proportions(p1, p2, n1, n2, z):
  error = sqrt( ((p1*(1-p1)) / n1) + ((p2*(1-p2)) / n2))
  diff = p1 - p2

  minimun = diff - z*error
  maximun = diff + z*error

  return minimun, maximun

def get_size_to_estimate_population_diff_means(z, variance1, variance2, error):
  return (pow(z, 2) * (variance1 + variance2)) / pow(error, 2)

def get_size_to_estimate_population_diff_proportions(z, p1, p2, error):
  p_operations = ( p1*(1-p1) + p2*(1-p2) )

  return (pow(z, 2) * p_operations) / pow(error, 2)

def proof_hip_means_different_samples(mean1, mean2, meanp1, meanp2, variance1, variance2, n1, n2):
  error = sqrt( (variance1 / n1) + (variance2 / n2)  )

  return ((mean1 - mean2) - ( meanp1 - meanp2 )) / error

def proof_little_sample_two(mean1, mean2, meanp1, meanp2, variance1, variance2, n1, n2):
  sp = (variance1 * (n1 - 1) + variance2*(n2 - 1)) / (n1 + n2 - 2)
  error = sqrt((sp / n1) + (sp / n2))

  return ((mean1 - mean2) - ( meanp1 - meanp2 )) / error

# def interval_pareadas(sample1, sample2, t):
#   from functools import reduce

#   if (len(sample1) != len(sample2)):
#     return
#   n = len(sample1)

#   suma = []
#   for i in range(0, len(sample1)):
#     suma.append(sample1[i] - sample2[i])

#   d = reduce(lambda a,b: a + b, suma) / n
#   d2 = reduce(lambda a,b: a + b,map(lambda a: a**2, sum))

#   sd = sqrt((d2 - n * (d**2)) / (n -1))

#   minimun = d - t*(sd / sqrt(n))
#   maximun = d + t*(sd / sqrt(n))

#   return minimun, maximun 

