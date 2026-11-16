---
title: Entropy balances in thermal equipment
lectures: 8–10
summary: Close the mass and energy accounts before interpreting the entropy residual in condensers, mixers, nozzles, and coupled devices.
source: https://www.youtube.com/watch?v=-lDtRFxhCuM
---

## A condenser and pump require two different reference temperatures

Consider the Tutorial 2 train. Steam condenses at constant pressure, then the liquid flows through an insulated pump. The coolant path ultimately rejects heat to an environment at temperature $T_0$. Let $\dot m$ be the water flow rate, with states 1 at the condenser inlet, 2 at its exit and 3 after the pump. The specific enthalpy $h$ measures internal energy plus the pressure-volume flow term. The specific entropy is $s$. With negligible kinetic and potential energy changes and no shaft work in the condenser, the rate of heat into the train from the environment is $\dot Q=\dot m(h_2-h_1)$. For the pump alone, the required shaft input is $\dot W_{\mathrm{in}}=\dot m(h_3-h_2)$. The ideal pump in the exercise is isentropic, so $s_3=s_2$. Its compression still requires work.

The condenser's wall temperature can vary. For the extended boundary reaching ambient, total generation is $\dot m(s_3-s_1)-\dot Q/T_0$. When most heat rejection is condensation near saturation temperature $T_{\mathrm{sat}}>T_0$, an idealized internally reversible condenser at one temperature would contribute zero internal generation. The thermal path then contributes approximately $-\dot Q(1/T_0-1/T_{\mathrm{sat}})$, which is positive. The actual tutorial adds a subcooled outlet, so use the exit entropy at the specified pressure and temperature. Match steam properties to the phase at each state. [Tutorial 2, Problem 7](https://www.youtube.com/watch?v=-lDtRFxhCuM&t=20s) · [IAPWS water and steam formulation](https://www.iapws.org/relguide/IF97-Rev.html)

## Frozen-composition gas mixtures

Problem 8 asks how entropy changes in an ideal-gas mixture with unchanged composition. On a molar basis, let $y_j$ be species $j$'s mole fraction and let $\bar c_{p,j}$ be its molar heat capacity. With ideal gases and constant heat capacities, $\bar c_{p,\mathrm{mix}}=\sum_j y_j\bar c_{p,j}$. For fixed composition, the species partial pressures are $y_jp$, so their pressure ratios equal the total pressure ratio. Weighting the species Gibbs relations by $y_j$ yields

$$
\bar s_2-\bar s_1
=\bar c_{p,\mathrm{mix}}\ln(T_2/T_1)-R_u\ln(p_2/p_1),
$$

where $R_u$ is the universal gas constant in units consistent with the molar flow rate. A gram-mole is a mole. Divide the molar heat capacity by the mixture molar mass to change to a mass basis. If composition varies, the partial-pressure ratios must retain the mole fractions, and the fixed-composition expression no longer applies. [Tutorial 2, Problem 8](https://www.youtube.com/watch?v=-lDtRFxhCuM&t=860s)

For the nitrogen–neon turbine, both molar flow rates are $5\,\mathrm{mol/s}$. The quoted heat-capacity ratios $1.4$ and $5/3$ give molar heat capacities $3.5R_u$ and $2.5R_u$, so $\bar c_{p,\mathrm{mix}}=3R_u$. For inlet temperature $300\,\mathrm K$ and pressure ratio $p_2/p_1=1/8$, the reversible adiabatic exit is $T_{2s}=300(1/8)^{1/3}=150\,\mathrm K$. The stated turbine efficiency $0.50$ gives $T_2=300-0.50(300-150)=225\,\mathrm K$. With $R_u=8.314\,\mathrm{J/(mol\,K)}$, the generation rate is $10[3R_u\ln(225/300)-R_u\ln(1/8)]=101.13\,\mathrm{W/K}$. Scaling the flow down by a factor of ten scales generation by the same factor while leaving the temperatures fixed. The caption's rate and spoken output are potentially inconsistent, so the calculation states its molar inputs explicitly.

## A tight outlet couples energy and continuity

Two air streams enter an insulated steady mixer. Let $T_j,p_j,C_j,\dot m_j$ denote each port's absolute temperature, pressure, speed and mass flow rate. Port 3 is the sole exit, with cross-sectional area $A_3$. Fixed-composition ideal air has specific gas constant $R$ and constant heat capacity $c_p$. Continuity gives $C_3=\dot m_3RT_3/(p_3 A_3)$ when pressure is in pascals and $R$ is in $\mathrm{J/(kg\,K)}$. Use those same SI units in the energy balance, with squared speeds halved in $\mathrm{J/kg}$. Inserting $C_3$ produces

$$
\frac12\left(\frac{\dot m_3R}{p_3A_3}\right)^2T_3^2+c_pT_3
=\frac{\dot m_1(c_pT_1+C_1^2/2)+\dot m_2(c_pT_2+C_2^2/2)}{\dot m_3}.
$$

For positive inlet temperature the right side is positive. The left side increases strictly from zero for $T_3\ge0$, giving a unique positive root. With the transcript inputs of $6$ and $1\,\mathrm{kg/s}$, $473.15$ and $373.15\,\mathrm K$, $100$ and $50\,\mathrm{m/s}$, exit diameter $0.10\,\mathrm m$, and exit pressure $400\,\mathrm{kPa}$, the laboratory solves for $T_3$ and $C_3$. It then evaluates entropy generation from the inlet pressures $600$ and $500\,\mathrm{kPa}$ and the calculated outlet state. A mixing-only estimate neglecting exit kinetic energy can fail through a small outlet. [Tutorial 2, Problem 9](https://www.youtube.com/watch?v=TukTqhqnfR4&t=20s)

## Nozzle efficiency and a coupled compressor–intercooler

For the steam nozzle in Problem 10, use the measured exit pressure $p_2$ and inlet entropy $s_1$ to obtain the reference isentropic exit enthalpy $h_{2s}$. If inlet speed is small, nozzle efficiency is $(h_1-h_2)/(h_1-h_{2s})$. First solve for $h_2$, then recover exit speed from $C_2^2/2=h_1-h_2$ in consistent units. Identify the exit phase by comparing $h_2$ with the saturation bounds at $p_2$. In the adiabatic nozzle, the generation rate per mass flow is $s_2-s_1$. [Tutorial 2, Problem 10](https://www.youtube.com/watch?v=TukTqhqnfR4&t=680s)

In Problem 11 an air compressor discharges to an intercooler cooled by a separate water stream. An air compressor balance can determine shaft power from its own enthalpy rise when heat loss is neglected. The heat exchanger balance gives air heat loss equal to water enthalpy gain as long as its outer boundary is insulated. Obtain volumetric-flow-based air mass flow from $\dot m=p\dot V/(RT)$ in consistent units. Across the combined control volume, the compressor exhaust port and the intercooler inlet port cancel. The water entropy gain and the air entropy change remain, and their sum is total generation for the insulated train. A separate calculation for each device can localize the sources of irreversibility when intermediate conditions are measured. [Tutorial 2, Problem 11](https://www.youtube.com/watch?v=LYDBQr1m8Mk&t=20s)

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

The [standalone mixer lab](code/chapter_03.py) checks continuity, energy and the sign of entropy generation for the restricted outlet. It gives $426.47\,\mathrm K$, $272.72\,\mathrm{m/s}$, and $267.61\,\mathrm{W/K}$ for outlet temperature, speed, and generation rate. The captions anchor device choices and tutorial assumptions. No full board audit was performed.
