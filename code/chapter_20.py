"""Compute local acoustic and stagnation quantities for an ideal gas."""

from math import isclose, sqrt


def stagnation(temperature, pressure, speed, gamma=1.4, gas_constant=287.0):
    """Return acoustic speed, Mach number, total temperature and pressure.

    Inputs use K, Pa, m/s and J/(kg K). The returned pressure is in Pa.
    The gas is calorically perfect and the hypothetical stop is isentropic.
    """
    if temperature <= 0 or pressure <= 0 or gamma <= 1 or gas_constant <= 0:
        raise ValueError("Require positive T, p, R, and gamma > 1")
    sound_speed = sqrt(gamma * gas_constant * temperature)
    mach = abs(speed) / sound_speed
    temperature_ratio = 1 + (gamma - 1) * mach**2 / 2
    return (
        sound_speed, mach, temperature * temperature_ratio,
        pressure * temperature_ratio ** (gamma / (gamma - 1))
    )


def main():
    a, mach, total_t, total_p = stagnation(300.0, 100_000.0, 250.0)
    cp = 1.4 * 287.0 / (1.4 - 1)
    assert isclose(cp * (total_t - 300.0), 250.0**2 / 2)
    assert stagnation(300.0, 100_000.0, 0)[1:] == (0, 300, 100_000)
    assert stagnation(300.0, 100_000.0, -250.0)[1:] == (
        mach, total_t, total_p
    )
    print(f"Sound speed: {a:.2f} m/s; Mach: {mach:.4f}")
    print(f"Stagnation state: {total_t:.2f} K, {total_p/1000:.2f} kPa")
    _, m2, t2, p2 = stagnation(300.0, 100_000.0, 150.0)
    print(f"Moving observer: Mach {m2:.4f}, {t2:.2f} K, {p2/1000:.2f} kPa")


if __name__ == "__main__":
    main()
