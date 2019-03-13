import distributions
import intervals
import hipotesis
import math

# # 1
# n = 12
# pi = 0.4
# probability_five = distributions.binomial_distribution(n, pi, 5)
# probability_more_five = distributions.acumulated_binomial(range(6, n + 1), n, pi)

# # 2
# N = 20
# r = 8

# n = 3
# X = 1
# probability_one = distributions.hypergeometric(N, r, n, X)
# # print(probability_one)

# # 3
# miles_bad = distributions.poisson(1, 1.5)
# # print(miles_bad)

# # 4
# probability_more_15 = 1 - distributions.exponential(15, 2)
# print(probability_more_15)
# # 5
# probility_range = distributions.uniform(12.7, 14.5, 18.3, 10.2)
# # print(probility_range)
# # 6
# probability_rains_3 = 1 - distributions.norm(0.8, 2.2, 0, 3.3)
# probability_rains_1 = 1 - distributions.norm(0.8, 2.2, 0, 1.3)
# probability_rain_2_3 = distributions.norm(0.8, 2.2, 2.7, 3.0)
# amount_ten = distributions.norm(0.8, 2.2, 0, 1.176)
# print(amount_ten)

# employers = distributions.binomial_distribution(150, 0.45, 72)
# print(employers)
# inv = distributions.norm(0.12, 0.3, 0.3, 0.31)
# print(inv)
# print(distributions.norm((12 / (250 ** 0.5)) , 30, 30, 31))
# print(intervals.interval_poblational_average(35500, 7200, 100, 1.96))
# print(intervals.interval_poblational_average_scipy(35500, 7200, 100, 0.95))
# print(intervals.interval_poblational_average(0.062, 0.017, 200, 1.64))
# print(math.ceil(distributions.when_get_x(13812, 3550, 0.15)))
# print(intervals.interval_poblational_average_t(1275.0, 235.0, 12, 0.95))
# print(intervals.get_interval_p(350.0, 77.0, 2.56))
# print(intervals.get_interval_p(1020.0, 673.0, 2.56))
# print(intervals.get_z(0.95))
# print(intervals.interval_poblational_average(2365.0, 983.0, 20, 2.56))
# print(intervals.get_sample_length_p_m(1.64, 8659**2, 2000, 0))
# print(intervals.get_sample_length_p_m(1.96, 6, 2, 0))
# intervals.get_sample_length_p_m()
# print(intervals.get_sample_length_p_m(1.64, 750.0, 100, 0))

# print(hipotesis.get_z_two_queues(298.10, 312.0, 97.30, 200.0))
# print(distributions.when_get_x(0, 1, 0.95))
# print(hipotesis.get_z_two_queues(31366.0, 31000, 1894.0, 100))
# print(hipotesis.get_p(31366.0, 31000.0, 1894.0, 100))
# print(hipotesis.get_z_two_queues(492.0/800.0, 0.6, ))
# print(hipotesis.get_hipotesis_p(492.0/800.0, 0.6, 800.0))
# print(hipotesis.get_hipotesis_p(120.0/700.0, 0.21, 700.0))
# print(hipotesis.get_p(106.81, 100.0, 36.60, 100.0, False))
# alpha = distributions.when_get_x(0, 1, 0.98)
# print(hipotesis.get_z_two_queues(80.23, 75, 45.67, 100))
# print(alpha)
#  hipotesis.proof_diff_means()
# print(hipotesis.proof_diff_means(76.0, 77.97, 2.56, 13.5**2, 9.05**2, 45.0, 40.0))
# print(hipotesis.proof_diff_means_t(3.5, 3.9, 15, 10, 15.3, 17.1, ))
# print(intervals.interval_poblational_average_t(1275.0, 235.0, 12, 0.95))
# print( intervals.interval_poblational_average_t(15.2, 0.86, 22, 0.95) )
# print(hipotesis.get_z_two_queues(41.17, 40.0, 4.71, 15))
n1 = 100.0
x_1 = 17.2
s_1 = 5.3

n2 = 75.0
x_2 = 19.4
s_2 = 4.5
proof_routes = hipotesis.proof_diff_means(x_1, x_2, 1.96, s_1**2, s_2**2, n1, n2)
print(proof_routes)
