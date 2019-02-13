from math import sqrt

def p_kwon(average, s, n, z):
    standard = s / sqrt(n)
    minimun = average - z*standard
    maximun = average + z*standard
    return (minimun, maximun)

def get_interval(n, n_special, z):
    p = n_special / n
    sp = sqrt((p * (1 - p)) /n)
    mini = p - z * sp
    maxi = p + z * sp
    return (mini, maxi)
