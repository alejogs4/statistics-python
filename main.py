# Arhivo para hacer pruebas de cada uno de los modulos
import descriptive
import dispersion
import probability
from distributions import binomial_distribution, acumulated_binomial, hypergeometric, acumulated_hypergeometric, poisson, exponential, norm
from distributions import uniform
from intervals import interval_poblational_average, interval_poblational_average_t, get_interval_p, get_sample_length_p_m, get_sample_length_p_p, get_z
from hipotesis import get_z_two_queues, get_p, proof_pi, proof_diff_means, proof_diff_means_t, proof_diff_proportions, get_size_to_estimate_population_diff_means, get_size_to_estimate_population_diff_proportions
from ANOVA import anova

# Taller
# print(binomial_distribution(10, 0.05, 2))
## Si me piden menor a 2
# print(acumulated_binomial(range(0, 3), 10, 0.05))

'''Aqui es si me piden mayor a algo en poisson'''
# sum = 0
# for i in range(0, 11):
#     sum += poisson(i, 10.0)

# print(1 - sum)