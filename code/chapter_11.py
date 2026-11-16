"""Compute a two-stage ideal Brayton cycle with optional heat recovery."""

from math import isclose


def modified_brayton(cold, hot, ratio, epsilon, cp=1.005, gamma=1.4):
    """Return net work, external heat supplied, recovered heat and efficiency."""
    if not (0 < cold < hot and ratio > 1 and 0 <= epsilon <= 1 and cp > 0 and gamma > 1):
        raise ValueError("Invalid temperatures, pressure ratio, effectiveness or gas properties")
    stage_scale = ratio ** ((gamma - 1) / (2 * gamma))
    after_compression = cold * stage_scale
    after_expansion = hot / stage_scale
    recovered = epsilon * cp * max(0, after_expansion - after_compression)
    heat_in = cp * (hot - after_compression + hot - after_expansion) - recovered
    heat_out = cp * (after_compression - cold + after_expansion - cold) - recovered
    net_work = 2 * cp * ((hot - after_expansion) - (after_compression - cold))
    if heat_in <= 0 or net_work <= 0:
        raise ValueError("No positive power-cycle solution")
    assert isclose(heat_in - heat_out, net_work)
    return net_work, heat_in, recovered, net_work / heat_in


if __name__ == "__main__":
    for epsilon in (0, 0.4, 0.8):
        net, heat, recovery, efficiency = modified_brayton(300, 1500, 10, epsilon)
        print(f"Effectiveness {epsilon:.1f}: work={net:.1f}, heat={heat:.1f}, recovered={recovery:.1f} kJ/kg, efficiency={efficiency:.2%}")
    off = modified_brayton(300, 1500, 10, 0)
    on = modified_brayton(300, 1500, 10, 0.8)
    assert isclose(off[0], on[0]) and isclose(off[1] - on[1], on[2])
    assert on[-1] > off[-1]
