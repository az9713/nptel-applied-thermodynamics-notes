---
title: Compressible flow and the stagnation state
lectures: 61–63
summary: Derive the acoustic speed, evaluate density changes, and connect local and stagnation properties.
source: https://www.youtube.com/watch?v=QC2PLN5D3wo
---

An air test stand has a pressure tap in the wall and a forward-facing probe. The wall tap reads 100 kPa where the air is at 300 K and travels at 250 m/s. The probe slows a small part of the stream almost to rest. Interpreting its pressure requires an account of the energy in the motion and of how the gas density changes as pressure rises.

## Density response and the Mach criterion [Part 1 · 3:40](https://www.youtube.com/watch?v=QC2PLN5D3wo&t=220s)

Let $p$ be absolute pressure, $T$ absolute temperature, $\rho$ mass per unit volume, and $s$ entropy per unit mass. The isentropic compressibility $\kappa_s=(1/\rho)(\partial\rho/\partial p)_s$ is the fractional density response per unit pressure during a fixed-entropy perturbation. The isothermal compressibility $\kappa_T$ uses a constant-temperature derivative. For an ideal gas with specific gas constant $R$, the equation of state $p=\rho RT$ gives $\kappa_T=1/p$. For the calorically perfect gas model, specific heats at constant pressure and volume, $c_p$ and $c_v$, are constants with $c_p-c_v=R$. Their ratio $\gamma=c_p/c_v$ is greater than 1.

A compressible fluid can flow with small relative density changes if the pressure changes are small and heat or species changes are negligible. Let $a$ be the acoustic speed and $C$ the local flow speed. With $a^2=(\partial p/\partial\rho)_s$, derived below, we have $\kappa_s=1/(\rho a^2)$. A pressure change of order $\rho C^2/2$ then produces a fractional density change of order $M^2/2$, where $M=C/a$ is the Mach number. The estimate motivates screening near $M=0.3$, at which the exact ideal-air isentropic density increase upon stopping is $4.56\%$. A flow with low inlet Mach can accelerate above the screening value in a restriction. Heating, composition changes, and pressure variation unrelated to local motion can also change density. [Part 1 · 18:20](https://www.youtube.com/watch?v=QC2PLN5D3wo&t=1100s)

## Conservation laws and a weak pressure wave [Part 2 · 0:40](https://www.youtube.com/watch?v=sYF4Kb647mY&t=40s)

Consider a steady one-dimensional stream with a constant cross section and negligible friction, heat transfer, shaft work, and gravity. Let $h$ be enthalpy per unit mass in joules per kilogram. Mass, axial momentum and energy balances give the three constants

$$
\rho C,\qquad p+\rho C^2,\qquad h+C^2/2.
$$

The first two have units of mass flux and pressure. The third has units of energy per unit mass. A smooth solution obeys the differential balances. A shock obeys the same balances across the entire discontinuity and has additional admissibility requirements.

Study a pressure disturbance in the frame attached to the wave. Upstream gas enters at speed $a$, and $d\rho$, $dp$, and $dC$ denote small downstream changes. First-order mass conservation gives $a\,d\rho+\rho\,dC=0$. Because $\rho C$ is constant, first-order momentum conservation can be written $dp+\rho a\,dC=0$. Eliminating $dC$ gives $dp=a^2d\rho$. The energy equation gives $dh+a\,dC=0$. Substitution into the identity $dh=T\,ds+dp/\rho$ gives $T\,ds=0$ at this order. Thus the linear wave samples the isentropic density response.

For a calorically perfect ideal gas, integration of $ds=c_p\,dT/T-R\,dp/p=0$ and the equation of state gives $p/\rho^\gamma$ constant. Differentiation gives

$$
a^2=\left(\frac{\partial p}{\partial\rho}\right)_s
=\frac{\gamma p}{\rho}=\gamma RT.
$$

With $\gamma=1.4$ and $R=287$ J/(kg K), 300 K air has $a=347.19$ m/s. The test stand's local Mach number is 0.7201. With a finite-amplitude compression, the differential acoustic derivation has to give way to the jump conditions. [Part 2 · 6:40](https://www.youtube.com/watch?v=sYF4Kb647mY&t=400s) · [NACA Report 1135, compressible-flow relations](https://www.nasa.gov/wp-content/uploads/2023/03/equations-tables-charts-compressibleflow-report-1135.pdf)

## Sonic and stagnation states [Part 3 · 5:20](https://www.youtube.com/watch?v=tCt7uXNYhzg&t=320s)

The sonic reference state has $M=1$. It may exist at a real constriction or be defined by a hypothetical isentropic continuation of a stream. In the tube's stationary frame, a weak upstream-traveling pressure signal moves at axial speed $C-a$ when the gas moves in the positive direction. The two effects cancel locally at a sonic plane. The nozzle analysis later determines when this condition limits mass flow.

The stagnation state is defined by slowing a parcel to zero speed reversibly and adiabatically, with no shaft work and no change in elevation. Its specific enthalpy is $h_t=h+C^2/2$, and its entropy equals the parcel's static entropy $s$. Subscript $t$ denotes this total state. For constant $c_p$, $h_t-h=c_p(T_t-T)$ and $C^2=M^2\gamma RT$. With $c_p=\gamma R/(\gamma-1)$ this yields

$$
\frac{T_t}{T}=1+\frac{\gamma-1}{2}M^2,\qquad
\frac{p_t}{p}=\left(\frac{T_t}{T}\right)^{\gamma/(\gamma-1)}.
$$

The second formula integrates the isentropic entropy relation along the hypothetical path. For real steam, obtain the stagnation state from the pair $(h_t,s)$ with an appropriate property formulation. The constant-$c_p$ temperature formula only applies to the calorically perfect model. [Part 3 · 11:20](https://www.youtube.com/watch?v=tCt7uXNYhzg&t=680s) · [IAPWS Industrial Formulation 1997](https://iapws.org/technical-guidance/release/IF97-Rev)

## Change the observer [Part 3 · 24:20](https://www.youtube.com/watch?v=tCt7uXNYhzg&t=1460s)

For a stationary probe at 250 m/s relative to the stream, the test stand example gives 331.11 K and 141.25 kPa at the stagnation state. For an observer moving downstream at 100 m/s, the relative speed is 150 m/s. The static pressure and temperature are unchanged, while the total values become 311.20 K and 113.69 kPa. Each value refers to stopping the parcel in the named frame. The probe interpretation assumes accurate local sampling and an effectively isentropic stop. A normal shock ahead of a probe used in supersonic flow reduces stagnation pressure before the fluid reaches the port.

## Numerical laboratory

The [Python laboratory](code/chapter_20.py) accepts static temperature, static pressure, relative velocity, and ideal-gas constants. It evaluates the three states above with a stationary and a moving observer, and verifies the signed-velocity symmetry, energy balance, and zero-speed case. It requires only the Python standard library.

## Problems with worked solutions

### Estimate the density change

For the test stand at 250 m/s, compute $\rho_t/\rho$. Use the measured static and computed stagnation values.

**Solution.** The equation of state gives $\rho_t/\rho=(p_t/p)/(T_t/T)$. The test stand ratios give $1.4125/(331.11/300)\approx1.280$. The roughly 28% increase is incompatible with retaining constant density through the stop at this speed.

### One Mach number and two velocities

Compare two ideal-air streams at $M=0.5$, one at 300 K and one at 600 K.

**Solution.** For fixed $M$ and composition, $C=M\sqrt{\gamma RT}$. Doubling temperature increases speed by $\sqrt{2}$, from 173.59 to 245.50 m/s. The Mach number measures speed relative to the local acoustic scale. An equal ratio across the two streams permits different speeds.

### Recover the incompressible pressure formula

Obtain the first nonzero term of $p_t-p$ in the limit of small $M$.

**Solution.** Expand $(1+(\gamma-1)M^2/2)^{\gamma/(\gamma-1)}$ about $M=0$. The first increment is $\gamma M^2/2$. Since $a^2=\gamma p/\rho$ and $M^2=C^2/a^2$, the pressure increment is $\rho C^2/2$ plus terms of order $pM^4$.

### An upstream disturbance at the throat

A stream moves right at 200 m/s where $a=350$ m/s. What velocity does a weak pressure wave moving against the fluid have in the laboratory? How does this change at the sonic state?

**Solution.** The wave moves at $-350$ m/s relative to the gas. Adding the laboratory gas velocity gives $-150$ m/s, so the wave can reach a location upstream. At a sonic section $C=a$ and the same characteristic has zero local speed in the laboratory.
