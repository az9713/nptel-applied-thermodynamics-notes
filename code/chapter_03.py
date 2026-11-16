"""Solve the ideal-gas mixer with a specified circular outlet."""

from math import isclose, log, pi, sqrt


def main():
    cp, gas_constant = 1010.0, 287.0
    area, outlet_pressure = pi * 0.10**2 / 4, 400_000
    streams = [(6.0, 473.15, 600_000, 100), (1.0, 373.15, 500_000, 50)]
    flow = sum(mass for mass, *_ in streams)
    energy = sum(
        mass * (cp * temp + speed**2 / 2)
        for mass, temp, _, speed in streams
    ) / flow
    velocity_factor = flow * gas_constant / (outlet_pressure * area)
    root = sqrt(cp**2 + 2 * velocity_factor**2 * energy)
    temperature = 2 * energy / (cp + root)
    speed = velocity_factor * temperature
    generation = sum(
        mass * (cp * log(temperature / temp)
                - gas_constant * log(outlet_pressure / pressure))
        for mass, temp, pressure, _ in streams
    )
    density = outlet_pressure / (gas_constant * temperature)
    assert isclose(density * area * speed, flow, rel_tol=1e-12)
    assert isclose(cp * temperature + speed**2 / 2, energy, rel_tol=1e-12)
    assert generation > 0
    print(f"Outlet: {temperature:.2f} K, {speed:.2f} m/s")
    print(f"Generation: {generation:.2f} W/K")


if __name__ == "__main__":
    main()
