"""Moist-air state and condensate in a sealed tank, in kPa, kg, m³ and °C."""

from math import exp, isclose


def saturation_pressure(temperature_c):
    """IAPWS SR1-86(1992) saturation pressure above liquid water, in kPa."""
    temperature = temperature_c + 273.15
    critical = 647.096
    if not 0.01 <= temperature_c <= critical - 273.15:
        raise ValueError("Temperature outside the liquid-vapor saturation curve")
    theta = 1 - temperature / critical
    coefficients = (-7.85951783, 1.84408259, -11.7866497, 22.6807411, -15.9618719, 1.80122502)
    powers = (1, 1.5, 3, 3.5, 4, 7.5)
    logarithm = (critical / temperature) * sum(
        coefficient * theta**power for coefficient, power in zip(coefficients, powers)
    )
    return 22064 * exp(logarithm)


def dew_point(vapor_pressure):
    low, high = 0.01, 60.0
    if not saturation_pressure(low) <= vapor_pressure <= saturation_pressure(high):
        raise ValueError("Vapor pressure outside this ambient-range dew-point calculation")
    for _ in range(50):
        middle = (low + high) / 2
        if saturation_pressure(middle) < vapor_pressure:
            low = middle
        else:
            high = middle
    return (low + high) / 2


if __name__ == "__main__":
    gas_constant_vapor = 0.4615
    pressure, initial, final, relative_humidity, volume = 101.325, 30.0, 10.0, 0.50, 1.0
    vapor_pressure = relative_humidity * saturation_pressure(initial)
    humidity = 0.622 * vapor_pressure / (pressure - vapor_pressure)
    dew = dew_point(vapor_pressure)
    initial_vapor = vapor_pressure * volume / (gas_constant_vapor * (initial + 273.15))
    final_saturated_vapor = saturation_pressure(final) * volume / (gas_constant_vapor * (final + 273.15))
    final_vapor = min(initial_vapor, final_saturated_vapor)
    condensate = initial_vapor - final_vapor

    print(f"Humidity ratio: {humidity:.5f} kg/kg dry air")
    print(f"Constant-pressure dew point: {dew:.2f} °C")
    print(f"Rigid-tank condensate: {condensate * 1000:.2f} g")
    assert isclose(saturation_pressure(dew), vapor_pressure, rel_tol=1e-12)
    assert isclose(final_vapor + condensate, initial_vapor, rel_tol=1e-12)
    assert 18 < dew < 19 and 0.005 < condensate < 0.006
