---
title: Air and steam nozzle calculations
lectures: 70–72
summary: Locate a normal shock from back pressure and adapt the nozzle balances to steam properties.
source: https://www.youtube.com/watch?v=HqYbWMEqE-4
---

An air nozzle with exit-to-throat area ratio 3.5 runs from a reservoir at 1 MPa and 500 K. The laboratory can set the back pressure to 20 or 500 kPa. Both settings choke the throat, so both pass the same mass flow. The interior shock occurs at 500 kPa. At 20 kPa the stream expands outside the nozzle. A second nozzle, fed by steam, illustrates which parts of the analysis survive a change of working fluid.

## Bracket the air-nozzle regime [Part 10 · 0:00](https://www.youtube.com/watch?v=HqYbWMEqE-4&t=0s)

Write $A_t$ for geometric throat area, $A_e$ for exit area, $p_{t1}$ for upstream stagnation pressure, $T_t$ for the common stagnation temperature, and $p_b$ for back pressure. In the one-dimensional, inviscid, adiabatic model with negligible shaft work, use $\gamma=1.4$ for air. The area–Mach relation gives both a subsonic and a supersonic root at the exit for $A_e/A_t=3.5$. The downstream state can also be subsonic following an interior normal shock.

There are three useful pressure landmarks. The subsonic isentropic root at the exit of a nozzle with a sonic throat gives first choking at $p_b=980.45$ kPa. The supersonic root is $M_e=2.8000$, giving the design exit pressure $p_e=36.85$ kPa. If the normal shock stands just at the exit, multiply that static pressure by the normal-shock pressure ratio to obtain $p_b=330.91$ kPa. Use the same upstream stagnation state for all three checks.

A back pressure of 20 kPa lies below design pressure. The jet is underexpanded and the divergent section has the isentropic supersonic exit at 36.85 kPa. By contrast 500 kPa is between the shock-at-exit and first-choking limits, so the ideal model selects an internal shock and a subsonic exit at the imposed 500 kPa. [Part 10 · 4:40](https://www.youtube.com/watch?v=HqYbWMEqE-4&t=280s)

## Locate the internal shock [Part 10 · 9:40](https://www.youtube.com/watch?v=HqYbWMEqE-4&t=580s)

Pick a trial shock section with area $A_s$ between throat and exit. On the upstream isentrope, $A^*=A_t$, where the starred area denotes the area that carries the current mass flow at Mach 1 and the local stagnation state. Invert the supersonic area–Mach branch at $A_s/A_t$ to obtain the Mach number $M_a$ immediately before the jump. The normal-shock relations give the total pressure ratio $\chi=p_{tb}/p_{ta}$, where $a$ and $b$ denote the states before and after the shock.

For the same gas and $T_t$, the choked mass flux is proportional to total pressure. Since mass flow is conserved, the downstream hypothetical sonic area is $A^*_b=A_t/\chi$. Use the subsonic area–Mach root at $A_e/A^*_b=(A_e/A_t)\chi$ to compute the candidate exit Mach number. Then compare the predicted exit pressure with $p_b$:

$$
\frac{p_e}{p_{t1}}=\chi
\left(1+\frac{\gamma-1}{2}M_e^2\right)^{-\gamma/(\gamma-1)}.
$$

Numerical bisection on $A_s/A_t$ at $p_b/p_{t1}=0.5$ yields $A_s/A_t=2.4118$, $M_a=2.4039$, and $M_e=0.3272$. For this smooth diverging section, increasing the trial shock area makes the upstream Mach number larger and the total-pressure ratio smaller. The exit area ratio on the downstream isentrope then decreases, making the subsonic exit Mach larger. Both factors reduce the predicted exit pressure, which makes the residual suitable for bisection. Converting the area ratio into an axial location also requires the nozzle's area profile. [Part 10 · 13:00](https://www.youtube.com/watch?v=HqYbWMEqE-4&t=780s) · [NACA Report 1135](https://www.nasa.gov/wp-content/uploads/2023/03/equations-tables-charts-compressibleflow-report-1135.pdf)

![The computed exit pressure falls as the trial shock moves into larger sections, crossing the target pressure ratio of 0.5 at a shock area of 2.412 times the throat area.](figures/shock-pressure.png)

## Critical pressure for a steam isentrope [Part 11 · 7:40](https://www.youtube.com/watch?v=xffwQnnoLQw&t=460s)

For a steam reservoir with stagnant enthalpy $h_0$ and specific entropy $s_0$, a smooth equilibrium isentrope through static pressure $p$ gives $h(p,s_0)$ and $v(p,s_0)$, where $v$ is the volume per kilogram. Compute the axial speed and mass flux $G$ with

$$
C(p)=\sqrt{2[h_0-h(p,s_0)]},\qquad
G(p)=\frac{C(p)}{v(p,s_0)}.
$$

Use J/kg for the enthalpy difference to recover m/s. In a convergent nozzle in this model, the maximum of $G(p)$ along the reservoir isentrope sets the choking pressure. This procedure can use tables or an equation of state. In the two-phase equilibrium region, recover the vapor mass fraction from $s_0=s_f+x(s_g-s_f)$ at the trial pressure, and use the same fraction in the $h$ and $v$ balances. [IAPWS Industrial Formulation 1997](https://iapws.org/technical-guidance/release/IF97-Rev)

The lecture also approximates a segment by $pv^n=p_0v_0^n$, where $p_0$ and $v_0$ are reservoir pressure and specific volume and $n>1$ is a fitted expansion exponent. With $r=p/p_0$, we have $v=v_0r^{-1/n}$. Integrating $dh=v\,dp$ along this model isentrope gives

$$
h_0-h=\frac{n}{n-1}p_0v_0\left(1-r^{(n-1)/n}\right).
$$

Substitution into the flow expression shows that $G^2$ is proportional to $r^{2/n}(1-r^{(n-1)/n})$. Setting its derivative with respect to $r$ to zero gives $r^{(n-1)/n}=2/(n+1)$. Thus

$$
r^*=\left(\frac{2}{n+1}\right)^{n/(n-1)}.
$$

At the maximum, substitution gives $C^2=npv$. On the fitted isentrope, $a^2=(\partial p/\partial\rho)_s=npv$, since $\rho=1/v$. The maximum therefore corresponds to the model sonic state. The fitted exponent varies with the state range and is a teaching approximation. Real rapid expansions can show delayed condensation and slip between droplets and vapor, which violate the equilibrium, uniform-velocity model. [Part 11 · 11:20](https://www.youtube.com/watch?v=xffwQnnoLQw&t=680s)

## Compare an unchoked and a choked steam outlet [Part 12 · 0:00](https://www.youtube.com/watch?v=rHRLM_Zpz4E&t=0s)

The lecture's first example gives wet steam in a chest at 600 kPa with vapor mass fraction 0.9 and $v_0=0.2845\,\mathrm{m^3/kg}$. The convergent outlet area is $0.002\,\mathrm{m^2}$. Use $n=1.035+0.1(0.9)=1.125$ for this example. The computed sonic pressure is 347.69 kPa. For a 400 kPa back pressure, the steam leaves at 400 kPa, 367.90 m/s and 1.8037 kg/s using the power-law model. For a 300 kPa back pressure the exit is sonic at 347.69 kPa, 425.14 m/s and 1.8401 kg/s. The free jet adjusts to 300 kPa downstream.

Later examples add two useful changes. First, if the stated inlet of a convergent nozzle is already moving, preserve its kinetic energy. Continuity gives $C_1=(A_e/A_1)(v_1/v_e)C_e$, with $A_1$ the inlet area. Substituting into $h_1-h_e=(C_e^2-C_1^2)/2$ determines $C_e$ from the static end states. For the 500-to-300 kPa example the lecture reports about 437 m/s at the exit and 70 m/s at entry. The stagnation enthalpy then follows from $h_{t1}=h_1+C_1^2/2$, while $s_{t1}=s_1$ fixes the stagnation pressure together with $h_{t1}$. [Part 12 · 9:20](https://www.youtube.com/watch?v=rHRLM_Zpz4E&t=560s)

Second, a 700 kPa, 250 °C reservoir expands to a specified in-nozzle exit state at 100 kPa. With the illustrative superheated-steam exponent $n=1.3$, the critical pressure is about 382 kPa. The throat is above the saturation crossing in the lecture's property calculation. Compute the throat using superheated properties, then compute the exit properties using equilibrium tables or a separately checked two-phase approximation. For a given $\dot m$ the sizing relation is $A=\dot m v/C$. Distinguish a specified static exit state from an ambient pressure reached outside the device. [Part 12 · 13:20](https://www.youtube.com/watch?v=rHRLM_Zpz4E&t=800s)

## Numerical laboratory

Run the [Python laboratory](code/chapter_23.py) in a directory containing its two local dependencies, the [normal shock routine](code/chapter_21.py) and [area–Mach solver](code/chapter_22.py). It prints the air-nozzle regime thresholds and internal shock solution, then checks the predicted exit pressure against the target. The steam calculation prints both operating states and verifies that lowering the back pressure further preserves the choked solution. Inputs are in SI units. The lab requires only the Python standard library.

## Problems with worked solutions

### Distinguish a jet pressure from a boundary demand

For the air nozzle, choose the ideal regime at $p_b=70$ kPa.

**Solution.** The pressure is below the 330.91 kPa shock-at-exit threshold and above the 36.85 kPa design point. The model predicts an internal isentropic supersonic exit at 36.85 kPa. The higher ambient pressure makes this jet overexpanded, so it compresses after leaving the nozzle. A large enough mismatch can introduce separation within a real nozzle.

### Compare the two sonic reference areas

A normal shock leaves 70% of its incoming stagnation pressure. Find $A^*_b/A_t$ for the choked nozzle.

**Solution.** With constant mass flow and total temperature, $p_{ta}A_t=p_{tb}A^*_b$. Thus $A^*_b/A_t=1/0.7\approx1.429$. The downstream reference is a mathematical state associated with the new isentrope. The actual geometric throat is unchanged.

### Size a convergent outlet for wet steam

Keep the 600 kPa steam reservoir and $n=1.125$. How much area would pass 0.920 kg/s at a back pressure below 347.69 kPa?

**Solution.** The computed sonic flux is $1.8401/0.002=920.05$ kg/(m² s). The required area is $0.920/920.05\approx0.00100\,\mathrm{m^2}$ in the power-law model. This scales linearly with requested flow at fixed reservoir state.

### Check the pressure at which the property model changes

Assume steam crosses from superheated vapor into the two-phase region at 212 kPa. The approximate sonic pressure is 382 kPa and the specified exit pressure is 100 kPa. Which states require mixture properties?

**Solution.** Pressure falls monotonically from the reservoir on the shock-free expansion considered. At 382 kPa the throat is encountered before the saturation crossing and remains superheated. The 100 kPa exit lies after the crossing and requires mixture properties on the selected isentrope. A single constant exponent across both intervals would require a separate accuracy check.
