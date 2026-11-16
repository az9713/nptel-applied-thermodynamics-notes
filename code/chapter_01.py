"""Check the mixer, upstream throttle, and saturated-liquid discharge."""

from math import isclose, log


CP_AIR = 1.005  # kJ/(kg K), constant teaching model
R_AIR = 0.287  # kJ/(kg K)


def entropy_change(t_initial, p_initial, t_final, p_final):
    """Return ideal-gas entropy change in kJ/(kg K); use K and kPa."""
    return CP_AIR * log(t_final / t_initial) - R_AIR * log(
        p_final / p_initial
    )


def check_draining_tank():
    pressure = 2000.0  # kPa
    tank_volume, initial_mass, reservoir_temperature = 0.600, 8.0, 523.15
    # IF97 saturation properties at 2 MPa, with h in kJ/kg and v in m³/kg.
    v_f, v_g = 0.00117675024425, 0.09958054416890
    h_f, h_g, t_sat = 908.62185113646, 2798.38414024152, 485.53453531849
    x_initial = (tank_volume / initial_mass - v_f) / (v_g - v_f)
    final_mass = tank_volume / v_g
    vapor_gain = initial_mass * (1 - x_initial) * v_f / v_g
    heat = vapor_gain * (h_g - h_f)
    u_initial = h_f + x_initial * (h_g - h_f)
    u_initial -= pressure * tank_volume / initial_mass
    u_final = h_g - pressure * v_g
    outflow = initial_mass - final_mass
    full_balance = final_mass * u_final - initial_mass * u_initial
    full_balance += outflow * h_f
    assert isclose(heat, full_balance, rel_tol=1e-10)
    generation = heat * (1 / t_sat - 1 / reservoir_temperature)
    assert 0 < generation
    print(f"Draining tank: {outflow:.5f} kg out, {heat:.2f} kJ in, "
          f"{1000 * generation:.2f} J/K generated")


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
    check_draining_tank()


if __name__ == "__main__":
    main()
