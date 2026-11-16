"""Compare closed Otto and Diesel cycles at common intake and peak temperatures."""

from math import isclose


def reciprocating(kind, t_intake, t_peak, compression, cv=0.718, gamma=1.4):
    """Return heat received, net work, efficiency, and MEP divided by intake pressure."""
    if kind not in ("Otto", "Diesel"):
        raise ValueError("Cycle must be Otto or Diesel")
    if not (0 < t_intake < t_peak and compression > 1 and cv > 0 and gamma > 1):
        raise ValueError("Invalid thermal or geometric inputs")
    a = gamma - 1
    t_compressed = t_intake * compression**a
    cutoff = t_peak / t_compressed if kind == "Diesel" else 1
    if t_peak <= t_compressed or cutoff >= compression:
        raise ValueError("Heat addition and expansion both require positive ranges")
    t_expanded = t_peak * (cutoff / compression) ** a
    c_heat = cv * gamma if kind == "Diesel" else cv
    heat_in = c_heat * (t_peak - t_compressed)
    work = heat_in - cv * (t_expanded - t_intake)
    gas_constant = cv * a
    mep_ratio = work / (gas_constant * t_intake * (1 - 1 / compression))
    return heat_in, work, work / heat_in, mep_ratio


if __name__ == "__main__":
    otto = reciprocating("Otto", 300, 1800, 10)
    diesel = reciprocating("Diesel", 300, 1800, 10)
    diesel_high = reciprocating("Diesel", 300, 1800, 18)
    assert isclose(otto[2], 1 - 10**-0.4)
    assert diesel[2] < otto[2] < diesel_high[2]
    for label, (q_in, work, eta, mep_ratio) in zip(("Otto r=10", "Diesel r=10", "Diesel r=18"), (otto, diesel, diesel_high)):
        print(f"{label:12}: heat={q_in:.1f}, work={work:.1f} kJ/kg, efficiency={eta:.2%}, MEP={100*mep_ratio:.1f} kPa at 100 kPa intake")
