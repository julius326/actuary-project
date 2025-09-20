import math

def arithmetic_mean_freq(x, f):
    return sum(xi * fi for xi, fi in zip(x, f)) / sum(f)

def geometric_mean_freq(x, f):
    product = 1
    for xi, fi in zip(x, f):
        product *= xi ** fi
    return product ** (1/sum(f))

def harmonic_mean_freq(x, f):
    return sum(f) / sum(fi/xi for xi, fi in zip(x, f))
