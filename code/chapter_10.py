"""Sweep gas-turbine pressure ratio at fixed cold and hot temperatures."""

from math import isclose, sqrt


def brayton(t_cold, t_hot, ratio, eta_c=1.0, eta_t=1.0, cp=1.005, gamma=1.4):
    """Return compressor and turbine exits, net work, and thermal efficiency."""
    if not (0 < t_cold < t_hot and ratio > 1 and cp > 0 and gamma > 1):
        raise ValueError("Require a positive temperature range and pressure ratio > 1")
    if not (0 < eta_c <= 1 and 0 < eta_t <= 1):
        raise ValueError("Device efficiencies must lie in (0, 1]")
    a = (gamma - 1) / gamma
    scale = ratio**a
    t_out_c = t_cold + t_cold * (scale - 1) / eta_c
    t_out_t = t_hot - eta_t * t_hot * (1 - 1 / scale)
    heat_in = cp * (t_hot - t_out_c)
    heat_out = cp * (t_out_t - t_cold)
    work = heat_in - heat_out
    if heat_in <= 0 or work <= 0:
        raise ValueError("The specified cycle does not operate as a heat engine")
    return t_out_c, t_out_t, work, work / heat_in


if __name__ == "__main__":
    cold, hot = 300, 1500
    optimum = sqrt(hot / cold) ** (1.4 / 0.4)
    best = brayton(cold, hot, optimum)
    assert isclose(best[0], best[1])
    assert best[2] > max(brayton(cold, hot, r)[2] for r in (0.93 * optimum, 1.07 * optimum))
    real = brayton(cold, hot, 10, 0.88, 0.91)
    assert real[2] < brayton(cold, hot, 10)[2]
    print(f"Ideal max work: {best[2]:.2f} kJ/kg at pressure ratio {optimum:.3f}")
    print(f"At pressure ratio 10 with nonideal components: {real[2]:.2f} kJ/kg, {real[3]:.2%}")
