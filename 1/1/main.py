def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    lcm = (a * b) // gcd(a, b)
    return lcm

def reduce(fraction):
    a = gcd(fraction[0], fraction[1])
    fraction[0] = int(fraction[0] / a)
    fraction[1] = int(fraction[1] / a)
    return fraction

def fraction(numerator=None, denominator=None):
    return [numerator, denominator]

def add_fractions_1(fraction_1, fraction_2):
    lcm_temp = lcm(fraction_1[1], fraction_2[1])
    frac_1_mult = lcm_temp / fraction_1[1]
    frac_2_mult = lcm_temp / fraction_2[1]
    fraction_2[0] = int(fraction_1[0] * frac_1_mult + fraction_2[0] * frac_2_mult)
    fraction_2[1] = lcm_temp
    reduce(fraction_2)

def add_fractions_2(fraction_1, fraction_2):
    lcm_temp = lcm(fraction_1[1], fraction_2[1])
    frac_1_mult = lcm_temp / fraction_1[1]
    frac_2_mult = lcm_temp / fraction_2[1]
    fraction_3 = fraction()
    fraction_3[0] = int(fraction_1[0] * frac_1_mult + fraction_2[0] * frac_2_mult)
    fraction_3[1] = lcm_temp
    return reduce(fraction_3)

def subtract_fractions_1(fraction_1, fraction_2):
    lcm_temp = lcm(fraction_1[1], fraction_2[1])
    frac_1_mult = lcm_temp / fraction_1[1]
    frac_2_mult = lcm_temp / fraction_2[1]
    fraction_2[0] = int(fraction_1[0] * frac_1_mult - fraction_2[0] * frac_2_mult)
    fraction_2[1] = lcm_temp
    reduce(fraction_2)

def subtract_fractions_2(fraction_1, fraction_2):
    lcm_temp = lcm(fraction_1[1], fraction_2[1])
    frac_1_mult = lcm_temp / fraction_1[1]
    frac_2_mult = lcm_temp / fraction_2[1]
    fraction_3 = fraction()
    fraction_3[0] = int(fraction_1[0] * frac_1_mult - fraction_2[0] * frac_2_mult)
    fraction_3[1] = lcm_temp
    return reduce(fraction_3)

def multiply_fractions_1(fraction_1, fraction_2):
    fraction_2[0] = int(fraction_1[0] * fraction_2[0])
    fraction_2[1] = int(fraction_1[1] * fraction_2[1])
    reduce(fraction_2)

def multiply_fractions_2(fraction_1, fraction_2):
    fraction_3 = fraction()
    fraction_3[0] = int(fraction_1[0] * fraction_2[0])
    fraction_3[1] = int(fraction_1[1] * fraction_2[1])
    return reduce(fraction_3)

def divide_fractions_1(fraction_1, fraction_2):
    temp = fraction_2.copy()
    fraction_2[0] = int(fraction_1[0] * temp[1])
    fraction_2[1] = int(fraction_1[1] * temp[0])
    reduce(fraction_2)

def divide_fractions_2(fraction_1, fraction_2):
    fraction_3 = fraction()
    fraction_3[0] = int(fraction_1[0] * fraction_2[1])
    fraction_3[1] = int(fraction_1[1] * fraction_2[0])
    return reduce(fraction_3)
