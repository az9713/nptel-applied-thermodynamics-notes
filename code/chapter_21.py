"""Calorically perfect normal shock and conservation checks."""

from math import isclose, log, sqrt


def normal_shock(mach_upstream, gamma=1.4):
    """Return downstream Mach and downstream/upstream p, rho, T and p_t."""
    if mach_upstream < 1 or gamma <= 1:
        raise ValueError("Require M >= 1 and gamma > 1")
    mach_sq = mach_upstream**2
    pressure_ratio = 1 + 2 * gamma / (gamma + 1) * (mach_sq - 1)
    density_ratio = (gamma + 1) * mach_sq / ((gamma - 1) * mach_sq + 2)
    temperature_ratio = pressure_ratio / density_ratio
    mach_downstream = mach_upstream / density_ratio / sqrt(temperature_ratio)
    factor = (gamma - 1) / 2
    total_ratio = pressure_ratio * (
        (1 + factor * mach_downstream**2) / (1 + factor * mach_sq)
    ) ** (gamma / (gamma - 1))
    return (
        mach_downstream, pressure_ratio, density_ratio, temperature_ratio,
        total_ratio
    )


def main():
    gamma, gas_constant, mach = 1.4, 287.0, 2.0
    mach2, p2, rho2, t2, pt2 = normal_shock(mach, gamma)
    assert normal_shock(1, gamma) == (1, 1, 1, 1, 1)
    assert isclose(1 + gamma * mach**2, p2 * (1 + gamma * mach2**2))
    assert isclose(1 + (gamma - 1) / 2 * mach**2,
                   t2 * (1 + (gamma - 1) / 2 * mach2**2))
    assert 0 < pt2 < 1
    print(f"M2={mach2:.5f}, p2/p1={p2:.5f}, rho2/rho1={rho2:.5f}")
    print(f"T2/T1={t2:.5f}, pt2/pt1={pt2:.5f}")
    print(f"Entropy increase: {-gas_constant * log(pt2):.2f} J/(kg K)")


if __name__ == "__main__":
    main()
