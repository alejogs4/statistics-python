# Arhivo para hacer pruebas de cada uno de los modulos
import descriptive
import dispersion
import probability
from distributions import binomial_distribution, acumulated_binomial, hypergeometric, acumulated_hypergeometric, poisson, exponential, norm
from distributions import uniform
from intervals import interval_poblational_average, interval_poblational_average_t, get_interval_p, get_sample_length_p_m, get_sample_length_p_p, get_z
from hipotesis import get_z_two_queues, get_p, proof_pi, proof_diff_means, proof_diff_means_t, proof_diff_proportions, get_size_to_estimate_population_diff_means, get_size_to_estimate_population_diff_proportions
from ANOVA import anova

any = anova([85,72,83,80], [80,84,81,78,82], [82,80,85,90,88])
print(any)


