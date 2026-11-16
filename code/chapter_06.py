"""Check steady compressor exergy destruction by two balances."""

from math import isclose, log


def main():
    cp, r = 1.005, 0.287
    t0, p0 = 300.0, 100.0
    outlet_t, outlet_p = 450.0, 400.0
    flow, shaft_input = 0.04, 8.0
    enthalpy_delta = cp * (outlet_t - t0)
    entropy_delta = cp * log(outlet_t / t0) - r * log(outlet_p / p0)
    heat_into_device = flow * enthalpy_delta - shaft_input
    generation = flow * entropy_delta - heat_into_device / t0
    product = flow * (enthalpy_delta - t0 * entropy_delta)
    destruction = shaft_input - product
    assert isclose(destruction, t0 * generation, rel_tol=1e-12)
    assert 0 < product < shaft_input
    engine_resource = 100 * (1 - 300 / 500)
    assert isclose(30 / engine_resource, 0.75)
    print(f"Compressor exergy gain: {product:.4f} kW")
    print(f"Compressor exergy destruction: {destruction:.4f} kW")
    print(f"Compressor second-law efficiency: {product/shaft_input:.2%}")
    print(f"Heat engine second-law efficiency: {30/engine_resource:.2%}")


if __name__ == "__main__":
    main()
