---
title: Exergy of steady and transient control volumes
lectures: 24–26
summary: Identify the exergy resource and useful product in heaters, turbines, chillers, and changing-mass vessels.
source: https://www.youtube.com/watch?v=Y2AbiUZc4wg
---

## Direct mixing and separated heat exchange

In a feedwater heater, a steam stream directly contacts colder liquid. Let $\dot m_i$ be its inlet and outlet mass flow rates, $h_i$ the corresponding enthalpies, and $\psi_i=h_i-h_0-T_0(s_i-s_0)$ the stream exergy with negligible speed and elevation changes. The insulated mixer satisfies $\dot m_3=\dot m_1+\dot m_2$ and $\dot m_3h_3=\dot m_1h_1+\dot m_2h_2$. If steam pressure is unknown while the feed and mixed-liquid conditions are known, solve this energy equation for the required steam enthalpy. Then use saturation properties to find candidate steam pressures. Accept a solution only if it matches the specified saturation branch and liquid states.

If inlet 1 is feedwater and inlet 2 steam, assign product $\dot m_1(\psi_3-\psi_1)$ and resource $\dot m_2(\psi_2-\psi_3)$. Their difference in resource-minus-product order is $\dot m_1\psi_1+\dot m_2\psi_2-\dot m_3\psi_3$, the destruction for the insulated mixer. The product definition follows the mass originally assigned to feedwater. [Tutorial 6, Problem 12](https://www.youtube.com/watch?v=Y2AbiUZc4wg&t=20s)

A gas-to-air preheater keeps the streams separate. When externally insulated, heat leaves the hot stream at the same rate it enters the cold stream. Each temperature can vary substantially along the exchanger. For constant-pressure streams with constant specific heats and unchanged composition,

$$
\dot S_{\mathrm{gen}}
=\dot m_h c_{p,h}\ln(T_{h,e}/T_{h,i})
+\dot m_c c_{p,c}\ln(T_{c,e}/T_{c,i}).
$$

Here subscripts $h,c$ distinguish hot and cold streams and $i,e$ their inlet and exit. The rate of exergy destruction is $T_0\dot S_{\mathrm{gen}}$. Pressure losses introduce further terms in the entropy changes. The lab uses an original counterflow-compatible temperature set, solves for the hot outlet and checks both energy and exergy balance. [Tutorial 6, Problem 13](https://www.youtube.com/watch?v=Y2AbiUZc4wg&t=820s)

## Include latent heat and a consistent reference

A chilling unit takes a material from $T_i$ above its freezing point $T_f$ to $T_e$ below it at effectively constant pressure. Let $c_{p,l}$ and $c_{p,s}$ be the liquid and solid constant heat capacities, and $L_f>0$ the latent heat of fusion per unit mass. The specific enthalpy and entropy changes are

$$
\Delta h=c_{p,l}(T_f-T_i)-L_f+c_{p,s}(T_e-T_f),
$$

$$
\Delta s=c_{p,l}\ln(T_f/T_i)-L_f/T_f
+c_{p,s}\ln(T_e/T_f).
$$

This model assumes equilibrium freezing at one temperature rather than a distributed freezing range. The outlet can have higher physical exergy while its enthalpy is lower because its entropy fell. If the inlet is at ambient, the chilled product's minimum reversible work requirement, with heat ultimately exchanged only with ambient, is its rise in flow exergy. A real refrigeration machine can require more. [Tutorial 6, Problem 14](https://www.youtube.com/watch?v=Y2AbiUZc4wg&t=1440s)

## Turbine work and stationary tank storage

For the nitrogen–argon turbine in Problem 15, the specified percentages are mass fractions $w_j$. Compute $R_{\mathrm{mix}}=\sum_j w_jR_u/M_j$ and $c_{p,\mathrm{mix}}=\sum_j w_jc_{p,j}$. Here $R_u$ is the universal gas constant and $M_j$ the species molar mass. If each species has constant heat capacity ratio $\gamma_j$, obtain $c_{p,j}=\gamma_jR_j/(\gamma_j-1)$ before averaging. For insulated flow with fixed composition, the entropy rise follows the ideal-gas relation using the mixture properties. Shaft output is the product and the decrease in stream exergy the resource. Averaging the two $\gamma_j$ directly does not give the mixture heat capacity ratio.

Problem 16 concerns vapor withdrawn from a rigid two-phase tank. Use the specified **phase volumes** to determine the initial and final phase masses via $m_f=V_f/v_f$ and $m_g=V_g/v_g$. Here subscripts $f,g$ identify saturated liquid and vapor. The entropy carried out is the integral of $s_{\mathrm{out}}\,dm_{\mathrm{out}}$. Replacing that term by a single outlet entropy requires a constant outlet state or an independent mass-weighted average. Determine heat from the integrated energy balance and its entropy transfer at the stated reservoir temperature. At an agreed $T_0$, apply $T_0S_{\mathrm{gen}}$ to that boundary. [Tutorial 6, Problem 15](https://www.youtube.com/watch?v=1m_uNUjAfjk&t=20s) · [Problem 16](https://www.youtube.com/watch?v=1m_uNUjAfjk&t=500s)

## A moving piston requires its own volume-work term

For an insulated cylinder admitting mass $m_i$ with constant $h_i,s_i$, the integrated balances with no outflow give $U_2-U_1=m_i h_i-W$, with $W$ the piston work out, and $S_{\mathrm{gen}}=S_2-S_1-m_i s_i$. Flow kinetic and elevation terms are neglected here. Problem 17 has a weighted piston moving at constant load pressure, so $W=p_{\mathrm{load}}(V_2-V_1)$. If the inlet enters at high enough enthalpy, its energy can evaporate part or all of the initial liquid. Use the final phase condition and the mass balance to close the problem.

Problem 18 extends this calculation to air filling a cylinder until the piston meets stops and then filling at fixed volume. Solve for the intermediate mass using the volume at the stops, the equation of state, and the energy balance for segment one. The second segment has zero piston work, even though pressure may change. For the whole interval the incoming mass contribution is $m_i s_i$ only if the entry entropy is constant. Total useful work is $W-p_0(V_2-V_1)$. A rigid tank model would omit the mechanical work of the piston. A larger stationary control volume can enclose the cylinder and moving hardware if it tracks the associated changes in energy storage and the mechanical transfer at its boundary. [Tutorial 6, Problem 17](https://www.youtube.com/watch?v=C4BzJiZvh5s&t=20s) · [Problem 18](https://www.youtube.com/watch?v=C4BzJiZvh5s&t=760s)

## Exercises and worked solutions

### Chilling below ambient

Compute the flow exergy gain from freezing a body already at its freezing point of 273.15 K with latent heat 334 kJ/kg. Ambient is 300 K.

**Solution.** Suppose freezing occurs at $273.15\,\mathrm K$, with $L_f=334\,\mathrm{kJ/kg}$, and the material is already at its freezing point. At $T_0=300\,\mathrm K$, freezing alone changes flow exergy by $-334+300(334/273.15)=32.83\,\mathrm{kJ/kg}$. Under the equilibrium model, the energy required to cool and freeze cannot be inferred from exergy without specifying how the refrigeration machine rejects heat.

### Mixture gas constant

Find the gas constant and nitrogen mole fraction of a mixture that contains 30% nitrogen and 70% argon by mass.

**Solution.** For $30\%$ nitrogen and $70\%$ argon by mass, use molar masses 28 and $40\,\mathrm{kg/kmol}$. Then $R_{\mathrm{mix}}=8.314(0.30/28+0.70/40)\approx0.2346\,\mathrm{kJ/(kg\,K)}$. Dividing the mass fractions by the molar masses and normalizing gives nitrogen mole fraction $(0.30/28)/(0.30/28+0.70/40)\approx0.380$. The two fractions differ because the molar masses differ.

### Work at the piston stops

A weighted piston moves from 0.20 to 0.50 m³ at 200 kPa, then rests against stops while filling continues. Find total and useful work at 100 kPa ambient.

**Solution.** A piston moves from $0.20$ to $0.50\,\mathrm{m^3}$ at $200\,\mathrm{kPa}$ and subsequently remains at the stops as filling continues. Total work is $60\,\mathrm{kJ}$. At $p_0=100\,\mathrm{kPa}$ it delivers $30\,\mathrm{kJ}$ of useful work. Pressure rise during the second stage contributes no boundary work.

### Control-volume entropy inventory

Steam enters an insulated piston cylinder with no exit. It brings 2.0 kg at an entropy of 6.5 kJ/(kg K). The total stored entropy rises by 14.2 kJ/K. Find entropy generation and exergy destruction at ambient temperature 300 K.

**Solution.** Mass brings $2.0(6.5)=13.0\,\mathrm{kJ/K}$. The entropy account requires generation $14.2-13.0=1.2\,\mathrm{kJ/K}$, so destruction is $300(1.2)=360\,\mathrm{kJ}$. The piston can still deliver useful work at the same time.

Run the [standalone heat-exchanger and freezing lab](code/chapter_08.py). These models test the analytical balances with original inputs. The captions anchor the tutorial cases, and the edition does not report a complete visual review of their property tables.
