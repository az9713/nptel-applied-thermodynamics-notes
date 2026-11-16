"""Frozen flame temperature and ideal oxygen equilibrium screening models."""

from math import exp, isclose, sqrt

from chapter_17 import methane_heating_values, methane_products


def frozen_temperature(air_ratio):
    heat_capacities = {"CO2": 0.054, "H2O": 0.044, "N2": 0.034, "O2": 0.035}
    products = methane_products(air_ratio)
    product_capacity = sum(products[name] * value for name, value in heat_capacities.items())
    lhv, _ = methane_heating_values()
    temperature = 298.15 + lhv / product_capacity
    residual = product_capacity * (temperature - 298.15) - lhv
    return temperature, residual


def dissociated_fraction(equilibrium_constant, pressure_ratio):
    if equilibrium_constant < 0 or pressure_ratio <= 0:
        raise ValueError("Expected nonnegative equilibrium constant and positive pressure ratio")
    return sqrt(equilibrium_constant / (4 * pressure_ratio + equilibrium_constant))


if __name__ == "__main__":
    stoichiometric, residual_st = frozen_temperature(1)
    lean, residual_lean = frozen_temperature(1.5)
    kp = 0.0126
    low_pressure = dissociated_fraction(kp, 1)
    high_pressure = dissociated_fraction(kp, 2)
    print(f"Frozen methane flame temperatures: {stoichiometric:.1f}, {lean:.1f} K")
    print(f"O2 fraction dissociated at p° and 2p°: {low_pressure:.3%}, {high_pressure:.3%}")
    assert stoichiometric > lean
    assert isclose(residual_st, 0, abs_tol=1e-10)
    assert isclose(residual_lean, 0, abs_tol=1e-10)
    assert high_pressure < low_pressure
    assert isclose(4 * low_pressure**2 / (1 - low_pressure**2), kp)

    oxygen = 15.5 / 1.25
    kp_shift = exp(-30.260 / (0.008314 * 2200))
    # With b moles CO, the atom balances give CO2=10-b,
    # H2O=4.8+b, and H2=6.2-b. Use the smaller quadratic root.
    linear = 16.2 + 4.8 * kp_shift
    constant = 62.0
    discriminant = linear**2 - 4 * (1 - kp_shift) * constant
    co = 2 * constant / (linear + sqrt(discriminant))
    co2, water, hydrogen = 10 - co, 4.8 + co, 6.2 - co
    assert 0 < co < 6.2
    assert isclose(co2 * hydrogen / (co * water), kp_shift)
    assert isclose(co + co2, 10)
    assert isclose(2 * (water + hydrogen), 22)
    assert isclose(co + 2 * co2 + water, 2 * oxygen)
    print(f"Rich decane CO, CO2, H2O, H2: {co:.4f}, {co2:.4f}, "
          f"{water:.4f}, {hydrogen:.4f} mol per mol fuel")
