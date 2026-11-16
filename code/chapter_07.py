"""Check closed-system exergy for compression and thermal equilibration."""

from math import isclose, log


def main():
    r, gamma = 0.287, 1.4
    cv = r / (gamma - 1)
    cp = cv + r
    p0, t0 = 100.0, 298.15
    p1, t1, volume1 = p0, t0, 0.002
    p2, t2, useful_input = 600.0, 423.15, 1.2
    mass = p1 * volume1 / (r * t1)
    volume2 = mass * r * t2 / p2
    delta_u = mass * cv * (t2 - t1)
    delta_s = mass * (cp * log(t2 / t1) - r * log(p2 / p1))
    delta_b = delta_u + p0 * (volume2 - volume1) - t0 * delta_s
    destruction = useful_input - delta_b
    assert 0 < delta_b < useful_input

    capacity_hot, capacity_cold = 24.0, 418.0
    t_hot, t_cold, work = 358.15, 293.15, 240.0
    final = (
        capacity_hot * t_hot + capacity_cold * t_cold + work
    ) / (capacity_hot + capacity_cold)
    assert isclose(capacity_hot * (final - t_hot)
                   + capacity_cold * (final - t_cold), work)
    generation = capacity_hot * log(final / t_hot)
    generation += capacity_cold * log(final / t_cold)
    assert generation > 0
    print(f"Compression exergy change: {delta_b:.4f} kJ")
    print(f"Compression destruction: {destruction:.4f} kJ")
    print(f"Stirred tank: {final:.3f} K, {generation:.5f} kJ/K")


if __name__ == "__main__":
    main()
