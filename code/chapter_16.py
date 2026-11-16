"""Duct flow, trial saturation state and dry-coil heat duty."""

from math import pi

from chapter_14 import dew_point, saturation_pressure
from chapter_15 import enthalpy, humidity_ratio


if __name__ == "__main__":
    inlet, outlet, minimum_coil_temperature, trial_condensing_outlet = 30.0, 25.0, 20.0, 5.0
    pressure, relative_humidity = 100.0, 0.30
    diameter, speed = 0.50, 18.0
    volume_flow = pi * diameter**2 * speed / 4
    initial_humidity = humidity_ratio(inlet, pressure, relative_humidity)
    vapor_pressure = relative_humidity * saturation_pressure(inlet)
    specific_volume = 0.287 * (inlet + 273.15) / (pressure - vapor_pressure)
    dry_air_flow = volume_flow / specific_volume
    outlet_relative_humidity = vapor_pressure / saturation_pressure(outlet)
    if minimum_coil_temperature < dew_point(vapor_pressure) or outlet_relative_humidity > 1:
        raise ValueError("Trial coil may condense water; use a wet-coil balance")
    duty = dry_air_flow * (enthalpy(outlet, initial_humidity) - enthalpy(inlet, initial_humidity))
    condensing_humidity = humidity_ratio(trial_condensing_outlet, pressure, 1.0)
    print(f"Dry-air flow: {dry_air_flow:.3f} kg/s")
    print(f"Trial outlet relative humidity: {outlet_relative_humidity:.2%}")
    print(f"Heat into dry coil control volume: {duty:.2f} kW")
    print(f"Condensate if cooled to 5 °C: {dry_air_flow * (initial_humidity - condensing_humidity):.4f} kg/s")
    assert condensing_humidity < initial_humidity < humidity_ratio(outlet, pressure, 1.0)
    assert duty < 0
