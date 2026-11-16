---
title: Work and irreversibility in flow equipment
lectures: 11–13
summary: Compare actual and reversible reference processes for diffusers, compressors, nozzles, linked shafts, and blowdown.
source: https://www.youtube.com/watch?v=L3pg5PPob_I
---

## A diffuser converts kinetic energy into enthalpy

An insulated diffuser slows a gas so that pressure can rise without a rotating shaft. Let $T,p,C,A$ denote temperature, pressure, flow speed and flow area. Subscripts 1 and 2 denote inlet and exit. For steady, one-dimensional dry air with constant specific heat $c_p$ and gas constant $R$, negligible elevation change, no heat and no shaft work, the energy and mass balances give

$$
C_2=\sqrt{C_1^2-2c_p(T_2-T_1)},\qquad
\frac{A_2}{A_1}=\frac{C_1}{C_2}\frac{p_1T_2}{p_2T_1}.
$$

Use $c_p$ in $\mathrm{J/(kg\,K)}$ in the speed equation. The area ratio eliminates the unknown mass flow through $\rho=p/(RT)$, with $\rho$ the density. The entropy rise is $c_p\ln(T_2/T_1)-R\ln(p_2/p_1)$, and must be nonnegative for the insulated device. The root and this inequality impose separate admissibility conditions.

Problem 13 gives $p_1=100\,\mathrm{kPa}$, $p_2=113\,\mathrm{kPa}$, $T_1=330.15\,\mathrm K$, $T_2=342.15\,\mathrm K$ and $C_1=200\,\mathrm{m/s}$. The lab evaluates these with $c_p=1005$ and $R=287\,\mathrm{J/(kg\,K)}$. The calculated entropy rise is small. Precision matters because two logarithmic terms nearly cancel. [Tutorial 3, Problem 13](https://www.youtube.com/watch?v=L3pg5PPob_I&t=20s)

## A compressor or nozzle needs a defined reference

For Problem 14 use the inlet state and exit pressure to define an isentropic reference. At constant $c_p$ it has temperature $T_{2s}=T_1(p_2/p_1)^{R/c_p}$. For a steady compressor with negligible speed and elevation changes, the actual specific shaft input is $h_2-h_1-q$, where $q$ is heat supplied per unit mass. The isentropic input $h_{2s}-h_1$ describes an adiabatic reference. A cooled compressor can require less work than that reference while still generating entropy. State which process the comparison holds fixed. Its entropy production per mass is $s_2-s_1-q/T_b$ for uniform boundary temperature $T_b$. With heat eventually exchanged with ambient, use $T_0$ for the larger region instead.

Problem 15 starts with superheated steam entering an adiabatic nozzle. Preserve the kinetic terms unless speeds are demonstrably negligible. At a specified exit pressure, use $s_{2s}=s_1$ to obtain $h_{2s}$ from water properties, then determine the available isentropic rise in kinetic energy. An actual exit entropy can be tested once pressure and enthalpy are known. A speed computed from an isentropic reference alone describes the reference nozzle. [Problem 14, air compressor](https://www.youtube.com/watch?v=L3pg5PPob_I&t=500s) · [Problem 15, steam nozzle](https://www.youtube.com/watch?v=L3pg5PPob_I&t=900s)

## Couple devices at their shaft

The steam turbine in Problem 16 drives an air compressor. The steam and air streams stay separate, but their power accounts couple through the shaft. Let $\dot W_t>0$ be the turbine shaft output, $\dot W_c>0$ the compressor shaft input, and $\dot W_{\mathrm{loss}}$ mechanical power dissipated in the coupling. Then $\dot W_t=\dot W_c+\dot W_{\mathrm{loss}}$ if there is no other load. When the tutorial specifies heat rejected by each machine as a fraction of its shaft power, enter those fractions as thermal terms in the corresponding device energy balances. A shaft loss and surface heat loss describe different terms unless a model explicitly sends the shaft dissipation across that same boundary.

For example, let a turbine lose heat to ambient at $5\%$ of its shaft output and let its steam lose enthalpy at $105\,\mathrm{kW}$. Neglect kinetic and potential changes. The energy balance is $105=\dot W_t+0.05\dot W_t$, so $\dot W_t=100\,\mathrm{kW}$. A lossless coupling drives a compressor that rejects $10\%$ of input, delivering an enthalpy rise of $90\,\mathrm{kW}$ to the air. Across the combined boundary, $105=90+5+10$. The shaft transfer cancels. For entropy generation, keep the separate steam and air entropy changes and add $(5+10)/T_0$ for heat ultimately reaching ambient. [Tutorial 3, Problem 16](https://www.youtube.com/watch?v=gRmtexDJWQk&t=20s)

## An electrically heated blowdown differs from liquid drainage

Problem 17 holds a rigid air tank at constant temperature while it discharges. Enclose both the well-mixed ideal gas and its electrical heater in an insulated boundary. The electrical work crosses this boundary without carrying entropy. If escaping gas crosses with the instantaneous tank specific entropy $s$ and heater entropy storage is negligible, the only entropy transfer is $s\,dm_e$ leaving with discharged mass $dm_e=-dm$. The generation increment is therefore $dS_{\mathrm{gen}}=d(ms)+s\,dm_e=m\,ds$. At fixed absolute temperature $T$ and volume $V$, ideal-gas relations give $m=pV/(RT)$ and $ds=-R\,dp/p$, so $dS_{\mathrm{gen}}=-V\,dp/T$. Integration gives $S_{\mathrm{gen}}=V(p_1-p_2)/T$. For the $5\,\mathrm{m^3}$ tank at $330.15\,\mathrm K$, dropping from $500$ to $200\,\mathrm{kPa}$ gives $4.543\,\mathrm{kJ/K}$ inside the selected boundary. A boundary around the gas alone would also require modeling the thermal interaction with the heater. [Tutorial 3, Problem 17](https://www.youtube.com/watch?v=14RBJj3gido&t=20s)

Problem 18 instead withdraws saturated liquid from a two-phase tank kept at constant pressure by heat input. At that pressure let $v_f,v_g$ be the saturated liquid and vapor specific volumes, $V$ the fixed tank volume and $m$ the current tank mass. Vapor mass fraction is $x=(V/m-v_f)/(v_g-v_f)$. The discharged mass has liquid properties even while the remaining material becomes richer in vapor. Compute $m_e=m_1-m_2$ first, then use $Q=(m_2u_2-m_1u_1)+m_eh_f$ and $S_{\mathrm{gen,total}}=m_2s_2-m_1s_1+m_es_f-Q/T_0$ for heat from a reservoir at $T_0$. Subscripts $f$ identify the saturated liquid values. [Tutorial 3, Problem 18](https://www.youtube.com/watch?v=14RBJj3gido&t=860s)

## Exercises and worked solutions

### Diffuser limit

Can the tutorial diffuser raise air temperature by 25 K without heat or shaft work?

**Solution.** For the lecture's $200\,\mathrm{m/s}$ inlet, the greatest stationary-frame enthalpy rise available by complete deceleration is $200^2/2=20\,\mathrm{kJ/kg}$. At $c_p=1.005\,\mathrm{kJ/(kg\,K)}$, a temperature rise of $25\,\mathrm K$ would require $25.125\,\mathrm{kJ/kg}$. The proposed adiabatic no-work diffuser cannot provide it.

### Entropy uncertainty

Estimate how a 0.3 K uncertainty at the diffuser exit affects the entropy balance.

**Solution.** At fixed $T_1$ and pressures the entropy-rise sensitivity to exit temperature is $c_p/T_2$. At the tutorial exit temperature this is about $2.94\,\mathrm{J/(kg\,K^2)}$. An uncertainty of $0.3\,\mathrm K$ shifts the entropy difference by approximately $0.88\,\mathrm{J/(kg\,K)}$, comparable to the computed difference. A measured sign at this scale needs uncertainty accounting.

### Two-phase outlet

A tank drains saturated liquid until its mass falls from 7.5 to 6.0 kg. If the liquid entropy is 1.8 kJ/(kg K), how much entropy leaves with mass?

**Solution.** Suppose the tank initially contains $7.5\,\mathrm{kg}$ and the final measured inventory is $6.0\,\mathrm{kg}$. If liquid alone leaves at $s_f=1.8\,\mathrm{kJ/(kg\,K)}$, the exported entropy is $1.5(1.8)=2.7\,\mathrm{kJ/K}$. The tank entropy inventory can rise or fall depending on the final vapor fraction. Add the exported entropy to the inventory difference before applying the reservoir correction.

### Shaft coupling loss

Repeat the 100 kW turbine example if the shaft loses 4 kW in the coupling and the compressor still rejects 10% of its shaft input. Assume coupling loss reaches ambient.

**Solution.** Only $96\,\mathrm{kW}$ reaches the compressor, so its air enthalpy rise is $0.90(96)=86.4\,\mathrm{kW}$. The surrounding sink receives $5+4+9.6=18.6\,\mathrm{kW}$. The combined energy account closes at $105=86.4+18.6\,\mathrm{kW}$. The sink contributes $18.6/T_0$ to the extended entropy account.

Run the [standalone diffuser and tank calculations](code/chapter_04.py). The timestamps reconstruct the tutorial's problems from automatic captions. The exact steam tables shown on screen were outside the pilot source audit.
