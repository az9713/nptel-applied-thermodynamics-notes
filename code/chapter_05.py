"""Compute closed-system physical exergy for simple teaching models."""

from math import isclose, log, log1p


def thermal_exergy(heat_capacity, temperature, ambient):
    """Use total heat capacity in kJ/K and absolute temperatures in K."""
    relative_gap = (temperature - ambient) / ambient
    return heat_capacity * ambient * (relative_gap - log1p(relative_gap))


def pressure_exergy(mass, gas_constant, temperature, pressure, ambient):
    """Compute physical exergy of ideal gas at ambient temperature."""
    ratio = pressure / ambient
    return mass * gas_constant * temperature * (log(ratio) + 1 / ratio - 1)


def main():
    hot = thermal_exergy(4.18, 350.0, 300.0)
    cold = thermal_exergy(4.18, 250.0, 300.0)
    assert cold > hot > 0
    assert thermal_exergy(4.18, 300.0, 300.0) == 0
    reduced = pressure_exergy(1.0, 0.287, 300.0, 200.0, 100.0)
    volume_change = 0.287 * 300 * (1 / 200 - 1 / 100)
    entropy_change = -0.287 * log(2)
    assert isclose(reduced, 100 * volume_change - 300 * entropy_change)
    print(f"Thermal availability: hot {hot:.3f} kJ, cold {cold:.3f} kJ")
    print(f"Compressed 1 kg ideal air: {reduced:.3f} kJ")


if __name__ == "__main__":
    main()
