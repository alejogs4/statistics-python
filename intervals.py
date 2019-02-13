from math import sqrt
def p_kwon(average, s, n, z):
    standard = s / sqrt(n)
    minimun = average - z*standard
    maximun = average + z*standard
    return (minimun, maximun)
