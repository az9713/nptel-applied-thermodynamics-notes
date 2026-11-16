"""Check entropy accounts for the ideal-gas mixer and upstream throttle."""

from math import isclose, log


CP_AIR = 1.005  # kJ/(kg K), constant teaching model
R_AIR = 0.287  # kJ/(kg K)


def entropy_change(t_initial, p_initial, t_final, p_final):
    """Return ideal-gas entropy change in kJ/(kg K); use K and kPa."""
    return CP_AIR * log(t_final / t_initial) - R_AIR * log(
        p_final / p_initial
    )


def main():
    hot_temperature, cold_temperature = 400.0, 300.0
    hot_flow, cold_flow = 1.0, 1.0  # kg/s
    chamber_pressure, upstream_pressure = 100.0, 200.0  # kPa

    outlet_flow = hot_flow + cold_flow
    outlet_temperature = (
        hot_flow * hot_temperature + cold_flow * cold_temperature
    ) / outlet_flow
    chamber_generation = hot_flow * entropy_change(
        hot_temperature, chamber_pressure, outlet_temperature,
        chamber_pressure,
    ) + cold_flow * entropy_change(
        cold_temperature, chamber_pressure, outlet_temperature,
        chamber_pressure,
    )
    throttle_generation = hot_flow * entropy_change(
        hot_temperature, upstream_pressure, hot_temperature,
        chamber_pressure,
    )
    combined_generation = hot_flow * entropy_change(
        hot_temperature, upstream_pressure, outlet_temperature,
        chamber_pressure,
    ) + cold_flow * entropy_change(
        cold_temperature, chamber_pressure, outlet_temperature,
        chamber_pressure,
    )

    thermal_enthalpy_residual = CP_AIR * (
        outlet_flow * outlet_temperature
        - hot_flow * hot_temperature - cold_flow * cold_temperature
    )
    assert isclose(thermal_enthalpy_residual, 0.0, abs_tol=1e-12)
    assert isclose(
        combined_generation, chamber_generation + throttle_generation,
        rel_tol=1e-12,
    )
    assert 0 < chamber_generation < combined_generation
    assert entropy_change(350.0, 100.0, 350.0, 100.0) == 0

    print(f"Outlet temperature: {outlet_temperature:.1f} K")
    print(f"Mixer entropy generation: {chamber_generation:.5f} kW/K")
    print(f"Throttle entropy generation: {throttle_generation:.5f} kW/K")
    print(f"Combined entropy generation: {combined_generation:.5f} kW/K")


if __name__ == "__main__":
    main()
