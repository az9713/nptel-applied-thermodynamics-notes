---
title: Work and irreversibility in flow equipment
lectures: 11–13
summary: Compare actual and reversible reference processes for diffusers, compressors, nozzles, linked shafts, and blowdown.
source: https://www.youtube.com/watch?v=L3pg5PPob_I
---

## A diffuser converts kinetic energy into enthalpy

An insulated diffuser slows a gas so that pressure can rise without a rotating shaft. Let $T,p,C,A$ denote absolute temperature, absolute pressure, flow speed, and flow area. Subscripts 1 and 2 denote inlet and exit. For steady, one-dimensional dry air with constant specific heat $c_p$ and gas constant $R$, negligible elevation change, no heat and no shaft work, the energy and mass balances give

$$
C_2=\sqrt{C_1^2-2c_p(T_2-T_1)},\qquad
\frac{A_2}{A_1}=\frac{C_1}{C_2}\frac{p_1T_2}{p_2T_1}.
$$

Use $c_p$ in $\mathrm{J/(kg\,K)}$ in the speed equation. The area ratio eliminates the unknown mass flow through $\rho=p/(RT)$, with $\rho$ the density. The entropy rise is $c_p\ln(T_2/T_1)-R\ln(p_2/p_1)$, and must be nonnegative for the insulated device. The root and this inequality impose separate admissibility conditions.

Problem 13 gives $p_1=100\,\mathrm{kPa}$, $p_2=113\,\mathrm{kPa}$, $T_1=330.15\,\mathrm K$, $T_2=342.15\,\mathrm K$ and $C_1=200\,\mathrm{m/s}$. With $c_p=1005$ and $R=287\,\mathrm{J/(kg\,K)}$, the formulas give $C_2=126.016\,\mathrm{m/s}$, $A_2/A_1=1.4556$, and a specific entropy rise of $0.8042\,\mathrm{J/(kg\,K)}$. Precision matters because the two logarithmic terms in the entropy change nearly cancel. [Tutorial 3, Problem 13](https://www.youtube.com/watch?v=L3pg5PPob_I&t=20s)

## A compressor or nozzle needs a defined reference

Problem 14 gives compressor shaft input of 300 kW, heat loss of 1500 kJ/min, and air entering at 96 kPa and 17 °C with negligible speed. The outlet at 1 MPa and 327 °C has speed 120 m/s. Retain the corresponding $120^2/2000=7.20\,\mathrm{kJ/kg}$ in the balance. With negligible elevation change and $c_p=1.005\,\mathrm{kJ/(kg\,K)}$, the steady mass flow is

$$
\dot m=\frac{300-25}{1.005(327-17)+7.20}=0.86275\,\mathrm{kg/s}.
$$

For $R=0.287\,\mathrm{kJ/(kg\,K)}$, the temperature and pressure terms in $s_2-s_1=c_p\ln(T_2/T_1)-R\ln(p_2/p_1)$ give the stream entropy rise. Adding $25/290.15$ kW/K for heat reaching the 17 °C surroundings gives total entropy generation $0.13608\,\mathrm{kW/K}$. For the smaller compressor boundary, integrate each heat flux divided by its local wall temperature. An adiabatic isentropic reference has temperature $T_{2s}=T_1(p_2/p_1)^{R/c_p}$. The heat-rejection path changes the energy balance, so the adiabatic work reference alone cannot measure irreversibility in the cooled compressor. [Problem 14, air compressor](https://www.youtube.com/watch?v=L3pg5PPob_I&t=480s)

Problem 15 has superheated steam at 3 MPa and 400 °C, entering a $7\,\mathrm{cm^2}$ nozzle at 70 m/s. The actual exit is 2 MPa and 320 m/s. The steady adiabatic energy balance gives $h_2=h_1+(70^2-320^2)/2000$. With IAPWS-IF97, $h_1=3231.57$ and $h_2=3182.82$ kJ/kg. At 2 MPa this gives about 370.34 °C. The inlet specific volume $v_1$ fixes the mass flow $\dot m=A_1C_1/v_1$, and $\dot m(s_2-s_1)=0.05243\,\mathrm{kW/K}$. Match the exit pressure and impose $s_{2s}=s_1$ to compute the isentropic reference speed of 485.82 m/s. The lecture defines efficiency using the ratio of exit kinetic energies, giving $(320/485.82)^2\approx0.4339$ with these properties. The ratio of **gains** in kinetic energy instead gives $(320^2-70^2)/(485.82^2-70^2)\approx0.4219$. Both conventions coincide at negligible inlet speed. [Problem 15, steam nozzle](https://www.youtube.com/watch?v=L3pg5PPob_I&t=920s) · [IAPWS-IF97](https://iapws.org/technical-guidance/release/IF97-Rev)

## Couple devices at their shaft

The steam turbine in Problem 16 drives an air compressor. The steam and air streams stay separate, but their power accounts couple through the shaft. Let $\dot W_t>0$ be the turbine shaft output, $\dot W_c>0$ the compressor shaft input, and $\dot W_{\mathrm{loss}}$ mechanical power dissipated in the coupling. Then $\dot W_t=\dot W_c+\dot W_{\mathrm{loss}}$ if there is no other load. When the tutorial specifies heat rejected by each machine as a fraction of its shaft power, enter those fractions as thermal terms in the corresponding device energy balances. A shaft loss and surface heat loss describe different terms unless a model explicitly sends the shaft dissipation across that same boundary.

For example, let a turbine lose heat to ambient at $5\%$ of its shaft output and let its steam lose enthalpy at $105\,\mathrm{kW}$. Neglect kinetic and potential changes. The energy balance is $105=\dot W_t+0.05\dot W_t$, so $\dot W_t=100\,\mathrm{kW}$. A lossless coupling drives a compressor that rejects $10\%$ of input, delivering an enthalpy rise of $90\,\mathrm{kW}$ to the air. Across the combined boundary, $105=90+5+10$. The shaft transfer cancels. For entropy generation, keep the separate steam and air entropy changes and add $(5+10)/T_0$ for heat ultimately reaching ambient. [Tutorial 3, Problem 16](https://www.youtube.com/watch?v=gRmtexDJWQk&t=20s)

In the tutorial calculation the steam exit is fixed at 1 bar and must be at least dry saturated. Along the vapor isobar $dh=c_p\,dT$ with positive $c_p$, so the smallest allowed exit enthalpy is the saturated-vapor value $h_g$. The 30 bar, 600 °C inlet volume flow of 0.363 m³/s gives steam mass flow $\dot m_s\approx2.741\,\mathrm{kg/s}$ using IF97. Then $\dot W_t=\dot m_s(h_i-h_g)/1.05\approx2631\,\mathrm{kW}$. The compressor's air flow is about 10.053 kg/s from 8.66 m³/s at 100 kPa and 27 °C. With a lossless shaft and compressor heat loss of $0.10\dot W_t$, energy gives $T_2=T_1+0.90\dot W_t/(\dot m_a c_p)\approx534.61$ K, where $\dot m_a$ is the air mass flow and $c_p=1.0045\,\mathrm{kJ/(kg\,K)}$.

The problem specifies the compressor path by $pv^n=\mathrm{constant}$ with $n=1.35$, where $v$ is specific volume. Eliminating $v$ using $pv=RT$ gives $p_2=p_1(T_2/T_1)^{n/(n-1)}\approx926.8$ kPa. This pressure rises with turbine power, which explains choosing the smallest allowed steam outlet enthalpy. At a 25 °C ambient boundary, adding each stream entropy change to its own heat-rejection rate divided by $298.15$ K gives about 0.0263 kW/K for the turbine and 0.2875 kW/K for the compressor. The turbine residual is sensitive to small property differences because its two contributions have opposite signs. [Problem 16, turbine limit and compressor path](https://www.youtube.com/watch?v=gRmtexDJWQk&t=240s)

## An electrically heated blowdown differs from liquid drainage

Problem 17 holds a rigid air tank at constant temperature while it discharges. Enclose both the well-mixed ideal gas and its electrical heater in an insulated boundary. The electrical work crosses this boundary without carrying entropy. If escaping gas crosses with the instantaneous tank specific entropy $s$ and heater entropy storage is negligible, the only entropy transfer is $s\,dm_e$ leaving with discharged mass $dm_e=-dm$. The generation increment is therefore $dS_{\mathrm{gen}}=d(ms)+s\,dm_e=m\,ds$. At fixed absolute temperature $T$ and volume $V$, ideal-gas relations give $m=pV/(RT)$ and $ds=-R\,dp/p$, so $dS_{\mathrm{gen}}=-V\,dp/T$. Integration gives $S_{\mathrm{gen}}=V(p_1-p_2)/T$. For the $5\,\mathrm{m^3}$ tank at $330.15\,\mathrm K$, dropping from $500$ to $200\,\mathrm{kPa}$ gives $4.543\,\mathrm{kJ/K}$ inside the selected boundary. A boundary around the gas alone would also require modeling the thermal interaction with the heater. [Tutorial 3, Problem 17](https://www.youtube.com/watch?v=14RBJj3gido&t=20s)

The same ideal-gas blowdown also requires $W_{\mathrm{elec,in}}=V(p_1-p_2)=1500\,\mathrm{kJ}$. In the energy balance each kilogram leaving takes enthalpy $h$, while the tank loses stored internal energy $u$. The electrical input supplies the difference $h-u=RT$ per kilogram. This reproduces $T S_{\mathrm{gen}}$ for the stated isothermal model.

Problem 18 instead withdraws saturated liquid from a two-phase tank that receives 5 kJ of heat at constant pressure of 400 kPa. The initial mass is 7.5 kg, and the experiment stops at dry saturated vapor. At that pressure let $v_f,v_g$ be the saturated liquid and vapor specific volumes, $h_{fg}$ the enthalpy of vaporization and $x_1$ the initial vapor mass fraction. Constant tank volume gives $m_2=m_1[x_1+(1-x_1)v_f/v_g]$. The enthalpy form of the balance in [Chapter 1, transient balances](chapter-01-control-volume-entropy.html#retain-entropy-storage-during-a-transient) gives $Q=(m_2-m_1x_1)h_{fg}$. Substitute the mass relation to obtain

$$
x_1=1-\frac{Qv_g}{m_1v_fh_{fg}}.
$$

At 400 kPa, IF97 gives $v_f=0.00108356$ and $v_g=0.462392\,\mathrm{m^3/kg}$, $h_{fg}=2133.33\,\mathrm{kJ/kg}$, and $T_{\mathrm{sat}}=416.76$ K. The initial quality is 0.86665, final mass 6.502 kg, and withdrawn liquid mass about 0.998 kg. The enlarged entropy balance for heat from a 500 °C reservoir gives $Q(1/T_{\mathrm{sat}}-1/773.15)=5.53\,\mathrm{J/K}$. This form avoids taking differences of large rounded energy and entropy inventories in a calculation driven by only 5 kJ of heat. [Tutorial 3, Problem 18](https://www.youtube.com/watch?v=14RBJj3gido&t=860s)

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

Run the [standalone diffuser and tank calculations](code/chapter_04.py). The worked examples use input data corroborated by retained slides and reevaluate the water states with IAPWS-IF97.
