---
title: Properties of Moist Air
lectures: 39–42
summary: Derive humidity ratio, dew point, and enthalpy on a dry-air mass basis, then use phase equilibrium to locate condensation.
source: https://www.youtube.com/watch?v=es-2LA2bsu4
---

Air at 30 °C and 50% relative humidity can reach saturation at a temperature well above freezing. The same air can be heated with no change in its water content while its relative humidity falls. Both observations follow once the water partial pressure and the water inventory are kept distinct.

## Describe the mixture with two partial pressures

Model moist air as a mixture of ideal gases. Use subscripts $a$ and $v$ for dry air and water vapor, respectively. At mixture pressure $p$, Dalton's law gives $p=p_a+p_v$. Both components occupy the same volume $V$ at absolute temperature $T$. From $pV=mRT$ applied to each component,

$$
\omega=\frac{m_v}{m_a}
=\frac{R_a}{R_v}\frac{p_v}{p-p_v}
\simeq 0.622\frac{p_v}{p-p_v}.
$$

The humidity ratio $\omega$ is in kg water vapor per kg dry air. The vapor mass fraction in the gas mixture is $\omega/(1+\omega)$. If liquid water appears, track its mass separately. In the ideal-mixture model, relative humidity $\phi=p_v/p_{\rm sat}(T)$ compares the actual partial pressure with the saturation pressure above liquid water at temperature $T$. Condensation at elevated pressure can require a model that accounts for nonideal gas and liquid equilibrium. The inverse ideal-mixture relation is $p_v=p\omega/(0.622+\omega)$. At fixed $p$ and $\omega$, $p_v$ is fixed. [Lecture 39 · Mixture definitions](https://www.youtube.com/watch?v=es-2LA2bsu4&t=220)

## Find the onset of condensation

For cooling at constant total pressure and fixed humidity ratio up to saturation, the dew point satisfies $p_{\rm sat}(T_{\rm dp})=p_v$. Use a saturation table or invert a vapor-pressure relation. At 30 °C, 101.325 kPa and $\phi=0.50$, take $p_{\rm sat}=4.246$ kPa. Then $p_v=2.123$ kPa, $\omega=0.01331$ kg/kg dry air, and $T_{\rm dp}\approx18.5$ °C. Below the dew point, some vapor condenses if the stable condensed phase is liquid.

The volume constraint changes the calculation in a rigid tank. For a sealed 1.00 m³ tank starting at the same state, the initial vapor mass is $p_{v,1}V/(R_vT_1)=0.01517$ kg. At 10 °C, saturation gives $p_{v,2}\simeq1.228$ kPa and $m_{v,2}=0.00940$ kg. About 5.8 g of liquid remains in the tank. A test for condensation is to calculate the hypothetical $p_{v,2}=m_{v,1}R_vT_2/V$ with all water still in vapor form, then compare it with $p_{\rm sat}(T_2)$. This test retains the rigid-volume constraint. [Lecture 40 · Worked examples](https://www.youtube.com/watch?v=ewtFkNDw-5c&t=0) · [IAPWS saturation properties](https://www.iapws.org/relguide/Supp-sat.html)

## Put mixture enthalpy on a dry-air basis

In a steady-flow duct with no dry-air source or sink, $\dot m_a$ is constant even when liquid water enters or leaves. Choose zero dry-air and liquid-water sensible enthalpy at 0 °C. With $t$ in °C and constant heat capacities near ambient conditions,

$$
h^*=h_a+\omega h_v \simeq 1.006t+\omega(2501+1.86t)
\qquad [\mathrm{kJ/kg_{dry\,air}}].
$$

Here $h_v$ is expressed per kg vapor and includes the reference latent enthalpy. The volume per kg dry air is $v^*=R_aT/(p-p_v)$. Multiplying $h^*$ by $\dot m_a$ gives the enthalpy flow carried by the air stream, and dividing the inlet volumetric flow by $v^*$ gives $\dot m_a$. For a sealed tank use internal energy in the closed-system balance, counting the remaining liquid separately. [Lecture 41 · Closed and steady-flow balances](https://www.youtube.com/watch?v=xyJWx-HbXyI&t=0)

For a sealed charge, $\Delta U=m_a\Delta u_a+\Delta(m_v u_v+m_\ell u_\ell)$. In the lecture's isothermal compression, air at 25 °C starts at 25% relative humidity, and its volume falls to one-fifth of the original value. With liquid volume negligible, the all-vapor trial gives $p_{v,2}=5p_{v,1}=1.25p_{\rm sat}(25\,{}^\circ\mathrm C)$. Saturation limits the remaining vapor mass to $m_{v,2}/m_{v,1}=1/(5\times0.25)=0.80$. The other 20% condenses. Since $T$ stays fixed, the ideal-gas internal energies per kg stay fixed, and $\Delta U=-m_{\ell,2}(u_v-u_\ell)$. With work positive out of the charge, $Q=\Delta U+W$. Computing $Q$ requires the compression path for $W=\int p\,dV$ when boundary work is the only work and compression is quasistatic. [Lecture 41 · Isothermal compression](https://www.youtube.com/watch?v=xyJWx-HbXyI&t=440)

## Distinguish dry bulb, dew point, and wet bulb

For an insulated steady-flow adiabatic saturator ultimately leaving saturated at $t_s$, take the make-up water at $t_s$. The water balance gives added liquid per kg dry air as $\omega_s-\omega_1$. The energy balance gives

$$
h_1^*+(\omega_s-\omega_1)h_\ell(t_s)=h_s^*,\qquad
\omega_s=\omega_{\rm sat}(t_s,p).
$$

The two terms on the left are the incoming gas and liquid enthalpies. Solve the equation for $t_s$ using the saturation relation. A ventilated wet-bulb thermometer uses evaporation from a wetted sensor. Its reading approximates the thermodynamic wet bulb for ordinary air–water mixtures under suitable airflow and radiation conditions. For ordinary unsaturated air with liquid water in the saturator, the dew point is below the thermodynamic wet bulb, which is below the dry-bulb temperature $t_1$. At saturation all three coincide. If $t_s$ is known, expand the incoming air term as $h_a(t_1)+\omega_1 h_v(t_1)$ and solve directly for

$$
\omega_1=\frac{h_s^*-h_a(t_1)-\omega_s h_\ell(t_s)}
{h_v(t_1)-h_\ell(t_s)}.
$$

This converts a measured dry-bulb and approximate wet-bulb pair into the vapor inventory. [Lecture 42 · Wet bulb and adiabatic saturation](https://www.youtube.com/watch?v=kSMMgwBP11c&t=1020)

## Numerical laboratory

Run the [Python laboratory](code/chapter_14.py) to reproduce the humidity ratio, dew point, and tank condensate. It uses the IAPWS liquid-water saturation-pressure correlation and checks the moisture and phase balances.

## Exercises and worked solutions

### Warm air without adding water

Heat the 30 °C, 50% air to 40 °C at constant pressure. Use $p_{\rm sat}(40\,^\circ\mathrm C)=7.385$ kPa. What happens to $\phi$ and $T_{\rm dp}$?

**Solution.** With neither vapor nor dry air added, $\omega$ stays constant. With $p$ fixed, $p_v=2.123$ kPa. The relative humidity falls to $2.123/7.385=0.2875$, and the dew point stays about 18.5 °C.

### Know the basis before applying a flow rate

The 30 °C inlet state has $h^*\approx64.2$ kJ/kg dry air. Find its enthalpy per kg of moist gas.

**Solution.** One kg dry air accompanies 0.01331 kg vapor. Divide by $1+\omega$ to obtain about $63.4$ kJ per kg of moist gas. Either basis gives the same enthalpy flow when multiplied by the corresponding mass rate.

### Predict the dew point of a compressed stream

Double the initial mixture pressure while keeping the air at 30 °C and its humidity ratio unchanged until it reaches equilibrium. How close is the endpoint to condensation?

**Solution.** The vapor fraction on a molar basis is fixed because the two gas masses remain fixed. Thus $p_v$ doubles to 4.246 kPa, which equals $p_{\rm sat}(30)$. An equilibrium gas at this point is saturated. Further compression at 30 °C requires some water to condense.

### Recover humidity from an adiabatic saturation state

An ideal saturator accepts air at 30 °C and 101.325 kPa and produces saturated air at 20 °C. Liquid feed enters at 20 °C. Use $p_{\rm sat}(20)=2.339$ kPa and $h_\ell(20)=83.6$ kJ/kg liquid. Find the inlet humidity ratio.

**Solution.** Saturation fixes $\omega_s=0.622(2.339)/(101.325-2.339)\approx0.01470$, and $h_s^*\approx57.43$ kJ/kg dry air. Substitute $h_1^*=30.18+2556.8\omega_1$ into the saturation balance to obtain $\omega_1=(57.43-30.18-0.01470(83.6))/(2556.8-83.6)\approx0.0105$ kg/kg dry air. The inlet ratio is below $\omega_s$, consistent with adding water.
