"""Check exergy accounts for a two-stream exchanger and freezing."""

from math import isclose, log


def main():
    hot_capacity_rate, cold_capacity_rate = 1.9, 2.1
    hot_in, cold_in, cold_out = 520.0, 300.0, 390.0
    ambient = 300.0
    heating_rate = cold_capacity_rate * (cold_out - cold_in)
    hot_out = hot_in - heating_rate / hot_capacity_rate
    assert hot_in > cold_out and hot_out > cold_in
    hot_entropy = hot_capacity_rate * log(hot_out / hot_in)
    cold_entropy = cold_capacity_rate * log(cold_out / cold_in)
    hot_resource = heating_rate + ambient * hot_entropy
    cold_product = heating_rate - ambient * cold_entropy
    destruction = ambient * (hot_entropy + cold_entropy)
    assert 0 < cold_product < hot_resource
    assert isclose(hot_resource - cold_product, destruction)

    fusion_heat, freezing_temperature = 334.0, 273.15
    exergy_gain = -fusion_heat + ambient * fusion_heat / freezing_temperature
    assert exergy_gain > 0
    print(f"Heat exchanger hot outlet: {hot_out:.2f} K")
    print(f"Heat exchanger destruction: {destruction:.3f} kW")
    print(f"Freezing exergy gain: {exergy_gain:.3f} kJ/kg")


if __name__ == "__main__":
    main()
