# Arhivo para hacer pruebas de cada uno de los modulos
import descriptive
import dispersion
import probability

sample = [1,2,3,4,5,6,7]
median = descriptive.median(sample)
percentile50 = dispersion.percentile(50, sample)
odd = probability.classic_probability(sample, lambda x: x % 2 == 0)

print(median)
print(percentile50)
print(odd)
