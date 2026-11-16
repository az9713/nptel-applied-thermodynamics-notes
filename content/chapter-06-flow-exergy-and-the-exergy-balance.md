---
title: Flow exergy and useful output
lectures: 17–18
summary: Derive stream availability and apply one exergy account to compressors, turbines, feedwater heaters, and heat engines.
source: https://www.youtube.com/watch?v=M2PWao2pvsI
---

## The flow term replaces ambient displacement work

A turbine can deliver work while a stream moves toward the reference environment. Let $T_0,p_0$ be the ambient temperature and pressure, and $h_0,s_0$ the specific enthalpy and entropy of the same composition at that reference state. The specific flow exergy of a stream with enthalpy $h$, entropy $s$, speed $C$, and elevation $z$ relative to reference is

$$
\psi=(h-h_0)-T_0(s-s_0)+
\frac{C^2/2+gz}{1000}.
$$

Here $h$ is in $\mathrm{kJ/kg}$, $s$ in $\mathrm{kJ/(kg\,K)}$, and gravitational acceleration $g$ in $\mathrm{m/s^2}$. The speed, elevation, and conversion factor use SI. For a fixed flow device, subtract $T_0$ times the steady entropy account from the energy account. The terms attached to each inlet and exit become mass-flow rates multiplying $\psi$. The enthalpy already includes the work needed to push a stream across the port. In a closed system that work is instead accounted for by subtracting ambient displacement from total work.

For a fixed control volume at steady operation, with heat rates $\dot Q_j$ into its surface at temperatures $T_j$, shaft output $\dot W$, and entropy generation inside the boundary $\dot S_{\mathrm{gen}}$,

$$
\dot W=\sum_i\dot m_i\psi_i-\sum_e\dot m_e\psi_e
+\sum_j(1-T_0/T_j)\dot Q_j-T_0\dot S_{\mathrm{gen}}.
$$

For unsteady operation subtract the rate of physical exergy accumulation inside the control volume on the right side. For heat rejected to ambient, a boundary expanded to $T_0$ sets the heat-exergy term to zero and includes dissipation along the thermal path in generation. The ambient balance remains useful even when the device-surface temperature is unknown. [Exergy transfer, Part 3](https://www.youtube.com/watch?v=ovsdDMvXmPw&t=1340s) · [Part 5, compressor](https://www.youtube.com/watch?v=vfdk8-Eiajc&t=20s)

## Choose the product before defining an efficiency

**Compression.** In the Part 5 example, 2.1 kg/min of air enters at ambient state and an 8 kW compressor raises it to 650 kPa and 187 °C. For an extended boundary whose heat reaches ambient, shaft input is the sole exergy resource and the stream exergy gain is the product. The lecture's energy balance gives about 2.27 kW of heat rejection. Its entropy balance yields about 1.21 kW of destruction, leaving a 6.79 kW stream exergy gain and $6.79/8\approx84.9\%$ second-law efficiency. With its own temperature, pressure and mass-flow inputs, the lab checks the same identity between the energy–entropy residual and the work-minus-stream-gain calculation. [Part 5, compressor](https://www.youtube.com/watch?v=vfdk8-Eiajc&t=20s)

**Turbine.** The stream exergy decrease supplies shaft production. With heat ultimately exchanged only with ambient, the second-law efficiency is $\dot W/\{\dot m(\psi_i-\psi_e)\}$. At fixed inlet and exit states with matched external thermal constraints, the stream decrease is the reversible work benchmark. It is distinct from an isentropic-efficiency calculation in which the actual and isentropic exits can have different enthalpies. [Part 5, turbine](https://www.youtube.com/watch?v=vfdk8-Eiajc&t=220s)

**Feedwater heater.** Part 5 assigns steam as the resource and heated feedwater as the product. In a direct mixer the steam eventually joins the outlet. To define the product, track the inlet feedwater mass and compare its outlet-equivalent exergy at the mixed state with its inlet exergy. Compare the inlet steam mass's exergy decrease to that same mixed reference state. That convention uses both mass fractions without adding a second outlet stream. With negligible kinetic or gravitational changes and only ambient heat rejection, the difference between resource and product equals destruction. [Part 5, feedwater heater](https://www.youtube.com/watch?v=vfdk8-Eiajc&t=380s)

**Heat engine.** For a cyclic engine receiving $Q_H>0$ at $T_H$ and rejecting $Q_C>0$ at $T_C$, energy conservation gives $W=Q_H-Q_C$. Part 5 counts the rejected heat as a recovered exergy stream when $T_H>T_C\ge T_0$. The entropy balance over the cycle, including both reservoir contacts, gives $S_{\mathrm{gen}}=Q_C/T_C-Q_H/T_H$. Write thermal efficiency as $\eta_{\mathrm{th}}=W/Q_H$ and Carnot efficiency as $\eta_C=1-T_C/T_H$. Substituting $Q_C=Q_H(1-\eta_{\mathrm{th}})$ in the recovered-to-supplied ratio gives

$$
\eta_{\mathrm{II}}=\frac{W+(1-T_0/T_C)Q_C}{(1-T_0/T_H)Q_H}
=1-\frac{(T_0/T_C)(\eta_C-\eta_{\mathrm{th}})}{1-T_0/T_H}.
$$

At $T_C=T_0$, the heat rejection term vanishes and $\eta_{\mathrm{II}}=\eta_{\mathrm{th}}/\eta_C$. For a plant whose product is shaft work alone, leave exported heat exergy outside the product even when the sink is warmer than ambient. [Part 5, cyclic engine](https://www.youtube.com/watch?v=vfdk8-Eiajc&t=940s)

## Connect the closed-system examples

The first three worked examples explain where a prescribed work or heat interaction enters the exergy account. In polytropic air compression $pV^n$ is constant. Integrate $p\,dV$ for boundary work, subtract $p_0\Delta V$ for useful work, and use endpoint entropy to get destruction once the heat source is specified. For rigid stirred refrigerant, volume work vanishes, but the stirrer supplies work and dissipates it internally. For a piston initially resting on stops, first use a constant-volume segment, then a moving boundary at the lift pressure. Sum the heat-exergy integrals for all segments and avoid treating the total heat as reversible work. [Part 4, polytropic compression](https://www.youtube.com/watch?v=M2PWao2pvsI&t=0s) · [Part 4, stirred refrigerant](https://www.youtube.com/watch?v=M2PWao2pvsI&t=240s) · [Part 4, piston on stops](https://www.youtube.com/watch?v=M2PWao2pvsI&t=580s)

In the polytropic example, 2 kg of air starts at 100 kPa and 300 K and reaches 800 kPa with $n=1.27$. The volume relation gives $V_2=V_1(100/800)^{1/1.27}$. The boundary-work integral is $(p_2V_2-p_1V_1)/(1-n)$. Using the lecture’s rounded work of −357.11 kJ and $p_0\Delta V=-139.50$ kJ gives useful work out of −217.61 kJ. At 300 K, generation of 0.08056 kJ/K destroys 24.17 kJ of exergy. The reversible comparison requires 193.44 kJ of useful input, so the efficiency is $193.44/217.61\approx88.9\%$.

The stirred-vessel example starts with 5 kg of saturated R134a vapor at −15 °C and ends at the 30 °C ambient temperature. Because the vessel is rigid, the 500 kJ of stirrer input is entirely useful work crossing the boundary, with the outward sign $W_u=-500$ kJ. The lecture finds about 1.70 kJ/K of generation, equivalent to about 514 kJ of destruction at ambient. The reversible comparison at the same endpoints and with heat exchanged only with ambient gives about $-500+514=14$ kJ of useful output. The process consumes work even though the specified state change reduces stored exergy. The reversible-to-actual input ratio used for the compressor has no useful interpretation here.

## Exercises and worked solutions

### Heat leak from a turbine

Steam loses 75 kW of exergy through its state change and delivers 60 kW of shaft work. Heat ultimately reaches ambient at 300 K. Find combined exergy destruction and entropy generation.

**Solution.** Steam loses flow exergy at $75\,\mathrm{kW}$ and produces $60\,\mathrm{kW}$ of shaft output. If all heat reaches $T_0=300\,\mathrm K$ ambient, the extended region destroys $15\,\mathrm{kW}$, so generation there is $0.050\,\mathrm{kW/K}$. A smaller region can transfer out some exergy as heat.

### Engine with a finite-temperature source

A heat engine receives 100 kJ at 500 K and delivers 30 kJ net work. Its sink is ambient at 300 K. Find its first- and second-law efficiencies.

**Solution.** With $100\,\mathrm{kJ}$ input at $500\,\mathrm K$ and ambient at $300\,\mathrm K$, the heat provides $40\,\mathrm{kJ}$ of exergy. If output is $30\,\mathrm{kJ}$ and heat only goes to ambient, first-law thermal efficiency is $30\%$ and second-law efficiency is $75\%$. The difference between ideal and actual work is $10\,\mathrm{kJ}$.

### Kinetic exergy

Determine the flow exergy change caused by raising speed from 20 to 100 m/s at unchanged temperature, pressure and elevation.

**Solution.** At otherwise unchanged temperature, pressure, and elevation, raising a stream speed from $20$ to $100\,\mathrm{m/s}$ increases its kinetic and flow exergy by $(100^2-20^2)/2000=4.8\,\mathrm{kJ/kg}$. This term can be the product for a nozzle.

### Why exergy follows the selected boundary

The turbine in the first exercise rejects 9 kW through a uniform wall at 450 K. The wall rejects to 300 K ambient. Split the total destruction between the device and its external heat path.

**Solution.** The device exports heat exergy $9(1-300/450)=3\,\mathrm{kW}$. Thus it destroys $75-60-3=12\,\mathrm{kW}$. The external transfer destroys the exported $3\,\mathrm{kW}$ as heat reaches the environment. The total remains $15\,\mathrm{kW}$.

Run the [standalone compressor and engine lab](code/chapter_06.py). The examples use original input data where the caption track did not convey a complete property table.
