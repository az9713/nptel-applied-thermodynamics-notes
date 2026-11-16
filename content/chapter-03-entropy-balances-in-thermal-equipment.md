---
title: Entropy balances in thermal equipment
lectures: 8–10
summary: Close the mass and energy accounts before interpreting the entropy residual in condensers, mixers, nozzles, and coupled devices.
source: https://www.youtube.com/watch?v=-lDtRFxhCuM
---

## A condenser and pump require two different reference temperatures

Consider the Tutorial 2 train. Steam condenses at constant pressure, then the liquid flows through an insulated pump. The coolant path ultimately rejects heat to an environment at temperature $T_0$. Let $\dot m$ be the water flow rate, with states 1 at the condenser inlet, 2 at its exit and 3 after the pump. The specific enthalpy $h$ measures internal energy plus the pressure-volume flow term. The specific entropy is $s$. With negligible kinetic and potential energy changes and no shaft work in the condenser, the rate of heat into the train from the environment is $\dot Q=\dot m(h_2-h_1)$. For the pump alone, the required shaft input is $\dot W_{\mathrm{in}}=\dot m(h_3-h_2)$. The ideal pump in the exercise is isentropic, so $s_3=s_2$. Its compression still requires work.

The condenser's wall temperature can vary. For the extended boundary reaching ambient, total generation is $\dot m(s_3-s_1)-\dot Q/T_0$. If condensation supplies nearly all the heat rejection at saturation temperature $T_{\mathrm{sat}}>T_0$, the thermal path contributes approximately $-\dot Q(1/T_0-1/T_{\mathrm{sat}})$. For the tutorial's subcooled outlet at 40 °C and 10 kPa, use the liquid entropy at that state. IAPWS-IF97 gives $h_1=2583.89$ and $h_2=167.54\,\mathrm{kJ/kg}$, so 1 kg/s rejects about 2416.34 kW. The stream entropy change is $0.572429-8.148893=-7.57646\,\mathrm{kJ/(kg\,K)}$. With $T_0=303.15\,\mathrm K$, generation inside the extended boundary is about $0.3943\,\mathrm{kW/K}$.

The Gibbs relation $dh=T\,ds+v\,dp$ reduces to $dh=v\,dp$ in the ideal pump, where $v$ is specific volume. Approximating liquid $v$ by its inlet value gives $h_3-h_2\approx0.00100788(10000-10)=10.07\,\mathrm{kJ/kg}$. Solving the isentropic pump state with IF97 gives 10.05 kJ/kg, which quantifies the error in holding $v$ constant over this pressure rise. [Tutorial 2, Problem 7](https://www.youtube.com/watch?v=-lDtRFxhCuM&t=20s) · [IAPWS-IF97](https://iapws.org/technical-guidance/release/IF97-Rev)

## Frozen-composition gas mixtures

Problem 8 asks how entropy changes in an ideal-gas mixture with unchanged composition. On a molar basis, let $y_j$ be species $j$'s mole fraction and let $\bar c_{p,j}$ be its molar heat capacity. With ideal gases and constant heat capacities, $\bar c_{p,\mathrm{mix}}=\sum_j y_j\bar c_{p,j}$. For fixed composition, the species partial pressures are $y_jp$, so their pressure ratios equal the total pressure ratio. Weighting the species Gibbs relations by $y_j$ yields

$$
\bar s_2-\bar s_1
=\bar c_{p,\mathrm{mix}}\ln(T_2/T_1)-R_u\ln(p_2/p_1),
$$

where $R_u$ is the universal gas constant in units consistent with the molar flow rate. A gram-mole is a mole. Divide the molar heat capacity by the mixture molar mass to change to a mass basis. If composition varies, the partial-pressure ratios must retain the mole fractions, and the fixed-composition expression no longer applies. [Tutorial 2, Problem 8](https://www.youtube.com/watch?v=-lDtRFxhCuM&t=860s)

The nitrogen–neon problem slide gives $0.5\,\mathrm{mol/s}$ of each gas. The two molecular masses, 28 and 20 g/mol, therefore give a combined flow of 24 g/s. The quoted heat-capacity ratios $1.4$ and $5/3$ give molar heat capacities $3.5R_u$ and $2.5R_u$, so $\bar c_{p,\mathrm{mix}}=3R_u$. At $T_1=300\,\mathrm K$ and $p_2/p_1=1/8$, setting the entropy change to zero gives $T_{2s}=300(1/8)^{1/3}=150\,\mathrm K$. The stated turbine efficiency of 0.50 gives $T_2=300-0.50(300-150)=225\,\mathrm K$. The actual molar entropy rise is $3R_u\ln(225/300)-R_u\ln(1/8)=10.11\,\mathrm{J/(mol\,K)}$ for $R_u=8.314\,\mathrm{J/(mol\,K)}$. At a total flow of 1 mol/s in the insulated turbine, this produces 10.11 W/K. [Problem 8, inputs and rate conversion](https://www.youtube.com/watch?v=-lDtRFxhCuM&t=880s)

## A tight outlet couples energy and continuity

Two air streams enter an insulated steady mixer. Let $T_j,p_j,C_j,\dot m_j$ denote each port's absolute temperature, pressure, speed and mass flow rate. Port 3 is the sole exit, with cross-sectional area $A_3$. Fixed-composition ideal air has specific gas constant $R$ and constant heat capacity $c_p$. Continuity gives $C_3=\dot m_3RT_3/(p_3 A_3)$ when pressure is in pascals and $R$ is in $\mathrm{J/(kg\,K)}$. Use those same SI units in the energy balance, with squared speeds halved in $\mathrm{J/kg}$. Inserting $C_3$ produces

$$
\frac12\left(\frac{\dot m_3R}{p_3A_3}\right)^2T_3^2+c_pT_3
=\frac{\dot m_1(c_pT_1+C_1^2/2)+\dot m_2(c_pT_2+C_2^2/2)}{\dot m_3}.
$$

For positive inlet temperature the right side is positive. The left side increases strictly from zero for $T_3\ge0$, giving a unique positive root. With the transcript inputs of $6$ and $1\,\mathrm{kg/s}$, $473.15$ and $373.15\,\mathrm K$, $100$ and $50\,\mathrm{m/s}$, exit diameter $0.10\,\mathrm m$, and exit pressure $400\,\mathrm{kPa}$, the laboratory solves for $T_3$ and $C_3$. It then evaluates entropy generation from the inlet pressures $600$ and $500\,\mathrm{kPa}$ and the calculated outlet state. A mixing-only estimate neglecting exit kinetic energy can fail through a small outlet. [Tutorial 2, Problem 9](https://www.youtube.com/watch?v=TukTqhqnfR4&t=20s)

## Nozzle efficiency and a coupled compressor–intercooler

For the steam nozzle in Problem 10, use the measured exit pressure $p_2$ and inlet entropy $s_1$ to obtain the reference isentropic exit enthalpy $h_{2s}$. With negligible inlet speed, nozzle efficiency is $(h_1-h_2)/(h_1-h_{2s})$. From 8 bar and 200 °C to 2 bar, IF97 gives $h_1=2839.77$ and $h_{2s}=2584.60$ kJ/kg. The specified 0.95 efficiency gives $h_2=2597.36\,\mathrm{kJ/kg}$. The adiabatic energy balance gives $C_2=\sqrt{2000(h_1-h_2)}=696.30\,\mathrm{m/s}$. Both outlet states are in the saturation dome. The actual vapor mass fraction is 0.95054 and generation per unit mass is $s_2-s_1=0.03243\,\mathrm{kJ/(kg\,K)}$. A mass flow rate would be required to turn this specific result into an entropy rate. [Tutorial 2, Problem 10](https://www.youtube.com/watch?v=TukTqhqnfR4&t=680s)

In Problem 11, air enters at 96 kPa and 27 °C with a volumetric rate of 26.91 m³/min. The ideal-gas relation $\dot m=p\dot V/(RT)$ gives $0.49982\,\mathrm{kg/s}$. The insulated compressor delivers air at 263 kPa and 127 °C. At $c_p=1.005\,\mathrm{kJ/(kg\,K)}$, shaft input is $0.49982(1.005)(127-27)=50.23\,\mathrm{kW}$. The intercooler brings the air to 77 °C at the same pressure. With water warming from 25 to 40 °C at $4.18\,\mathrm{kJ/(kg\,K)}$, its required mass flow is $0.49982(1.005)(127-77)/[4.18(40-25)]\approx0.401\,\mathrm{kg/s}$.

Across the combined control volume, the compressor exhaust and intercooler inlet cancel. The two external changes give total generation of about 15.0 W/K. Treated separately, the compressor gives a residual of about $-0.12\,\mathrm{W/K}$, which the adiabatic model forbids for exact inputs. The stated outlet pressure is about 0.22 kPa above the isentropic upper limit for the stated outlet temperature, a difference smaller than the reported pressure increment of 1 kPa. An admissible reconstruction needs pressure or temperature precision sufficient to resolve the sign. The positive combined result does not establish admissibility of the compressor alone. [Tutorial 2, Problem 11](https://www.youtube.com/watch?v=LYDBQr1m8Mk&t=20s)

## An adiabatic vortex tube can split a stream by temperature

Problem 12 supplies 1 kg/s of ideal air at 1 MPa, 20 °C, and 1 m/s. Two outlets discharge at 101.3 kPa, each carrying half the inlet flow. The hot outlet is at 116 °C and 100 m/s. The cold outlet has speed 200 m/s. Let $C_j$ and $T_j$ denote the port speeds and absolute temperatures. With zero shaft work, negligible elevation changes and the stated insulated boundary, the steady energy balance yields

$$
T_3=2T_1-T_2+\frac{C_1^2-(C_2^2+C_3^2)/2}{c_p},
$$

where $c_p=1.4R/(1.4-1)=1004.5\,\mathrm{J/(kg\,K)}$ and $R=287\,\mathrm{J/(kg\,K)}$. Substitution gives $T_3=172.26$ K. The entropy balance gives $\dot S_{\mathrm{gen}}=\sum_{j=2,3}\dot m_j[c_p\ln(T_j/T_1)-R\ln(p_j/p_1)]\approx532.39\,\mathrm{W/K}$. The inlet pressure drop allows an adiabatic separation of the temperatures with positive entropy production. These balances check the given outlet split and hot state. Predicting the split itself requires a flow model. [Tutorial 2, Problem 12](https://www.youtube.com/watch?v=LYDBQr1m8Mk&t=820s)

## Exercises and worked solutions

### Condenser feasibility

A condenser rejects $100\,\mathrm{kW}$ at a uniform $330\,\mathrm K$ to ambient at $300\,\mathrm K$. Find the entropy generated by that thermal path.

**Solution.** An idealized condenser rejects $100\,\mathrm{kW}$ isothermally at $330\,\mathrm K$ to ambient at $300\,\mathrm K$. The thermal path generates $100(1/300-1/330)=0.03030\,\mathrm{kW/K}$. An ideal insulated downstream pump adds no entropy generation. Moving the coolant boundary to ambient includes the positive generation even if the condenser fluid balance is internally reversible.

### Nozzle reference

A nozzle has $h_1=3000$ and $h_{2s}=2800\,\mathrm{kJ/kg}$, efficiency $0.90$ and negligible inlet speed. Find actual exit enthalpy and velocity.

**Solution.** Take $h_1=3000$ and $h_{2s}=2800\,\mathrm{kJ/kg}$ with efficiency $0.90$. Then $h_2=3000-0.90(200)=2820\,\mathrm{kJ/kg}$. With negligible inlet speed the exit speed is $\sqrt{2000(180)}=600\,\mathrm{m/s}$. This is an energy calculation. Phase and entropy require an additional property lookup.

### Internal flows

The compressor raises the air entropy flux by 0.04 kW/K. Its intercooler lowers the air entropy flux by 0.03 kW/K and raises the water entropy flux by 0.06 kW/K. How much entropy does the insulated train generate?

**Solution.** If a compressor raises the air's entropy flux by $0.04\,\mathrm{kW/K}$, its intercooler lowers the air entropy flux by $0.03\,\mathrm{kW/K}$ and increases the water flux by $0.06\,\mathrm{kW/K}$, generation for the insulated train is $0.04-0.03+0.06=0.07\,\mathrm{kW/K}$. The entropy change of the cooling air is negative even though generation of the exchanger is positive.

### Restriction and limiting flow

What happens to the mixer outlet temperature if the outlet area grows while inlet properties, mass flows, and exit pressure remain fixed?

**Solution.** The velocity factor $\dot m_3R/(p_3A_3)$ tends to zero. The quadratic reduces to its linear enthalpy term. Using the chapter inputs, the mass-weighted inlet enthalpy-equivalent temperature is $458.86\,\mathrm K$, and $(6\cdot 100^2+1\cdot 50^2)/(2\cdot 7\cdot 1010)=4.42\,\mathrm K$ of inlet kinetic energy raises the limiting outlet to $463.28\,\mathrm K$. This limit assumes the exit pressure can still be held fixed.

The [standalone lab](code/chapter_03.py) checks continuity, energy and the sign of entropy generation for the restricted mixer outlet. It gives $426.47\,\mathrm K$, $272.72\,\mathrm{m/s}$, and $267.61\,\mathrm{W/K}$ for outlet temperature, speed, and generation rate. A second check reproduces the vortex tube's cold-outlet temperature and entropy generation.
