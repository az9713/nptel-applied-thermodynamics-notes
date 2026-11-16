"""Methane atom balances, exhaust composition and reference heating values."""

from math import isclose


def methane_heating_values():
    """Positive heat release, kJ/mol fuel, at 298.15 K."""
    methane, carbon_dioxide = -74.87, -393.51
    water_vapor, liquid_water = -241.826, -285.830
    lhv = methane - (carbon_dioxide + 2 * water_vapor)
    hhv = methane - (carbon_dioxide + 2 * liquid_water)
    return lhv, hhv


def methane_products(air_ratio):
    if air_ratio < 1:
        raise ValueError("Complete methane oxidation requires at least stoichiometric air")
    return {"CO2": 1.0, "H2O": 2.0, "O2": 2 * (air_ratio - 1), "N2": 7.52 * air_ratio}


if __name__ == "__main__":
    air_ratio = 1.20
    products = methane_products(air_ratio)
    wet_total = sum(products.values())
    dry_total = wet_total - products["H2O"]
    lhv, hhv = methane_heating_values()
    print(f"Dry exhaust oxygen: {products['O2'] / dry_total:.2%}")
    print(f"Wet exhaust oxygen: {products['O2'] / wet_total:.2%}")
    print(f"Reference methane LHV: {lhv:.3f} kJ/mol")
    print(f"Reference methane HHV: {hhv:.3f} kJ/mol")
    assert isclose(products["CO2"], 1)
    assert isclose(2 * products["H2O"], 4)
    assert isclose(2 * products["CO2"] + products["H2O"] + 2 * products["O2"], 4 * air_ratio)
    assert isclose(products["N2"], 3.76 * 2 * air_ratio)
    assert isclose(hhv - lhv, 2 * (285.830 - 241.826))
