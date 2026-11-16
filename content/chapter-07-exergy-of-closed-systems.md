---
title: Exergy of closed systems
lectures: 19–23
summary: Apply the closed-system exergy balance to compression, phase changes, internal equilibration, and moving pistons, then compare the flow tutorial cases.
source: https://www.youtube.com/watch?v=8unoXVZtbdg
---

## The reversible comparison uses useful work

Suppose a compressor takes the material inside a sealed piston from state 1 to state 2. Let $E,S,V$ be its energy, entropy, and volume, and let $T_0,p_0$ be the environmental temperature and pressure. For a fixed composition and fixed mass, the physical exergy change is $\Delta B=\Delta E+p_0\Delta V-T_0\Delta S$. The supplied useful work is the signed negative of $W-p_0\Delta V$, where $W$ is total work by the material. If only ambient heat transfer occurs, $\Delta B=W_{u,\mathrm{in}}-T_0S_{\mathrm{gen}}$. For a compression intended to raise exergy, the product is $\Delta B$ and the actual useful work input is the resource.

For ideal air with gas constant $R$ and constant heat capacities $c_v,c_p$, the initial mass is $p_1V_1/(RT_1)$. Then $V_2=mRT_2/p_2$, $\Delta U=mc_v(T_2-T_1)$ and $\Delta S=m[c_p\ln(T_2/T_1)-R\ln(p_2/p_1)]$. Use absolute temperature and pressure. The lab takes the tutorial's piston data and approximate constant-property air, defines the reported $1.2\,\mathrm{kJ}$ as **useful** work input, and obtains destruction from the balance. [Tutorial 4, air compression](https://www.youtube.com/watch?v=8unoXVZtbdg&t=20s)

## State properties and process heat play different roles

For a constant-pressure cooling process with only quasistatic pressure work, use $Q=\Delta H$ and $W=p\Delta V$. The change in chemical composition is zero. If refrigerant reaches saturation, compare the pressure with its critical pressure before selecting a two-phase model. Captions can drop decimal points and prefixes. The cooling example requires a subcritical pressure consistent with the stated saturation endpoint. A property-table calculation should use reliable refrigerant data on a consistent reference basis. [Tutorial 4, refrigerant cooling](https://www.youtube.com/watch?v=8unoXVZtbdg&t=660s)

When a partition separating two bodies is removed inside a closed, adiabatic, rigid vessel, $U$ and $V$ remain fixed if work is negligible. Use conservation of mass, the final common state and the initial compartment energies to solve equilibrium. Then $B_{\mathrm{dest}}=T_0(S_2-S_1)$ if no heat or useful work crosses the boundary. The initial entropy $S_1$ is the sum over both compartments. Applying a single initial temperature before equilibration changes the entropy account. [Tutorial 4, partitioned water tank](https://www.youtube.com/watch?v=8unoXVZtbdg&t=1280s)

For a piston moving under a specified pressure with stops, divide the process into a fixed-volume segment and a segment at its load pressure. In the fixed-volume segment $Q_{12}=\Delta U_{12}$ if there is no other work. In the second $Q_{23}=\Delta U_{23}+p_{\mathrm{load}}(V_3-V_2)$. The heater's exergy resource is $(1-T_0/T_H)(Q_{12}+Q_{23})$ when a single source reservoir at $T_H$ supplies all heat and the enlarged boundary reaches it. A reservoir at a temperature different from ambient can supply exergy, even when the piston does little useful work. [Tutorial 4, piston stops](https://www.youtube.com/watch?v=IN2KY5Ke79Y&t=20s)

## Internal heating and fixed-composition mixtures

An insulated tank contains a hot iron block and cooler water while a paddle wheel adds work. Let $C_b,C_w$ be their constant total heat capacities, $T_b,T_w$ their initial absolute temperatures, $T_f$ their common final temperature, and $W_{\mathrm{in}}>0$ the paddle work. With negligible container heat capacity and volume change, first-law and entropy accounts give

$$
C_b(T_f-T_b)+C_w(T_f-T_w)=W_{\mathrm{in}},\qquad
S_{\mathrm{gen}}=C_b\ln(T_f/T_b)+C_w\ln(T_f/T_w).
$$

Even if $W_{\mathrm{in}}=0$, equilibration through a finite temperature difference generates entropy. When the shaft delivers work as well, its energy adds to final internal energy, and dissipation is included in the generation residual. [Tutorial 5, iron block, water and paddle wheel](https://www.youtube.com/watch?v=5A8W-PzwdEw&t=20s)

For the constant-composition neon, oxygen and nitrogen mixture in a piston, use mole fractions $y_j$ and species molar masses $M_j$ to obtain mixture molar mass $M=\sum_jy_jM_j$. The mass fraction is $w_j=y_jM_j/M$, so the mass-specific heat capacity is $\sum_jw_jc_{p,j}$. The mass-specific gas constant is $R_u/M$. The volume displaced by travel $\ell$ in a cylinder of diameter $D$ is $\pi D^2\ell/4$. Use the appropriate external pressure history to compute work from that volume change. The piston diameter and travel alone do not fix the pressure history. [Tutorial 5, ideal gas mixture](https://www.youtube.com/watch?v=5A8W-PzwdEw&t=480s)

## Transfer the same reasoning to flow devices

| Source case | Exergy balance to apply |
| --- | --- |
| [Tutorial 5, air compressor](https://www.youtube.com/watch?v=5A8W-PzwdEw&t=1320s) | Shaft work supplies the stream exergy increase when heat ultimately reaches ambient. The destruction is the difference between the two rates. |
| [R134a throttle](https://www.youtube.com/watch?v=4HL1SnuKMQc&t=20s) | For an insulated steady valve with negligible speed and elevation changes, $h_e=h_i$ and the physical exergy decrease is $T_0(s_e-s_i)$. Zero actual work can coexist with positive reversible work between the endpoints. |
| [Insulated steam turbine](https://www.youtube.com/watch?v=4HL1SnuKMQc&t=700s) | Include inlet and exit speeds in stream exergy. The matched-state reversible power exceeds actual power by $T_0\dot S_{\mathrm{gen}}$. |
| [Steam turbine losing heat](https://www.youtube.com/watch?v=9JiZniMAnt0&t=20s) | Recover wet-steam enthalpy and entropy from quality if the outlet is saturated. Use the energy balance to infer mass flow if actual output and heat loss are given. Use the ambient heat term for the extended entropy generation. |
| [Steam nozzle](https://www.youtube.com/watch?v=9JiZniMAnt0&t=580s) | Kinetic energy increase is the useful product when acceleration is the purpose. Compare it with the thermomechanical stream exergy reduction that supplies it. |

## Exercises and worked solutions

### Ambient work in compression

A load supplies 3.0 kJ of useful work as volume drops by 0.008 m³ in 100 kPa ambient. Find the gas's total work input.

**Solution.** A piston reduces volume by $0.008\,\mathrm{m^3}$ against $100\,\mathrm{kPa}$ ambient while a load supplies $3.0\,\mathrm{kJ}$ of useful work. The atmosphere supplies another $0.8\,\mathrm{kJ}$, so total work input into the gas is $3.8\,\mathrm{kJ}$. Use the total in the energy balance and the useful input in the exergy balance.

### Thermal equilibration

Two rigid bodies at 400 and 300 K equilibrate in an insulated enclosure. Each has heat capacity 1 kJ/K. Find the lost useful work at 300 K ambient.

**Solution.** Two rigid bodies each have heat capacity $1\,\mathrm{kJ/K}$ and initially sit at $400$ and $300\,\mathrm K$. An insulated enclosure gives $T_f=350\,\mathrm K$ and $S_{\mathrm{gen}}=\ln(350/400)+\ln(350/300)=0.02062\,\mathrm{kJ/K}$. At $T_0=300\,\mathrm K$, the lost useful work is about $6.186\,\mathrm{kJ}$.

### Valve benchmark

How much physical exergy does an insulated valve destroy per kilogram for an entropy rise of 0.08 kJ/(kg K) at 300 K ambient?

**Solution.** If an insulated valve forces a stream through a specific entropy rise of $0.08\,\mathrm{kJ/(kg\,K)}$ at $T_0=300\,\mathrm K$, it destroys $24\,\mathrm{kJ/kg}$ of physical exergy. For the valve alone and negligible kinetic and potential terms, all of the stream exergy decrease is destroyed.

### Heater potential and work benchmark

A piston receives 60 kJ from a 600 K reservoir and gains 18 kJ of physical exergy. If ambient is 300 K, what useful output would a reversible process deliver at those endpoints and heat input?

**Solution.** The heat brings $60(1-300/600)=30\,\mathrm{kJ}$ of exergy. The reversible limit sets generation to zero, so the useful work would be $30-18=12\,\mathrm{kJ}$. A measured useful work of $8\,\mathrm{kJ}$ would correspond to $4\,\mathrm{kJ}$ destroyed.

The [standalone lab](code/chapter_07.py) checks energy conservation in a stirred enclosure and the useful work account for ideal-air compression. The captions anchor each case; the lab states its independent constant-property assumptions.
