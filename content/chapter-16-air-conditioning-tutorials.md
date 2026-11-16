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

The tutorial gives a heat-removal rate of 1227 kJ/min, or 20.45 kW. With the chapter's constant-heat-capacity approximation and negligible velocity change, the dry-coil trial gives $t_2=t_1-20.45/[\dot m_a(1.006+1.86\omega)]\approx25.0$ °C. With $p_{v,2}=p_{v,1}$, the relative humidity is $1.274/3.170=40.2\%$, so no condensation is needed to reach the bulk outlet state. The inlet dew point is about 10.6 °C. Assume the entire coil surface stays above it to rule out local condensation. Checking the duty with the rounded outlet temperature gives

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

Steam injection follows the same water balance but brings vapor enthalpy into the humidifier. In the lecture's heating and humidification example, air enters at 10 °C and 70% relative humidity, at 100 kPa and 50 m³/min. It leaves at 20 °C and 60% relative humidity. The inlet and final humidity ratios are 0.00539 and 0.00885 kg/kg dry air. The inlet $v^*$ gives $\dot m_a=1.016$ kg/s, so the rate of injecting saturated steam at 50 °C is $1.016(0.00885-0.00539)\approx0.00352$ kg/s. The heater outlet has $\omega_2=\omega_1$. The adiabatic humidifier balance gives $h_2^*=h_3^*-(\omega_3-\omega_1)h_g(50)\approx33.62$ kJ/kg dry air using $h_g(50)\approx2592$ kJ/kg. Inverting at $\omega_1$ gives $t_2\approx19.8$ °C. Taking the difference $\dot m_a(h_2^*-h_1^*)$ across the heater gives about 10.1 kW. [Tutorial 8 Part 4 · Steam injection](https://www.youtube.com/watch?v=oJgpYsLNJh0&t=20)

In the lecture's wet-tower problem, 90 kg/s of recirculating water cools from 40 to 25 °C. Make-up enters at 25 °C. Air enters at 23 °C and 60% relative humidity and leaves saturated at 32 °C, at approximately one atmosphere. Neglect heat losses, fan work, liquid drift and blowdown. The make-up rate is $\dot m_{\rm make}=\dot m_a\Delta\omega$, where $\Delta\omega$ is the outlet minus inlet humidity ratio. The recirculating stream loses $90[h_\ell(40)-h_\ell(25)]$ kW. The air gains $\dot m_a\Delta h^*$, and make-up supplies $\dot m_{\rm make}h_\ell(25)$. Eliminating make-up from the energy balance gives

$$
\dot m_a=\frac{90[h_\ell(40)-h_\ell(25)]}
{\Delta h^*-\Delta\omega\,h_\ell(25)}.
$$

The correlations give $\Delta\omega\approx0.0201$ kg/kg dry air, $\Delta h^*\approx60.8$ kJ/kg dry air, and $\dot m_a\approx96$ kg/s, so make-up is about 1.94 kg/s. Values read from a chart give a slightly different result. The tower approach temperature is the cold-water temperature above entering-air wet-bulb temperature. The range is the hot-to-cold water temperature drop, here 15 °C. [Tutorial 8 Part 4 · Cooling tower](https://www.youtube.com/watch?v=oJgpYsLNJh0&t=1860)

## Numerical laboratory

Run the [Python laboratory](code/chapter_16.py) to calculate the duct airflow and dry-coil outlet at the tutorial's heat duty. It checks that a colder trial crosses the dew point and solves the tower make-up balance.

## Exercises and worked solutions

### Force the dew-point test

For the duct inlet above, test a 5 °C outlet using $p_{\rm sat}(5)=0.872$ kPa.

**Solution.** The predicted unchanged vapor pressure 1.274 kPa exceeds 0.872 kPa, so the gas cannot leave at 5 °C with all its initial vapor. For a saturated 5 °C outlet, $\omega_2=0.622(0.872)/(100-0.872)=0.00547$. At 4.01 kg/s dry-air flow, about $4.01(0.00802-0.00547)=0.0102$ kg/s drains.

### Include losses in a tower

Add drift of 0.10 kg/s and blowdown of 0.30 kg/s to the tower example. Find the make-up rate at steady inventory.

**Solution.** At the same air flow and states, make-up balances evaporation and both outgoing liquid streams, giving $1.94+0.10+0.30=2.34$ kg/s. The air-side water balance identifies the vapor loss. The energy balance would also require the liquid outlet enthalpies if the air flow were unknown.

### Judge a partially bypassed coil

The bulk air outlet in the duct case is 25 °C. Can a coil with surface temperatures as low as 8 °C still yield unsaturated bulk outlet air?

**Solution.** Yes. The surface is below the inlet dew point, so air reaching it can lose vapor. When that colder, drier air mixes with warmer bypassed air, the mixed outlet can be unsaturated. Bulk outlet temperature alone cannot validate the dry-coil energy balance.

### Compare two equal volume flows

Two unsaturated streams each deliver 1.0 m³/s to a mixer. Their volumes per kg dry air are 0.90 and 0.80 m³/kg, and their humidity ratios are 0.018 and 0.006 kg/kg. Find the mixed humidity ratio assuming no condensation.

**Solution.** The two dry-air rates are $1/0.90$ and $1/0.80$ kg/s. Their first-stream fraction is $8/17\approx0.471$, giving $\omega_3\approx0.01165$ kg/kg dry air. Equal weighting would give 0.012 and would overstate the wetter inlet's contribution.
