---
title: Air-Conditioning Tutorials
lectures: 46–49
summary: Infer state from dew point, test if a coil can stay dry, and distinguish liquid make-up from total water circulation.
source: https://www.youtube.com/watch?v=srqc4eXwM8Y
---

Psychrometric tutorials often give readings in one set of variables and ask for energy in another. Translate the readings into temperature, total pressure, and water-vapor partial pressure before deciding which terms belong in the control-volume balances.

## Use the dew point at the actual pressure

Suppose air at 30 °C and total pressure 100 kPa has a dew point of 20 °C. From the saturation data take $p_{\rm sat}(20)=2.339$ kPa and $p_{\rm sat}(30)=4.246$ kPa. Then $p_v=2.339$ kPa, $p_a=97.661$ kPa, $\phi=55.1\%$, and $\omega=0.01490$ kg vapor/kg dry air. The mixture density is $[1+\omega]/v^*$ with $v^*=R_aT/p_a$.

Now repeat with the same readings at 360 kPa. The vapor pressure and relative humidity have the same values under the ideal-mixture model, but $\omega$ drops to 0.00407 kg/kg dry air. A sea-level psychrometric chart would give the wrong humidity ratio for this pressure. In a rigid heated vessel with liquid initially present, first calculate the vapor mass that saturation would require at the trial temperature. If that mass exceeds the water inventory, evaporate the entire inventory and use the resulting unsaturated vapor pressure. [Tutorial 7 Part 1 · State and rigid-vessel questions](https://www.youtube.com/watch?v=srqc4eXwM8Y&t=0)

## Heat at fixed humidity ratio or cool with a drain

In a simple heating duct with no moisture transfer, $\omega_2=\omega_1$ when all water remains vapor. At essentially constant pressure, $\phi_2=\phi_1 p_{\rm sat}(t_1)/p_{\rm sat}(t_2)$. This step differs from cooling below the dew point, in which water separates and leaves as liquid. If moist air enters at $t_1$ and leaves saturated at $t_2<t_{\rm dp}$, the heat entering per unit dry-air mass is $h_2^*-h_1^*+(\omega_1-\omega_2)h_\ell(t_2)$. The sign follows the specified control-volume convention. [Tutorial 7 Part 2 · Duct heating and dehumidification](https://www.youtube.com/watch?v=Wu0Td5nzcs8&t=0)

## Get mass flow from the inlet volume flow

Take the tutorial geometry of a 0.50 m diameter duct with 18 m/s inlet speed. For a uniform inlet profile the volumetric flow is $\dot V=\pi D^2 U/4=3.534$ m³/s. Let the inlet state be 30 °C, 100 kPa, 30% relative humidity. Then $p_v=1.274$ kPa, $\omega=0.00802$, and $v^*\approx0.8814$ m³/kg dry air. The dry-air mass rate is about 4.01 kg/s.

For a teaching variant, let the coil leave the gas at 25 °C at about the same pressure and with negligible velocity change. With the trial $p_{v,2}=p_{v,1}$, the relative humidity is $1.274/3.170=40.2\%$, so no condensation is needed to reach the bulk outlet state. The inlet dew point is about 10.6 °C. Assume the entire coil surface stays above it to rule out local condensation. The duty is

$$
\dot Q=\dot m_a(1.006+1.86\omega)(25-30)\approx-20.5\ \mathrm{kW}.
$$

When two streams mix, a volumetric flow rate must be converted separately using its own inlet $v^*$ before weighting $\omega$ and $h^*$. Equal volume rates of warm and cool air do not generally contain equal dry-air mass rates. [Tutorial 8 Part 3 · Duct and mixer](https://www.youtube.com/watch?v=Jd3gLOTJ9fw&t=20)

## Use the water and energy requirements together

An evaporative cooler that adds liquid at temperature $t_w$ and has negligible external heat transfer obeys

$$
h_2^*-h_1^*=(\omega_2-\omega_1)h_\ell(t_w).
$$

For water cool enough that the right-side correction is small, treating $h^*$ as constant is a useful first estimate. At the outlet, check that $\omega_2\leq\omega_{\rm sat}(t_2,p)$ and that $\omega_2\geq\omega_1$ for net water addition. A specified outlet cooler than the adiabatic saturation point cannot be obtained by an ideal saturator with its feed water at the outlet temperature.

For a tower with $\dot m_a=180$ kg/s and humidity-ratio rise 0.0106 kg/kg dry air, evaporation is 1.91 kg/s. A recirculation rate of hundreds of kg/s would not change that vapor balance. Drift and blowdown add to make-up and must be counted if present. The tower approach temperature is the cold-water temperature above entering-air wet-bulb temperature; it differs from the hot-to-cold water temperature range. [Tutorial 8 Part 4 · Evaporative cooler and cooling tower](https://www.youtube.com/watch?v=oJgpYsLNJh0&t=1280)

## Numerical laboratory

Run the [Python laboratory](code/chapter_16.py) to calculate the duct flow, the saturation test at the trial outlet, and heat duty. It also checks that a colder trial outlet crosses the dew point.

## Exercises and worked solutions

### Force the dew-point test

For the duct inlet above, test a 5 °C outlet using $p_{\rm sat}(5)=0.872$ kPa.

**Solution.** The predicted unchanged vapor pressure 1.274 kPa exceeds 0.872 kPa, so the gas cannot leave at 5 °C with all its initial vapor. For a saturated 5 °C outlet, $\omega_2=0.622(0.872)/(100-0.872)=0.00547$. At 4.01 kg/s dry-air flow, about $4.01(0.00802-0.00547)=0.0102$ kg/s drains.

### Include losses in a tower

Add drift of 0.10 kg/s and blowdown of 0.30 kg/s to the tower example. Find the make-up rate at steady inventory.

**Solution.** Makeup balances evaporation and both outgoing liquid streams, giving $1.91+0.10+0.30=2.31$ kg/s. The air-side water measurement identifies the vapor loss and leaves the liquid losses to separate measurements.

### Judge a partially bypassed coil

The bulk air outlet in the duct case is 25 °C. Can a coil with surface temperatures as low as 8 °C still yield unsaturated bulk outlet air?

**Solution.** Yes. The surface is below the inlet dew point, so air reaching it can lose vapor. When that colder, drier air mixes with warmer bypassed air, the mixed outlet can be unsaturated. Bulk outlet temperature alone cannot validate the dry-coil energy balance.

### Compare two equal volume flows

Two unsaturated streams each deliver 1.0 m³/s to a mixer. Their volumes per kg dry air are 0.90 and 0.80 m³/kg, and their humidity ratios are 0.018 and 0.006 kg/kg. Find the mixed humidity ratio assuming no condensation.

**Solution.** The two dry-air rates are $1/0.90$ and $1/0.80$ kg/s. Their first-stream fraction is $8/17\approx0.471$, giving $\omega_3\approx0.01165$ kg/kg dry air. Equal weighting would give 0.012 and would overstate the wetter inlet's contribution.
