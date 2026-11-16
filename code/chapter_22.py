"""Invert the ideal-gas area–Mach relation on a specified flow branch."""

from math import isclose, sqrt


def area_ratio(mach, gamma=1.4):
    """Return A/A* for positive Mach in a calorically perfect isentrope."""
    if mach <= 0 or gamma <= 1:
        raise ValueError("Require M > 0 and gamma > 1")
    factor = (2 + (gamma - 1) * mach**2) / (gamma + 1)
    return factor ** ((gamma + 1) / (2 * (gamma - 1))) / mach


def mach_from_area(ratio, supersonic, gamma=1.4):
    """Find the selected Mach root by bisection."""
    if ratio < 1 or gamma <= 1:
        raise ValueError("Require A/A* >= 1 and gamma > 1")
    if ratio == 1:
        return 1.0

    if supersonic:
        lo, hi = 1.0, 2.0
        while area_ratio(hi, gamma) < ratio:
            hi *= 2
    else:
        lo, hi = 0.5, 1.0
        while area_ratio(lo, gamma) < ratio:
            lo /= 2

    for _ in range(70):
        mid = (lo + hi) / 2
        area_is_high = area_ratio(mid, gamma) > ratio
        if area_is_high == supersonic:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


def pressure_ratio(mach, gamma=1.4):
    """Return local static pressure divided by local stagnation pressure."""
    return (1 + (gamma - 1) * mach**2 / 2) ** (-gamma / (gamma - 1))


def sonic_flux(total_pressure, total_temperature, gamma=1.4,
               gas_constant=287.0):
    """Return choked mass flow per unit area in kg/(m² s), using Pa and K."""
    if total_pressure <= 0 or total_temperature <= 0:
        raise ValueError("Require positive total pressure and temperature")
    factor = (2 / (gamma + 1)) ** ((gamma + 1) / (2 * (gamma - 1)))
    return (
        total_pressure / sqrt(total_temperature)
        * sqrt(gamma / gas_constant) * factor
    )


def main():
    ratio = 2.0
    mach_sub = mach_from_area(ratio, False)
    mach_sup = mach_from_area(ratio, True)
    assert mach_sub < 1 < mach_sup
    assert isclose(area_ratio(mach_sub), ratio, rel_tol=1e-12)
    assert isclose(area_ratio(mach_sup), ratio, rel_tol=1e-12)
    assert mach_from_area(1, False) == mach_from_area(1, True) == 1
    print(f"Roots at A/A*=2: {mach_sub:.5f}, {mach_sup:.5f}")
    print(f"Static/total pressure on each branch: "
          f"{pressure_ratio(mach_sub):.5f}, {pressure_ratio(mach_sup):.5f}")
    print(f"Critical pressure ratio: {pressure_ratio(1):.5f}")
    print(f"Choked mass flux at 300 kPa, 300 K: "
          f"{sonic_flux(300_000, 300):.2f} kg/(m^2 s)")


if __name__ == "__main__":
    main()
