"""Audit a steady vapor-compression refrigerator using supplied enthalpies."""

from math import isclose


def refrigeration(h_suction, h_discharge_s, h_liquid, efficiency, load):
    """Return fluid flow, compressor power, rejection rate and COP in kg/s and kW."""
    if not (h_discharge_s > h_suction > h_liquid and 0 < efficiency <= 1 and load > 0):
        raise ValueError("Need positive load, refrigeration effect and compression work")
    h_discharge = h_suction + (h_discharge_s - h_suction) / efficiency
    flow = load / (h_suction - h_liquid)
    power = flow * (h_discharge - h_suction)
    rejected = flow * (h_discharge - h_liquid)
    assert isclose(rejected, load + power)
    return flow, power, rejected, load / power


if __name__ == "__main__":
    base = refrigeration(395.66, 419.56, 241.72, 0.75, 10)
    subcooled = refrigeration(395.66, 419.56, 233.13, 0.75, 10)
    ideal = refrigeration(395.66, 419.56, 241.72, 1, 10)
    assert subcooled[0] < base[0] and base[-1] < subcooled[-1] < ideal[-1]
    print(f"Base: flow={base[0]:.5f} kg/s, power={base[1]:.3f} kW, heat rejected={base[2]:.3f} kW, COP={base[3]:.3f}")
    print(f"Subcooled: flow={subcooled[0]:.5f} kg/s, power={subcooled[1]:.3f} kW, COP={subcooled[3]:.3f}")
