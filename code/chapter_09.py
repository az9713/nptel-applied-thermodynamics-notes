"""Audit a Rankine cycle from a consistent set of specific enthalpies."""

from math import isclose


def rankine(h_liquid, h_pump_out, h_turbine_in, h_turbine_out):
    """Return positive net work, boiler heat and efficiency using kJ/kg throughout."""
    if not h_liquid < h_pump_out < h_turbine_in or not h_liquid < h_turbine_out < h_turbine_in:
        raise ValueError("Expected physically ordered Rankine enthalpies")
    work = (h_turbine_in - h_turbine_out) - (h_pump_out - h_liquid)
    if work <= 0:
        raise ValueError("Expansion must deliver more work than pumping consumes")
    heat_in = h_turbine_in - h_pump_out
    heat_out = h_turbine_out - h_liquid
    assert isclose(work, heat_in - heat_out)
    return work, heat_in, work / heat_in


def feedwater_bleed(h_cold, h_mixed, h_bleed):
    """Return extracted vapor mass per unit mass leaving an open feedwater heater."""
    if not h_cold < h_mixed < h_bleed:
        raise ValueError("Expected cold < mixed < bleed enthalpy")
    return (h_mixed - h_cold) / (h_bleed - h_cold)


if __name__ == "__main__":
    net, heat, efficiency = rankine(191.81, 199.87, 3349.53, 2109.33)
    bleed = feedwater_bleed(192.31, 640.09, 2650.0)
    assert isclose((1 - bleed) * 192.31 + bleed * 2650.0, 640.09)
    assert 0 < efficiency < 1
    try:
        rankine(0, 200, 250, 249)
    except ValueError:
        pass
    else:
        raise AssertionError("Rejected heat exceeds added heat in the negative-work case")
    print(f"Net output {net:.2f} kJ/kg; input {heat:.2f} kJ/kg; efficiency {efficiency:.2%}")
    print(f"Example open-heater bleed fraction: {bleed:.2%}")
