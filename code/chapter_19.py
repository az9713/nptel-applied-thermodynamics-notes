"""Frozen flame temperature and ideal oxygen equilibrium screening models."""

from math import isclose, sqrt

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
