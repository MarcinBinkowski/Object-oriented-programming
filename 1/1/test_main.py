from main import *


def test_addition():
    assert add_fractions_2([1, 2], [3, 5]) == [11, 10]
    assert add_fractions_2([123123, 41241243], [-1234124, 1243124]) == [-4228645884990, 4272331580261]

    fraction_1 = fraction(123123, 41241243)
    fraction_2 = fraction(-1234124, 1243124)
    add_fractions_1(fraction_1, fraction_2)

    assert fraction_2 == [-4228645884990, 4272331580261]


def test_subtraction():
    assert subtract_fractions_2([1, 2], [3, 5]) == [-1, 10]
    assert subtract_fractions_2([123123, 41241243], [-1234124, 1243124]) == [4254155411032, 4272331580261]

    fraction_1 = fraction(123123, 41241243)
    fraction_2 = fraction(-1234124, 1243124)
    subtract_fractions_1(fraction_1, fraction_2)

    assert fraction_2 == [4254155411032, 4272331580261]


def test_multiplication():
    assert multiply_fractions_2([1, 2], [3, 5]) == [3, 10]
    assert multiply_fractions_2([123123, 41241243], [-1234124, 1243124]) == [-12662420771, 4272331580261]

    fraction_1 = fraction(123123, 41241243)
    fraction_2 = fraction(-1234124, 1243124)
    multiply_fractions_1(fraction_1, fraction_2)

    assert fraction_2 == [-12662420771, 4272331580261]


def test_division():
    assert divide_fractions_2([1, 2], [3, 5]) == [5, 6]
    assert divide_fractions_2([123123, 41241243], [-1234124, 1243124]) == [-12754763021, 4241400648011]

    fraction_1 = fraction(123123, 41241243)
    fraction_2 = fraction(-1234124, 1243124)
    divide_fractions_1(fraction_1, fraction_2)

    assert fraction_2 == [-12754763021, 4241400648011]

test_addition()
test_subtraction()
test_multiplication()
test_division()