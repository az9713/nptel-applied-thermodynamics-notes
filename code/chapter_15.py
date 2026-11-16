"""Cooling with condensate removal, followed by sensible reheat."""

from math import isclose

from chapter_14 import saturation_pressure


def humidity_ratio(temperature, pressure, relative_humidity):
    vapor_pressure = relative_humidity * saturation_pressure(temperature)
    if not 0 <= relative_humidity <= 1 or not 0 <= vapor_pressure < pressure:
        raise ValueError("Expected physical relative humidity and pressure")
    return 0.622 * vapor_pressure / (pressure - vapor_pressure)


def enthalpy(temperature, humidity):
    return 1.006 * temperature + humidity * (2501 + 1.86 * temperature)


if __name__ == "__main__":
    pressure = 101.325
    inlet, coil_exit, supply = 35.0, 15.0, 24.0
    initial_humidity = humidity_ratio(inlet, pressure, 0.80)
    final_humidity = humidity_ratio(coil_exit, pressure, 1.0)
    condensate = initial_humidity - final_humidity
    if condensate < 0:
        raise ValueError("The assumed saturated coil outlet would require adding water")
    drain_enthalpy = 4.18 * coil_exit
    coil = enthalpy(coil_exit, final_humidity) - enthalpy(inlet, initial_humidity) + condensate * drain_enthalpy
    reheat = enthalpy(supply, final_humidity) - enthalpy(coil_exit, final_humidity)
    supply_relative_humidity = saturation_pressure(coil_exit) / saturation_pressure(supply)
    print(f"Drain: {condensate:.5f} kg/kg dry air")
    print(f"Heat into air and drain at coil: {coil:.2f} kJ/kg dry air")
    print(f"Reheat: {reheat:.2f} kJ/kg dry air")
    print(f"Supply relative humidity: {supply_relative_humidity:.2%}")
    assert isclose(final_humidity + condensate, initial_humidity)
    assert isclose(
        enthalpy(inlet, initial_humidity) + coil + reheat,
        enthalpy(supply, final_humidity) + condensate * drain_enthalpy,
    )
