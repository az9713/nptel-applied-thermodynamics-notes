"""Solve a restricted ideal-gas mixer and the vortex-tube energy balance."""

from math import isclose, log, pi, sqrt


def check_vortex_tube():
    gas_constant = 287.0
    cp = 1.4 * gas_constant / (1.4 - 1)
    t_in, t_hot = 293.15, 389.15
    c_in, c_hot, c_cold = 1.0, 100.0, 200.0
    t_cold = 2 * t_in - t_hot
    t_cold += (c_in**2 - (c_hot**2 + c_cold**2) / 2) / cp
    energy_in = cp * t_in + c_in**2 / 2
    energy_out = cp * (t_hot + t_cold) / 2 + (c_hot**2 + c_cold**2) / 4
    assert isclose(energy_in, energy_out, rel_tol=1e-12)
    pressure_ratio = 101.3 / 1000
    generation = (
        cp * (log(t_hot / t_in) + log(t_cold / t_in)) / 2
        - gas_constant * log(pressure_ratio)
    )
    assert generation > 0
    print(f"Vortex tube cold exit: {t_cold:.2f} K, {generation:.2f} W/K generated")


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
    check_vortex_tube()


if __name__ == "__main__":
    main()
