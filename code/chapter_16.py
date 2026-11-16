"""Dry-coil outlet and wet-tower make-up from psychrometric balances."""

from math import isclose, pi

from chapter_14 import dew_point, saturation_pressure
from chapter_15 import enthalpy, humidity_ratio


if __name__ == "__main__":
    inlet, minimum_coil_temperature, trial_condensing_outlet = 30.0, 20.0, 5.0
    pressure, relative_humidity = 100.0, 0.30
    diameter, speed = 0.50, 18.0
    volume_flow = pi * diameter**2 * speed / 4
    initial_humidity = humidity_ratio(inlet, pressure, relative_humidity)
    vapor_pressure = relative_humidity * saturation_pressure(inlet)
    specific_volume = 0.287 * (inlet + 273.15) / (pressure - vapor_pressure)
    dry_air_flow = volume_flow / specific_volume
    duty = -1227.0 / 60
    heat_capacity = enthalpy(inlet + 1, initial_humidity) - enthalpy(inlet, initial_humidity)
    outlet = inlet + duty / (dry_air_flow * heat_capacity)
    outlet_relative_humidity = vapor_pressure / saturation_pressure(outlet)
    if minimum_coil_temperature < dew_point(vapor_pressure) or outlet_relative_humidity > 1:
        raise ValueError("Trial coil may condense water; use a wet-coil balance")
    condensing_humidity = humidity_ratio(trial_condensing_outlet, pressure, 1.0)
    print(f"Dry-air flow: {dry_air_flow:.3f} kg/s")
    print(f"Trial outlet temperature: {outlet:.2f} °C")
    print(f"Trial outlet relative humidity: {outlet_relative_humidity:.2%}")
    print(f"Heat into dry coil control volume: {duty:.2f} kW")
    print(f"Condensate if cooled to 5 °C: {dry_air_flow * (initial_humidity - condensing_humidity):.4f} kg/s")
    assert condensing_humidity < initial_humidity < humidity_ratio(outlet, pressure, 1.0)
    assert isclose(duty, dry_air_flow * (enthalpy(outlet, initial_humidity) - enthalpy(inlet, initial_humidity)))

    ambient_humidity = humidity_ratio(23, 101.325, 0.60)
    exhaust_humidity = humidity_ratio(32, 101.325, 1.0)
    tower_humidity_rise = exhaust_humidity - ambient_humidity
    tower_enthalpy_rise = enthalpy(32, exhaust_humidity) - enthalpy(23, ambient_humidity)
    makeup_enthalpy = 4.18 * 25
    water_cooling = 90 * 4.18 * (40 - 25)
    tower_dry_air_flow = water_cooling / (tower_enthalpy_rise - tower_humidity_rise * makeup_enthalpy)
    makeup = tower_dry_air_flow * tower_humidity_rise
    print(f"Wet-tower dry-air flow: {tower_dry_air_flow:.1f} kg/s")
    print(f"Wet-tower make-up: {makeup:.2f} kg/s")
    assert isclose(tower_dry_air_flow * tower_enthalpy_rise, water_cooling + makeup * makeup_enthalpy)
