"""Restricted rich ethanol products and an inverse dry-exhaust calculation."""

from math import isclose


def rich_ethanol_products(equivalence_ratio):
    if not 1 <= equivalence_ratio <= 1.5:
        raise ValueError("The restricted products are valid only for 1 <= phi <= 1.5")
    oxygen = 3 / equivalence_ratio
    carbon_dioxide = 2 * oxygen - 4
    return oxygen, carbon_dioxide, 2 - carbon_dioxide, 3, 3.76 * oxygen


if __name__ == "__main__":
    oxygen, co2, co, water, nitrogen = rich_ethanol_products(1.10)
    print(f"Rich ethanol CO2, CO, H2O, N2: {co2:.5f}, {co:.5f}, {water:.5f}, {nitrogen:.5f} mol")
    print(f"Rich ethanol exhaust dry CO: {co / (co2 + co + nitrogen):.2%}")
    assert isclose(co2 + co, 2)
    assert isclose(2 * water, 6)
    assert isclose(2 * co2 + co + water, 1 + 2 * oxygen)
    assert isclose(nitrogen, 3.76 * oxygen)
    assert isclose(rich_ethanol_products(1.5)[1], 0, abs_tol=1e-12)

    stoichiometric = 15.5
    dry_co2, dry_oxygen = 0.12043, 0.03733
    supplied_oxygen = stoichiometric + 10 * dry_oxygen / dry_co2
    excess_air = supplied_oxygen / stoichiometric - 1
    air_mass_ratio = supplied_oxygen * (31.998 + 3.76 * 28.014) / 142.286
    print(f"Inverse decane excess air: {excess_air:.2%}")
    print(f"Actual decane air-fuel ratio: {air_mass_ratio:.2f} kg/kg")
    predicted_dry_total = 10 + supplied_oxygen - stoichiometric + 3.76 * supplied_oxygen
    assert isclose(10 / predicted_dry_total, dry_co2, rel_tol=1e-4)
