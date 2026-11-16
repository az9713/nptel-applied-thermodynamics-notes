---
title: Exergy and the reference environment
lectures: 14–16
summary: Derive closed-system availability, distinguish work transfer from energy transfer, and quantify the work lost to entropy generation.
source: https://www.youtube.com/watch?v=vvBkCJtw1rI
---

## Useful work excludes displacement of the environment

A piston expands against ambient at pressure $p_0$ while lifting a load. Let $W$ be total work out of the gas and $\Delta V$ the change in its volume. Work $p_0\Delta V$ goes to displacing the surroundings; useful work received by the load is $W_u=W-p_0\Delta V$. If the piston instead compresses the gas, the ambient helps supply work and the same formula holds with $\Delta V<0$.

To compare different initial states, specify an environment at fixed absolute temperature $T_0$ and pressure $p_0$. The **physical dead state** has the same temperature and pressure, zero motion and reference elevation, and preserves the material's composition under the model. Chemical exergy requires additional assumptions about the environment and allowed reactions. A cold object, a vacuum vessel, and a hot object can all have positive physical exergy because each departs from equilibrium with that specified environment. [Exergy, Part 1](https://www.youtube.com/watch?v=vvBkCJtw1rI&t=20s)

## Derive physical exergy

Let $E=U+E_{\mathrm{kin}}+E_{\mathrm{pot}}$ be stored energy of a fixed mass and $S$ its entropy. Subscript $0$ denotes the physical dead state of that same mass. Consider a coupled process that takes the mass from its current state to the dead state, exchanges heat $Q$ only with the reference environment, and delivers useful work. The first law gives $W=E-E_0+Q$. The combined entropy balance gives $S_{\mathrm{gen}}=S_0-S-Q/T_0$. Substitute $Q=T_0(S_0-S-S_{\mathrm{gen}})$ and subtract the ambient displacement work $p_0(V_0-V)$:

$$
W_u=(E-E_0)+p_0(V-V_0)-T_0(S-S_0)-T_0S_{\mathrm{gen}}.
$$

Define physical exergy $B=(E-E_0)+p_0(V-V_0)-T_0(S-S_0)$. Since $S_{\mathrm{gen}}\ge0$, $W_u\le B$, and the reversible limit realizes the bound when suitable reversible interactions are available. For the same endpoints and the same exergy transfer by heat, the reversible useful work exceeds the actual useful work by $B_{\mathrm{dest}}=T_0S_{\mathrm{gen}}$. Heat transfer at $T_0$ carries zero exergy, so its magnitude can differ between those paths. [Exergy, Part 2](https://www.youtube.com/watch?v=Q4M_IjgkyL0&t=20s) · [MIT 2.43, forms of availability](https://ocw.mit.edu/courses/2-43-advanced-thermodynamics-spring-2024/mit2_43_s24_lec08.pdf)

## Show why hot and cold bodies both offer work

Let a body of mass $m$ have constant specific heat $c$ and negligible volume change. Its thermal energy difference from ambient is $mc(T-T_0)$ and its entropy difference is $mc\ln(T/T_0)$. Denote the absolute temperature ratio by $r=T/T_0$. Then

$$
B=mcT_0(r-1-\ln r).
$$

For $r>0$, $\ln r\le r-1$, with equality only at $r=1$. This establishes nonnegativity even when cooling the environment supplies energy to warm a cold body. Expanding near $r=1$ gives $B\approx mc(T-T_0)^2/(2T_0)$ to lowest nonzero order. Thermal energy relative to ambient is linear in the temperature gap. Reversible work potential is quadratic near equilibrium.

The lecture also studies compressed air at ambient temperature. For an ideal gas at $T_0$, define pressure ratio $r_p=p/p_0$ and specific gas constant $R$. Then $E-E_0=0$, $p_0(V-V_0)=mRT_0(1/r_p-1)$ and $S-S_0=-mR\ln r_p$. Hence $B=mRT_0(\ln r_p+1/r_p-1)$. Differentiating the bracket gives $(r_p-1)/r_p^2$ and therefore a global minimum at $r_p=1$. A pressure below ambient also permits work in the reversible construction. [Part 2, compressed air at ambient temperature](https://www.youtube.com/watch?v=Q4M_IjgkyL0&t=460s)

The lecture's 10 m³ tank starts at 1 MPa and 298 K, with the environment at 100 kPa and the same temperature. Treat the air inventory as a closed mass in the reversible work calculation. Since $mRT_0=pV=10{,}000\,\mathrm{kJ}$ and $r_p=10$, the initial availability is $10{,}000(\ln 10+0.1-1)=14.026\,\mathrm{MJ}$. Isothermal reversible expansion supplies $mRT_0\ln 10$ of total work. Displacing the atmosphere over the 90 m³ volume increase consumes 9 MJ, leaving the useful work above. A rigid tank discharging through a turbine is a different control-volume process. Stopping its discharge at ambient pressure can leave a cold residual inventory with work potential. [Part 2, tank setup and comparison](https://www.youtube.com/watch?v=Q4M_IjgkyL0&t=340s)

The positive thermal and volume contributions also explain the exergy contours around the dead state. Consider ideal air with constant specific heat at fixed volume $c_v$, specific volume $v=V/m$, and dead-state specific volume $v_0=RT_0/p_0$. With kinetic and gravitational energy omitted, $u-u_0=c_v(T-T_0)$ and $s-s_0=c_v\ln(T/T_0)+R\ln(v/v_0)$. Write $\theta=T/T_0$ and $\nu=v/v_0$. Substitution into closed-system exergy gives

$$
\frac{B}{m}=c_vT_0(\theta-1-\ln\theta)+RT_0(\nu-1-\ln\nu).
$$

Each term has its minimum at a ratio of one. At fixed volume, differentiating with respect to $T$ gives $c_v(1-T_0/T)$, so warming from below ambient decreases availability until the dead-state temperature is reached. At fixed temperature, compressing from $v>v_0$ can similarly reduce availability. The work that comes in across this boundary and the exergy destroyed inside it enter the balance as separate terms. [Part 2, availability contours](https://www.youtube.com/watch?v=Q4M_IjgkyL0&t=1240s)

## Track exergy carried by heat and useful work

At a boundary with absolute temperature $T_b$, an incremental heat input $\delta Q$ carries incremental exergy $(1-T_0/T_b)\delta Q$. To obtain the factor, operate a reversible engine between source $T_b$ and ambient $T_0$. Entropy balance fixes rejected heat to $(T_0/T_b)\delta Q$, and the first law gives the work difference. For heat entering at $T_b<T_0$, the multiplier is negative. Adding heat to a cold body while it remains below ambient can reduce its work potential. Evaluate the factor locally when temperature varies.

For a closed system between two arbitrary states with heat input and useful work output,

$$
\Delta B=\int(1-T_0/T_b)\,\delta Q-W_u-T_0S_{\mathrm{gen}}.
$$

Insert the energy and entropy balances into $\Delta B=\Delta E+p_0\Delta V-T_0\Delta S$ to derive the result. In an isolated composite of fixed total volume, $\Delta E=\Delta V=0$ and $\Delta S=S_{\mathrm{gen}}$, so $\Delta B=-T_0S_{\mathrm{gen}}\le0$. Energy is conserved while exergy is destroyed. [Part 2, isolated system](https://www.youtube.com/watch?v=Q4M_IjgkyL0&t=880s) · [Part 3, balance](https://www.youtube.com/watch?v=ovsdDMvXmPw&t=1040s)

## Compare work output and input with their reversible benchmarks

Call the exergy input with heat $B_Q=\int(1-T_0/T_b)\,\delta Q$. For fixed end states and fixed $B_Q$, the balance gives $W_u=W_{u,\mathrm{rev}}-B_{\mathrm{dest}}$, with $W_{u,\mathrm{rev}}=B_1-B_2+B_Q$. For a device delivering positive useful work, its second-law efficiency is $W_u/W_{u,\mathrm{rev}}=1-B_{\mathrm{dest}}/W_{u,\mathrm{rev}}$. For a work-consuming device the reversible input magnitude is $-W_{u,\mathrm{rev}}$ and the actual input is $-W_u=-W_{u,\mathrm{rev}}+B_{\mathrm{dest}}$. Its efficiency uses the reversible magnitude in the numerator and the actual magnitude in the denominator. Both ratios attain one when generation vanishes under the stated comparison.

For a steady mixing or heat-transfer device with no shaft power, a work ratio supplies no useful comparison. Specify the useful increase or recovery of stream exergy and the exergy supplied to deliver it. [Chapter 6](chapter-06-flow-exergy-and-the-exergy-balance.html) applies that rule to flow devices. [Part 3, second-law efficiencies](https://www.youtube.com/watch?v=ovsdDMvXmPw&t=1580s)

## Exercises and worked solutions

### Piston load

A piston delivers 80 kJ of work and expands by 0.25 m³ against 100 kPa ambient. How much useful work is delivered?

**Solution.** If $W=80\,\mathrm{kJ}$ while the gas volume increases by $0.25\,\mathrm{m^3}$ against $100\,\mathrm{kPa}$, $W_u=80-100(0.25)=55\,\mathrm{kJ}$. Accounting only for the load misses the displacement work needed in the gas energy balance.

### Low-grade heat

Compare reversible work from 100 kJ of heat supplied at 600 K or 330 K to a 300 K environment.

**Solution.** A heat source at $600\,\mathrm K$ delivers $100\,\mathrm{kJ}$ to a reversible engine with a $300\,\mathrm K$ sink. The engine rejects $50\,\mathrm{kJ}$ at ambient and produces $50\,\mathrm{kJ}$ of work. A source at $330\,\mathrm K$ delivers the same energy with only $100(1-300/330)=9.09\,\mathrm{kJ}$ of work potential.

### Irreversibility cost

Compare exergy destruction for 0.20 kJ/K of generation at environments of 300 K and 290 K.

**Solution.** A process with $S_{\mathrm{gen}}=0.20\,\mathrm{kJ/K}$ in an environment at $300\,\mathrm K$ destroys $60\,\mathrm{kJ}$ of exergy. At $290\,\mathrm K$ the algebra gives $58\,\mathrm{kJ}$ only if the entropy generation is held fixed. Changing the environment can change the process and therefore the generation itself.

### Cold body near ambient

Use the quadratic approximation to predict the work available from a body with total heat capacity 4.18 kJ/K at 295 K in an environment at 300 K. Compare with the exact expression.

**Solution.** The quadratic prediction is $4.18(5)^2/(2\cdot300)=0.17417\,\mathrm{kJ}$. The exact result $4.18[295-300-300\ln(295/300)]$ is $0.17613\,\mathrm{kJ}$. The difference is about 1.1%, consistent with a small temperature offset.

The [standalone exergy lab](code/chapter_05.py) checks equivalent compressed-gas expressions and shows why an equal hot and cold temperature offset can have unequal exergy. The source lectures supply topic order. The numerical lab and examples use original teaching inputs.
