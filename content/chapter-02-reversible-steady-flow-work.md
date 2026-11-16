---
title: Reversible Steady-Flow Work
lectures: 5–7
summary: Derive the pressure integral for shaft work, compare compression paths, and use both thermodynamic laws to test real equipment.
source: https://www.youtube.com/watch?v=rLxnEV4MLps
---

A compressor must raise air from 100 to 800 kPa. A cooled machine may need less shaft power than an insulated one, even if both machines are reversible internally. The discharge pressure alone leaves the discharge temperature and the heat exchanged with the surroundings unspecified. The choice of thermal path determines the density during compression and therefore the work.

## Shaft work and the pressure integral [Lecture 5 · 1:20](https://www.youtube.com/watch?v=rLxnEV4MLps&t=80)

Enclose the compressor in a fixed control volume. Let $p$ be absolute pressure, $T$ absolute temperature, $v$ volume per unit mass, $h$ specific enthalpy, and $s$ specific entropy. Use $q$ for heat entering per kg of fluid and $w_s$ for shaft work leaving per kg. Consider steady flow with a single inlet and outlet. Assume that changes in kinetic and potential energy can be neglected. The energy balance reads $q-w_s=h_2-h_1$, where subscripts 1 and 2 identify the inlet and outlet.

For a fixed-composition simple compressible substance, the first and second laws applied to a reversible differential change give $du=T\,ds-p\,dv$, where $u$ is specific internal energy. Differentiating the definition $h=u+pv$ gives

$$
dh=du+p\,dv+v\,dp=T\,ds+v\,dp.
$$

Here $pv$ is the flow-work contribution to enthalpy. For an internally reversible adiabatic path, $q=0$ and entropy generation vanishes. The specific entropy stays constant, leaving $dh=v\,dp$. For an internally reversible isothermal path that exchanges heat at the fluid temperature $T$, the entropy balance gives $q=T(s_2-s_1)$. This cancels the integral of $T\,ds$ in $h_2-h_1$. Both paths give

$$
w_s=-\int_{p_1}^{p_2}v\,dp.
$$

An increase in pressure makes this work negative, which represents shaft input. At constant pressure the pressure integral vanishes. The expression refers to steady flow through a device. For comparison, a closed mass with reversible pressure work gives $w_b=\int_1^2 p\,dv$, since boundary displacement determines its energy transfer. Integration by parts gives $w_s=w_b-(p_2v_2-p_1v_1)$ for the paths considered here. Flow work accounts for the difference. [MIT Unified Engineering, thermodynamics notes](https://web.mit.edu/course/16/16.unified/www/FALL/thermodynamics/notes/notes.html)

## Comparing the paths at the same back pressure [Lecture 5 · 6:00](https://www.youtube.com/watch?v=rLxnEV4MLps&t=360)

Use an ideal gas with constant $c_p$, the specific heat at constant pressure, and $R$, the gas constant per unit mass. The ideal-gas law gives $v=RT/p$. Combining that relation and $dh=c_p\,dT$ with the enthalpy differential yields

$$
ds=c_p\,\frac{dT}{T}-R\,\frac{dp}{p}.
$$

For isothermal compression at $T_1$, integrate $RT_1/p$ with respect to pressure. For isentropic compression, integrate $ds=0$ to obtain $T_{2s}=T_1(p_2/p_1)^{R/c_p}$, where $2s$ denotes the isentropic outlet. Then use the adiabatic energy balance for the shaft input. Defining $r_p=p_2/p_1$ gives

$$
w_{\mathrm{in},T}=RT_1\ln r_p,\qquad
w_{\mathrm{in},s}=c_p T_1(r_p^{R/c_p}-1).
$$

For $T_1=300$ K, $r_p=8$, $R=0.287$ kJ/(kg K), and $c_p=1.005$ kJ/(kg K), the two work inputs are 179.04 and 244.49 kJ/kg. The isentropic discharge is at 543.27 K. The isothermal discharge is at 300 K and requires rejection of 179.04 kJ/kg of heat because ideal-gas enthalpy stays constant. Since $T$ rises with $p$ along the isentrope, the isentropic integrand $RT/p$ exceeds its isothermal counterpart at every intermediate pressure. As $r_p$ approaches 1, both work inputs approach zero with the same first-order term $RT_1(r_p-1)$. [NASA Glenn, isentropic compression](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/isentrophic-compression/)

For reversible expansion traversing a pressure drop from a common inlet state, heat addition maintains temperature in the isothermal case. The greater specific volume then yields more work than the isentropic path at the same exit pressure. The comparison assumes the required heat transfer is available. To compare two insulated machines, use the isentropic reference with the common inlet and outlet pressures.

## A cooled throttle [Tutorial 1, Part 1 · 0:20](https://www.youtube.com/watch?v=f714NjxTB8A&t=20)

A refrigerant valve has zero shaft work. At steady state with negligible speed and elevation changes, $h_2=h_1+q$. With heat loss, $q$ is negative. If the pressure and enthalpy at the exit put the refrigerant in the saturation region, set $T_2$ to the saturation temperature at $p_2$. The enthalpy fixes the vapor mass fraction $x_2=(h_2-h_f)/(h_g-h_f)$. Subscripts $f$ and $g$ denote saturated liquid and vapor at the outlet pressure. Use that same mass fraction to compute $s_2=s_f+x_2(s_g-s_f)$.

Take the rounded R-134a teaching inputs $h_1=93.58$ kJ/kg, $s_1=0.3479$ kJ/(kg K), and $q=-0.80$ kJ/kg. At the outlet pressure of 200 kPa the example has $h_f=38.41$, $h_g=244.5$ kJ/kg, $s_f=0.1545$, and $s_g=0.9379$ kJ/(kg K), with saturation temperature $-10.09$ °C. These properties use one common reference convention. Then $h_2=92.78$ kJ/kg, $x_2\approx0.264$, and $s_2\approx0.3612$ kJ/(kg K).

Let $T_b$ be the absolute temperature where heat crosses the boundary. For a boundary extended to a single environment at $T_b=298.15$ K, the entropy generated per kg is $s_2-s_1-q/T_b\approx0.0160$ kJ/(kg K). This choice includes irreversibility outside the valve up to that boundary. A calculation around the valve wall alone requires its heat-transfer-weighted boundary temperature.

## Two ways to close a turbine balance [Tutorial 1, Part 1 · 14:00](https://www.youtube.com/watch?v=f714NjxTB8A&t=840)

In the first case the adiabatic turbine takes steam at 6 MPa and 500 °C and discharges at 100 kPa. Its isentropic efficiency is $\eta_t=(h_1-h_2)/(h_1-h_{2s})=0.77$. Use $h_1=3422$ kJ/kg and $s_1=6.88$ kJ/(kg K) from the slide's rounded tables. At 100 kPa the isentropic reference is inside the saturation dome, with $x_{2s}=(6.88-1.303)/(7.359-1.303)$. Interpolate enthalpy between 417.5 and 2675 kJ/kg to obtain $h_{2s}=2496.44$ kJ/kg. Then $h_2=2709.32$ kJ/kg, above the saturated-vapor enthalpy at 100 kPa. The actual state lies in the superheated region. With 5 MW output, $\dot m=5000/(3422-2709.32)=7.016$ kg/s. The tutorial's interpolation gives $s_2\approx7.445$ kJ/(kg K), hence $\dot S_{\mathrm{gen}}\approx3.96$ kW/K.

In the second case the same inlet steam leaves as saturated vapor at 20 kPa with 4 MW output and 25,000 kg/h flow. The steam tables used in the tutorial give $h_2=2610$ kJ/kg and $s_2=7.98$ kJ/(kg K). The heat rate into the device is $4000+(25000/3600)(2610-3422)\approx-1638.89$ kW. Including the thermal path to a 25 °C ambient gives $\dot S_{\mathrm{gen}}=(25000/3600)(7.98-6.88)-(-1638.89/298.15)\approx13.14$ kW/K using the shown state values. Work output and the specified outlet independently determine the heat rate. [Tutorial 1, Part 1 · 26:40](https://www.youtube.com/watch?v=f714NjxTB8A&t=1600s)

## Check a cooled compressor [Tutorial 1, Part 2 · 0:00](https://www.youtube.com/watch?v=R7ovrLScZ8k&t=0s)

The tutorial slide gives 0.4 kg/s of air at 100 kPa and 20 °C, compressed to 1200 kPa and 300 °C. Heat rejection is 15 kW. With the ideal-gas properties above, shaft input is $0.4(1.005)(300-20)+15=127.56$ kW. At a boundary including the heat path to 20 °C ambient, generation is $0.4[1.005\ln(573.15/293.15)-0.287\ln(12)]+15/293.15\approx0.03543$ kW/K. The gas's entropy flux falls. The rejected heat carries a larger outward entropy flux, so generation is positive.

## Heat exchange inside an insulated boundary [Tutorial 1, Part 2 · 8:20](https://www.youtube.com/watch?v=R7ovrLScZ8k&t=500)

Wrap the boundary around an insulated heat exchanger carrying water and ethylene glycol in separate channels. Let $C_g=\dot m_g c_{p,g}$ and $C_w=\dot m_w c_{p,w}$ be heat capacity rates, in kW/K. Here $\dot m$ is mass flow in kg/s and $c_p$ is specific heat. Assume negligible pressure effects on liquid properties and constant specific heats. For glycol flowing at 2.00 kg/s with specific heat 2.56 kJ/(kg K), cooling from 80 to 40 °C releases 204.8 kW. Heating water from 20 to 55 °C with $c_{p,w}=4.18$ kJ/(kg K) therefore requires $\dot m_w=204.8/(4.18\times35)\approx1.400$ kg/s.

The external heat-transfer term is zero. Each liquid contributes a stream entropy change, computed by integrating $c_p\,dT/T$ at constant pressure. Using the temperatures in kelvin gives

$$
\dot S_{\mathrm{gen}}=
C_g\ln(313.15/353.15)+C_w\ln(328.15/293.15)
\approx0.0445\ \mathrm{kW/K}.
$$

The internal heat exchange contributes to generation because heat flows across a finite temperature difference between the streams. If the boundary follows just one channel, the shared wall appears in that channel’s entropy transfer. The full exchanger balance avoids estimating the wall temperature from inlet and outlet temperatures. Its positive entropy generation is compatible with an energy balance in which the heat rates cancel.

In a final exercise, steam mixes directly with 2.50 kg/s of 20 °C water at 200 kPa and leaves as 60 °C liquid while losing 20 kW to ambient. With the tutorial's rounded steam, cold water, and mixed enthalpies $h_s=2769$, $h_w=83.94$ and $h_e=251.1$ kJ/kg, steam supply is $[20+2.5(h_e-h_w)]/(h_s-h_e)\approx0.174$ kg/s. The outlet mass flow is the sum of the two inlets. Use it with the liquid outlet entropy and deduct the two inlet entropy fluxes and the signed heat entropy flux. At 298.15 K ambient the result is about 0.282 kW/K from the slide properties. [Tutorial 1, Part 2 · 15:20](https://www.youtube.com/watch?v=R7ovrLScZ8k&t=920)

## Numerical laboratory

Run the [Python laboratory](code/chapter_02.py) with a standard Python installation. Its inputs are the compressor inlet temperature, pressure ratio, and ideal-gas constants. It reports the shaft-work inputs and isentropic discharge temperature, then checks the entropy change, the work ordering, and the zero-pressure-rise limit. Unsupported arguments raise a value error. The program uses no network or files.

## Exercises and worked solutions

### Same end pressure and different end state

Explain why the difference of 65.45 kJ/kg between the two compressor work inputs cannot be attributed to irreversibility inside one of the machines.

**Solution.** Both paths were internally reversible. Holding an ideal gas at 300 K during compression requires heat rejection and preserves its enthalpy. Insulation forces all shaft input into the enthalpy rise. Thus the common exit pressure coexists with two different outlet temperatures. At the fixed inlet and pressure ratio, the work difference is $244.49-179.04=65.45$ kJ/kg.

### Reverse the isothermal path

Reverse the reversible isothermal compression from 800 to 100 kPa. State the signs of heat and shaft work in the chosen convention.

**Solution.** Interchanging the integration limits changes the sign, so $w_s=179.04$ kJ/kg. Since the inlet and outlet enthalpies match, $q=w_s$. Heat enters the gas and its entire contribution emerges as shaft work during this open-flow step. Closing the cycle must also restore the inlet pressure.

### Check a throttle mixture

Use the cooled-valve example to test whether an exit enthalpy of 250 kJ/kg at 200 kPa would permit the same quality calculation.

**Solution.** The saturated-vapor endpoint is 244.5 kJ/kg. At 250 kJ/kg the mixture formula would give $(250-38.41)/(244.5-38.41)\approx1.027$. No mass fraction exceeds 1. With this pressure and enthalpy, look up the superheated vapor state on the same property reference.

### Heat exchanger feasibility

Suppose the same hot stream and water inlet were used in a co-current heat exchanger. Can the streams leave at 40 °C for glycol and 55 °C for water?

**Solution.** At the inlet, glycol is hotter. In a passive co-current exchanger the local temperature difference drives heat into water. With both heat capacity rates positive, the difference decreases toward zero from above. Integrating the local energy balances for a positive conductance gives exponential decay of the difference along the exchanger. The proposed exit would require the water to be hotter than the glycol at the same end. Counterflow permits these terminal temperatures because water leaving at 55 °C sees glycol entering at 80 °C and water entering at 20 °C sees glycol leaving at 40 °C.
