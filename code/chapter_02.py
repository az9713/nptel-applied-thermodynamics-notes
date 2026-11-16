"""Compare reversible ideal-gas compression paths at fixed end pressures."""

from math import isclose, log


def compressor_paths(t_in, pressure_ratio, gas_constant, cp):
    """Return (isothermal input, isentropic input, isentropic outlet T).

    Temperatures are in kelvin and work and heat capacities are mass specific,
    using kJ/kg and kJ/(kg K). Work input is reported as a positive magnitude.
    The gas is ideal with constant cp, and both paths are internally reversible.
    """
    if t_in <= 0 or pressure_ratio < 1 or not 0 < gas_constant < cp:
        raise ValueError("Require T > 0, pressure ratio >= 1, and cp > R > 0")
    t_out_s = t_in * pressure_ratio ** (gas_constant / cp)
    isothermal = gas_constant * t_in * log(pressure_ratio)
    isentropic = cp * (t_out_s - t_in)
    return isothermal, isentropic, t_out_s


def main():
    t_in, pressure_ratio, gas_constant, cp = 300, 8, 0.287, 1.005
    isothermal, isentropic, t_out_s = compressor_paths(
        t_in, pressure_ratio, gas_constant, cp
    )
    entropy_rise = cp * log(t_out_s / t_in)
    entropy_rise -= gas_constant * log(pressure_ratio)
    assert isclose(entropy_rise, 0, abs_tol=1e-12)
    assert 0 < isothermal < isentropic
    assert compressor_paths(t_in, 1, gas_constant, cp) == (0, 0, t_in)
    print(f"Isothermal shaft input: {isothermal:.2f} kJ/kg")
    print(f"Isentropic shaft input: {isentropic:.2f} kJ/kg")
    print(f"Isentropic outlet temperature: {t_out_s:.2f} K")


if __name__ == "__main__":
    main()
