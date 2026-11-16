---
title: Psychrometric Paths
lectures: 73, 44–45
summary: Read a pressure-specific chart and use water and energy balances for cooling, reheating, mixing, drying, and towers.
source: https://www.youtube.com/watch?v=IVz3N68fF1c
---

A cooling coil can meet a supply-air moisture target at a temperature below the delivery target. A reheater then raises the temperature at unchanged humidity ratio. The coil, drain, and reheater each carry terms that a single inlet-to-outlet temperature difference cannot identify.

## Build the chart from equations

At fixed total pressure $p$, put dry-bulb temperature $t$ on the horizontal axis and humidity ratio $\omega$ on the vertical axis. For any relative humidity $\phi$, plot

$$
\omega(t,\phi)=\frac{0.622\,\phi\,p_{\rm sat}(t)}
{p-\phi\,p_{\rm sat}(t)}.
$$

The $\phi=1$ curve is the saturation boundary of single-phase moist air. Intersect a horizontal line through a state with this curve to find the constant-pressure dew point. Using the dry-air enthalpy correlation from Chapter 14, an isenthalpic line satisfies $\omega=[h^*-1.006t]/(2501+1.86t)$. The denominator varies slowly near ambient temperatures, so these lines appear nearly straight. Constant wet-bulb lines are close to isenthalpic lines because the make-up liquid enthalpy in the adiabatic saturation balance is usually a small correction. Pressure enters both humidity ratio and specific volume. Read the chart at its specified pressure. [Psychrometry Part 5 · Chart construction](https://www.youtube.com/watch?v=IVz3N68fF1c&t=320)

Substituting $p_v=p\omega/(0.622+\omega)$ into $v^*=R_aT/(p-p_v)$ gives $v^*=(R_aT/p)(1+\omega/0.622)$, with $T$ in kelvin. To follow a constant-volume-per-kg line, hold the product $T(1+\omega/0.622)$ fixed. For sensible heating at fixed pressure and with no moisture added, follow a horizontal line to the right. To find the dry-air mass flow from an inlet volume flow, read $v^*$ at the inlet and divide the volume flow by it. [Psychrometry Part 5 · Specific-volume and process lines](https://www.youtube.com/watch?v=IVz3N68fF1c&t=420)

## Cool, drain, and reheat

Take air at 35 °C and 80% relative humidity, at 101.325 kPa. As an idealized coil model, let the outlet be saturated at 15 °C and the condensate leave at 15 °C. The inlet and outlet humidity ratios are 0.0289 and 0.01065 kg/kg dry air, using saturation pressures of 5.628 and 1.705 kPa. Let $q$ denote heat entering per kg dry air. With negligible shaft work and changes in kinetic and potential energy, separate water and energy balances give

$$
\frac{\dot m_\ell}{\dot m_a}=\omega_1-\omega_2,\qquad
q_{\rm coil}=h_2^*-h_1^*+(\omega_1-\omega_2)h_\ell(15).
$$

Here $h_\ell(15)\approx62.7$ kJ/kg liquid on the same reference. The drain carries about 0.0183 kg/kg dry air and the coil extracts about 66.3 kJ/kg dry air. Heating from 15 to 24 °C at fixed $\omega_2$ takes roughly 9.23 kJ/kg dry air. At 24 °C, the vapor pressure stays 1.705 kPa and the relative humidity is about 57%. The cooling step changes humidity ratio after saturation is reached. The reheating step changes relative humidity by raising $p_{\rm sat}$. A real coil can deliver unsaturated outlet air due to bypass and surface-temperature variation. [Psychrometry Part 6 · Cooling and reheat](https://www.youtube.com/watch?v=689t3mWiPy0&t=680)

The lecture also solves the design in reverse. For supply at 22 °C and 40% relative humidity, take $p_{\rm sat}(22)\approx2.645$ kPa. The supply vapor pressure must be $0.40(2.645)=1.058$ kPa. Sensible reheat at the same pressure preserves $\omega$ and therefore $p_v$. The idealized saturated coil outlet must be at the dew point of that vapor pressure, about 7.8 °C by saturation data. This is close to the lecture's chart reading of 7.5 °C. [Psychrometry Part 6 · Outlet design](https://www.youtube.com/watch?v=689t3mWiPy0&t=680)

## Mix on a dry-air flow basis

For an adiabatic mixer at common pressure without condensation, let $f=\dot m_{a,1}/(\dot m_{a,1}+\dot m_{a,2})$. Dry-air conservation gives the outlet base flow. Vapor and energy conservation then give

$$
\omega_3=f\omega_1+(1-f)\omega_2,\qquad
h_3^*=fh_1^*+(1-f)h_2^*.
$$

These are exactly linear in $(h^*,\omega)$ coordinates. The chart's $(t,\omega)$ coordinates approximate this straight mixing line because the heat capacity of air per kg dry air varies slightly with $\omega$. Invert the enthalpy relation for $t_3$ and test the result against saturation. If the calculated gas is supersaturated, allow a liquid stream and solve its phase equilibrium, water balance, and enthalpy simultaneously. [Psychrometry Part 7 · Adiabatic mixing](https://www.youtube.com/watch?v=32NLJlrLtTQ&t=0)

## Carry moisture out of a dryer or tower

In a steady dryer, $\dot m_a(\omega_{\rm out}-\omega_{\rm in})$ is the water gained from wet solids when air is the only outlet for removed moisture. On a wet basis, moisture fraction $x_{\rm wb}$ is water per kg wet solid. The ratio of water to dry solid is $x_{\rm wb}/(1-x_{\rm wb})$. For 150 kg/h wet feed at one-third moisture by mass, there is 100 kg/h dry solid and 50 kg/h water. A product at 10% wet-basis moisture retains $100(0.10/0.90)=11.11$ kg/h water. Air picking up 0.007 kg/kg dry air therefore needs about 5556 kg dry air/h.

A cooling tower likewise exports $\dot m_a(\omega_{\rm out}-\omega_{\rm in})$ as vapor. At steady inventory the make-up liquid rate must replace that vapor plus any liquid drift and blowdown. Cooling capacity comes from the energy balance, including sensible and latent changes in the air stream and the enthalpy carried by liquid water. A vapor balance alone gives the evaporative loss. [Psychrometry Part 7 · Drying and cooling tower](https://www.youtube.com/watch?v=32NLJlrLtTQ&t=800)

## Numerical laboratory

The [Python laboratory](code/chapter_15.py) computes coil duty, condensate, and reheater duty on one dry-air basis. It checks that total heat across both units plus the drain accounts for the change in moist-air enthalpy.

## Exercises and worked solutions

### Remove the drain enthalpy term

How much error in coil duty would result from treating the drain as having zero enthalpy in the stated reference?

**Solution.** The missing term is $0.0183(62.7)\simeq1.15$ kJ/kg dry air. With the liquid term omitted, calculated heat into the control volume is too negative by that amount, so the coil heat-removal magnitude is too high.

### Compare dryer moisture conventions

What is the wet-basis fraction for a product with 0.10 kg water per kg dry solid?

**Solution.** The wet solid weighs 1.10 kg per kg dry solid. The wet-basis fraction is $0.10/1.10=0.0909$. A target of 10% wet basis instead permits 0.1111 kg water per kg dry solid.

### Infer a mixing fraction

Mix two air streams without heat transfer or condensation. One enters with $\omega_1=0.018$ kg/kg dry air and the second with $\omega_2=0.006$. What dry-air flow fraction must the first supply to obtain $\omega_3=0.009$?

**Solution.** Solve $f=(0.009-0.006)/(0.018-0.006)=0.25$. The first-to-second dry-air mass-flow ratio is 1:3. An energy balance is still needed to find the outlet temperature and confirm the assumption of no condensation.

### Test whether a supply target needs a colder coil

Keep the reheater outlet at 24 °C, but require at most 50% relative humidity. Use $p_{\rm sat}(24)=2.985$ kPa. Can a 15 °C saturated coil outlet meet this limit with sensible reheat alone?

**Solution.** The supply vapor pressure must be at most $0.50(2.985)=1.493$ kPa. The coil leaves 1.705 kPa, which sensible reheat at unchanged pressure preserves. A saturated coil outlet needs $p_{\rm sat}\le1.493$ kPa, corresponding to roughly 13 °C or colder in this idealized model.
