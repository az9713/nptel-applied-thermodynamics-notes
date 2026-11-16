"""Check the adiabatic diffuser and heated tank balances."""

from math import isclose, log, sqrt


def main():
    cp, r = 1005.0, 287.0
    t_in, t_out = 330.15, 342.15
    p_in, p_out = 100.0, 113.0
    c_in = 200.0
    c_out = sqrt(c_in**2 - 2 * cp * (t_out - t_in))
    area_ratio = c_in / c_out * p_in * t_out / (p_out * t_in)
    delta_s = cp * log(t_out / t_in) - r * log(p_out / p_in)
    assert isclose(cp * (t_out - t_in), (c_in**2 - c_out**2) / 2)
    assert isclose(p_out * c_out / t_out * area_ratio,
                   p_in * c_in / t_in)
    assert delta_s >= 0
    generation = 5.0 * (500.0 - 200.0) / 330.15
    assert isclose(generation * 330.15, 1500.0)
    print(f"Diffuser: {c_out:.3f} m/s, area ratio {area_ratio:.4f}")
    print(f"Specific generation: {delta_s:.4f} J/(kg K)")
    print(f"Tank generation: {generation:.4f} kJ/K")


if __name__ == "__main__":
    main()
