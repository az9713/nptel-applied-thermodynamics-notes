---
title: Stagnation pressure and normal shocks
lectures: 64–66
summary: Use energy and entropy to explain stagnation-pressure changes and derive the compressive shock solution.
source: https://www.youtube.com/watch?v=PNRiUi9Brtw
---

A duct brings an air stream at Mach 2 toward a component that needs subsonic flow. A normal shock, a thin compression layer oriented perpendicular to the stream, can achieve that change within a short distance. It raises the wall pressure while lowering the pressure that a reversible diffuser could recover. These two pressures correspond to different thermodynamic states.

## Total-state changes diagnose heat, work, and entropy [Part 4 · 0:00](https://www.youtube.com/watch?v=PNRiUi9Brtw&t=0s)

Let $C$ denote axial speed, $h$ static specific enthalpy in J/kg, and $h_t=h+C^2/2$ [stagnation enthalpy](chapter-20-compressible-flow-and-stagnation.html#sonic-and-stagnation-states-part-3-520). Take $q$ as heat into the fluid and $w_s$ as shaft work leaving the fluid per kilogram. With negligible gravitational energy change the steady energy balance gives $h_{t2}-h_{t1}=q-w_s$. The subscript $t$ indicates an isentropic stop from the local stream state. Its entropy equals the static entropy. For a calorically perfect ideal gas with constant specific heat $c_p$ and specific gas constant $R$, integrating $ds=c_p\,dT_t/T_t-R\,dp_t/p_t$ between those two total states gives

$$
s_2-s_1=c_p\ln(T_{t2}/T_{t1})-R\ln(p_{t2}/p_{t1}).
$$

Here $p_t$ and $T_t$ are stagnation pressure and absolute temperature. In a single-stream adiabatic device, the steady entropy balance gives $s_2-s_1=s_{\rm gen}$, the entropy generated per kilogram. If $T_t$ also stays fixed, positive entropy generation lowers $p_t$. A turbine can lower total pressure by reversible work extraction even while its entropy stays constant. A compressor can raise total pressure while generating entropy if the temperature term dominates. Total pressure alone diagnoses loss only under the accompanying energy and entropy constraints.

On a temperature–entropy diagram an isentropic stop moves vertically to a higher temperature. Along a passive adiabatic duct without shaft work, $T_t$ is constant. That fixes a common sonic temperature $2T_t/(\gamma+1)$, with $\gamma=c_p/(c_p-R)$. A local temperature below the sonic value corresponds to supersonic motion. Across a shock this sonic temperature remains common while the pressure of the sonic reference state changes. On a pressure–specific-volume plot, $p=\text{constant}/v$ for a fixed-temperature ideal gas, with slope $-p/v$. The isentropic slope is $-\gamma p/v$ from $pv^\gamma=\text{constant}$. For real steam use $h_t$ and $s$, with properties read from a fluid model. [Part 4 · 5:00](https://www.youtube.com/watch?v=PNRiUi9Brtw&t=300s) · [Part 4 · 22:40](https://www.youtube.com/watch?v=PNRiUi9Brtw&t=1360s)

At fixed pressure $ds=c_p\,dT/T$, so an isobar has slope $(dT/ds)_p=T/c_p$. At fixed specific volume, $ds=c_v\,dT/T$, so an isochore has the steeper slope $T/c_v$ at the same state, where $c_v=c_p-R$ is the specific heat at constant volume. For a constant-$c_p$ gas, the vertical separation from the static state to its isentropic stagnation state is $C^2/(2c_p)$. Thus a pair of points on that diagram can encode velocity as well as the static and stagnation temperatures. [Part 4 · Diagram slopes and stagnation states](https://www.youtube.com/watch?v=PNRiUi9Brtw&t=340s)

## Derive the compressive jump [Part 5 · 4:40](https://www.youtube.com/watch?v=6lq2dfFuQ0Q&t=280s)

In the stationary shock's frame take states 1 and 2 just outside the thin layer. Assume the cross section is constant, both states are uniform and the layer exchanges negligible heat and shaft work. Let $\rho$ be density, $v=1/\rho$, $M=C/a$ the local Mach number, and $a^2=\gamma p/\rho$. Mass conservation gives $\rho_1 C_1=\rho_2 C_2$. Define $y=v_2/v_1=C_2/C_1$. Momentum conservation then gives

$$
\frac{p_2}{p_1}=1+\gamma M_1^2(1-y).
$$

Energy conservation gives $h_2-h_1=(C_1^2-C_2^2)/2$. With $h=c_pT$ up to an arbitrary reference, $T=pv/R$, and $c_p/R=\gamma/(\gamma-1)$, divide through by $\gamma p_1 v_1$. The result is

$$
\frac{y[1+\gamma M_1^2(1-y)]-1}{\gamma-1}
=\frac{M_1^2}{2}(1-y^2).
$$

Both sides have a factor $1-y$. The trivial root $y=1$ preserves the upstream state. For the nontrivial root cancel that factor and solve the remaining linear equation for $y$. The final ratios are

$$
y=\frac{2+(\gamma-1)M_1^2}{(\gamma+1)M_1^2},\qquad
\frac{T_2}{T_1}=\frac{p_2}{p_1}y,\qquad
M_2^2=\frac{1+(\gamma-1)M_1^2/2}{\gamma M_1^2-(\gamma-1)/2}.
$$

For $M_1>1$, the qualified root has $y<1$, $p_2>p_1$, and $M_2<1$. Admissibility also follows from entropy. With $z=M_1^2$ and $P=p_2/p_1$, the ideal-gas identity gives $(\gamma-1)(s_2-s_1)/R=\ln P+\gamma\ln y$. Differentiating this expression with respect to $z$ gives

$$
\frac{2\gamma(\gamma-1)(z-1)^2}
{[2\gamma z-(\gamma-1)]\,z\,[2+(\gamma-1)z]}.
$$

This derivative is positive for $z>1$. The entropy increase vanishes at $z=1$ and is positive above it. Reversing the compressive shock would decrease entropy at zero heat transfer. The smooth weak-wave limit retains the original acoustic state. [NACA Report 1135, normal-shock relations](https://www.nasa.gov/wp-content/uploads/2023/03/equations-tables-charts-compressibleflow-report-1135.pdf)

## Recover pressure at the cost of total pressure [Part 6 · 2:40](https://www.youtube.com/watch?v=P6HLJKGw2SI&t=160s)

For air with $\gamma=1.4$ and $M_1=2$, the shock gives $M_2=0.57735$, $p_2/p_1=4.5$, $\rho_2/\rho_1=2.66667$, and $T_2/T_1=1.6875$. The two total temperatures agree by the energy balance. To find the total pressures, compute independently on the two sides $p_{tk}=p_k[1+(\gamma-1)M_k^2/2]^{\gamma/(\gamma-1)}$, where $k$ denotes the side. This yields $p_{t2}/p_{t1}=0.72087$ and $s_2-s_1=-R\ln(0.72087)=93.93$ J/(kg K) for $R=287$ J/(kg K).

Take the lecture's 100 kPa and 300 K inlet and its rounded Mach number of 2. The upstream speed is $2\sqrt{1.4(287)(300)}\simeq694.4$ m/s with this gas constant. The downstream speed is $C_2=C_1v_2/v_1\simeq260.4$ m/s. The static state downstream is 450 kPa and 506.25 K, while $T_{t1}=T_{t2}=540$ K. The inlet total pressure is $100(1.8)^{3.5}\simeq782.4$ kPa, giving an outlet total pressure of about 564.0 kPa.

A shock can deliver a large static pressure rise with a short compression distance. An ideal smooth diffuser preserves more of the inlet stagnation pressure for later recovery. A real diffuser introduces wall losses and geometric constraints of its own. Evaluate available length and required total pressure separately. The normal-shock calculation assumes a stationary plane. Real shock structures can depart from it when the flow separates or the shock is oblique. [Part 6 · 8:40](https://www.youtube.com/watch?v=P6HLJKGw2SI&t=520s)

## Numerical laboratory

The [Python laboratory](code/chapter_21.py) returns the downstream Mach number and four downstream-to-upstream ratios from an ideal-gas upstream Mach number and $\gamma$. It verifies momentum and total temperature across the shock, checks the sonic limit, and calculates the entropy increase. The code is valid for a normal shock in a calorically perfect gas and rejects upstream Mach below 1.

## Problems with worked solutions

### Calculate both pressures

If the Mach-2 shock starts at $p_1=80$ kPa, compute $p_2$ and the total-pressure loss as a fraction of $p_{t1}$.

**Solution.** The momentum relation gives $p_2=4.5(80)=360$ kPa. The pressure reduction at the hypothetical stopped state is $1-p_{t2}/p_{t1}=1-0.72087=0.27913$, about 27.9%. Static and total pressures answer different questions, so the signs can differ.

### Find the compression limit

What maximum density ratio does the ideal-gas formula approach as $M_1$ increases for $\gamma=1.4$?

**Solution.** Use $\rho_2/\rho_1=1/y$. Divide numerator and denominator by $M_1^2$ to obtain the limiting ratio $(\gamma+1)/(\gamma-1)=6$. The limiting statement assumes constant $\gamma$ even as temperature increases. A real gas can enter a regime where variable heat capacity and chemical reactions matter.

### Verify stagnation enthalpy

Check the total-temperature conservation at $M_1=2$ using $M_2^2=1/3$ and $T_2/T_1=1.6875$.

**Solution.** The upstream total temperature is $T_1(1+0.2\times4)=1.8T_1$. The downstream value is $1.6875T_1(1+0.2/3)=1.8T_1$. The static temperature rise draws on kinetic energy as the stream slows.

### Distinguish cooling from shock loss

Give a criterion for deciding whether a measured total pressure drop in a duct can be interpreted by $s_2-s_1=-R\ln(p_{t2}/p_{t1})$.

**Solution.** Measure the stagnation temperatures or justify their equality from negligible heat, shaft work, and elevation change. The stated formula also assumes fixed composition and the ideal-gas entropy relation. If $T_{t2}$ differs from $T_{t1}$, include $c_p\ln(T_{t2}/T_{t1})$ for constant $c_p$. Entropy rise then combines entropy transfer with any generation inside the selected boundary.
