"""Locate an ideal internal shock and compare two steam nozzle back pressures."""

from math import isclose, sqrt

from chapter_21 import normal_shock
from chapter_22 import mach_from_area, pressure_ratio, sonic_flux


def trial_shock(area_to_throat, exit_to_throat, gamma=1.4):
    """Return exit p/p_t1, exit Mach and upstream Mach at a trial shock."""
    if not 1 <= area_to_throat <= exit_to_throat:
        raise ValueError("Shock must lie between the throat and exit")
    mach_a = mach_from_area(area_to_throat, True, gamma)
    shock = normal_shock(mach_a, gamma)
    total_ratio = shock[-1]
    mach_exit = mach_from_area(max(1.0, exit_to_throat * total_ratio),
                               False, gamma)
    return total_ratio * pressure_ratio(mach_exit, gamma), mach_exit, mach_a


def locate_shock(back_to_total, exit_to_throat, gamma=1.4):
    """Invert the post-shock exit pressure for a single interior normal shock."""
    lo, hi = 1.0, exit_to_throat
    high_back = trial_shock(lo, exit_to_throat, gamma)[0]
    low_back = trial_shock(hi, exit_to_throat, gamma)[0]
    if not low_back < back_to_total < high_back:
        raise ValueError("Back pressure does not select an interior shock")
    for _ in range(60):
        mid = (lo + hi) / 2
        if trial_shock(mid, exit_to_throat, gamma)[0] > back_to_total:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def steam_exit(p_total, v_total, exponent, throat_area, p_back):
    """Power-law steam expansion, p in Pa and v in m³/kg."""
    if not (0 < p_back <= p_total and v_total > 0 and exponent > 1
            and throat_area > 0):
        raise ValueError("Inputs outside the pressure or steam model domain")
    ratio_star = (2 / (exponent + 1)) ** (exponent / (exponent - 1))
    ratio = max(p_back / p_total, ratio_star)
    v = v_total * ratio ** (-1 / exponent)
    delta_h = exponent / (exponent - 1) * p_total * v_total * (
        1 - ratio ** ((exponent - 1) / exponent)
    )
    speed = sqrt(2 * delta_h)
    return p_total * ratio, speed, throat_area * speed / v


def main():
    area_ratio = 3.5
    mach_sup = mach_from_area(area_ratio, True)
    p_sup = pressure_ratio(mach_sup)
    p_shock_exit = trial_shock(area_ratio, area_ratio)[0]
    p_choke = trial_shock(1, area_ratio)[0]
    assert 0.02 < p_sup < p_shock_exit < 0.5 < p_choke
    a_shock = locate_shock(0.5, area_ratio)
    ratio, mach_exit, mach_a = trial_shock(a_shock, area_ratio)
    assert isclose(ratio, 0.5, rel_tol=1e-12)
    gamma, gas_constant, total_temperature = 1.4, 287.0, 500.0
    exit_pressure = 500_000.0
    exit_flux = sonic_flux(1_000_000, total_temperature) / area_ratio
    # Infer exit Mach independently from known exit pressure and mass flux.
    scale = (exit_flux / exit_pressure)**2 * gas_constant * total_temperature / gamma
    direct_mach = sqrt(2 * scale / (1 + sqrt(1 + 2 * (gamma - 1) * scale)))
    assert isclose(direct_mach, mach_exit, rel_tol=1e-12)
    print(f"Isentropic supersonic exit: M={mach_sup:.4f}, p/p_t={p_sup:.5f}")
    print(f"Shock at exit: p_b/p_t={p_shock_exit:.5f}; "
          f"first choking: {p_choke:.5f}")
    print(f"Internal shock: A/A_t={a_shock:.4f}, "
          f"M_up={mach_a:.4f}, exit M={mach_exit:.4f}")
    for p_back in (400_000, 300_000, 200_000):
        p, u, mdot = steam_exit(600_000, 0.2845, 1.125, 0.002, p_back)
        print(f"Steam at p_b={p_back/1000:.0f} kPa: "
              f"p_e={p/1000:.2f} kPa, u_e={u:.2f} m/s, m_dot={mdot:.4f} kg/s")
    assert steam_exit(600_000, 0.2845, 1.125, 0.002, 300_000) == (
        steam_exit(600_000, 0.2845, 1.125, 0.002, 200_000)
    )


if __name__ == "__main__":
    main()
