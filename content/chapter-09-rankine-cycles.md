---
title: Rankine Cycles
lectures: 27–29
summary: Reconstruct a steam power cycle, distinguish moisture and efficiency constraints, and quantify how feedwater heating and reheat change the balance.
source: https://www.youtube.com/watch?v=TJVk37kchOA
---

A plant must supply 100 MW of net shaft power from a boiler that can raise steam to 480 °C at 8 MPa. A condenser operating at 10 kPa gives the steam a large expansion range. The plant designer still needs to answer two questions before sizing the equipment. How much steam must circulate, and how much liquid forms during expansion? A smaller condenser pressure can improve the first answer while making the second harder.

## Four devices and two pressures [Lecture 27 · 5:40](https://www.youtube.com/watch?v=TJVk37kchOA&t=340)

Use state 1 at the condenser outlet, state 2 at the pump discharge, state 3 at the turbine inlet, and state 4 at the turbine exhaust. All properties are per kg of circulating water. Let $h$ be specific enthalpy in kJ/kg, $s$ specific entropy in kJ/(kg K), $v$ specific volume in m³/kg, and $p$ absolute pressure. Neglect changes in flow speed and elevation, and treat the devices as steady. The pump and turbine are adiabatic. Neglect pressure drop in the boiler and condenser. Define $w_p$ and $w_t$ as positive pump input and turbine output, and $q_H$ and $q_L$ as positive boiler heat input and condenser rejection.

| Path | Ideal model | Energy per kg |
| --- | --- | --- |
| $1\to2$ | Isentropic pumping of liquid | $w_p=h_2-h_1$ |
| $2\to3$ | High-pressure heating and evaporation | $q_H=h_3-h_2$ |
| $3\to4$ | Isentropic turbine expansion | $w_t=h_3-h_4$ |
| $4\to1$ | Low-pressure condensation | $q_L=h_4-h_1$ |

The steady-flow first law yields each table entry. Summing it over the loop cancels all four enthalpies and leaves $w_{\rm net}=w_t-w_p=q_H-q_L$. Thus $\eta=w_{\rm net}/q_H$. In a temperature–entropy diagram the isentropic paths are vertical. In the idealized fluid path heat equals the integral of $T\,ds$, where $T$ is the fluid temperature in K. The enclosed area gives net work because the loop restores the fluid state. Heat exchange across a finite source-to-fluid temperature difference can still generate entropy outside that fluid path.

For the liquid pump, $dh=T\,ds+v\,dp$ and $ds=0$. With $v$ nearly constant, $w_p\approx v_1(p_2-p_1)$. Input pressure in kPa gives work in kJ/kg. The same equation explains why replacing liquid with vapor would make compression expensive: the volume passing through the pressure rise would be much larger. At the other end of the cycle, determine state 4 from $s_4=s_3$ at $p_4$. In the saturation region,

$$
x_4=\frac{s_3-s_f}{s_g-s_f},\qquad h_4=h_f+x_4(h_g-h_f).
$$

Here $x_4$ is the vapor mass fraction and $f,g$ denote saturated liquid and vapor at $p_4$. A computed $x_4$ outside $[0,1]$ calls for a single-phase property calculation at the given pressure and entropy. The [IAPWS-IF97 formulation](https://iapws.org/technical-guidance/release/IF97-Rev) defines property relations for the saturation endpoints and the superheated state on a consistent reference.

## Sizing the plant and checking moisture [Lecture 27 · 19:20](https://www.youtube.com/watch?v=TJVk37kchOA&t=1160)

In the 8 MPa example take rounded properties $h_1=191.81$, $h_2=199.87$, $h_3=3349.53$, and $h_4=2109.33$ kJ/kg. The condenser endpoints are approximately $h_f=191.81$ and $h_g=2583.89$ kJ/kg. The pump costs 8.06 kJ/kg and the turbine supplies 1240.20 kJ/kg, giving $w_{\rm net}=1232.14$ and $q_H=3149.66$ kJ/kg. The efficiency is 39.12% and the steam flow for 100 MW is $100{,}000/1232.14=81.16$ kg/s. The turbine exhaust is approximately 80.2% vapor by mass. An efficiency calculation alone would have missed nearly 20% liquid by mass at the exit.

Superheat moves the turbine inlet above the saturation temperature at boiler pressure. An increase in $s_3$ raises $x_4$ at a fixed condenser pressure when the exhaust remains in the dome. It also changes both $w_t$ and $q_H$. Their ratio improves when the additional net work per additional boiler heat exceeds the original efficiency. Boiler pressure, condenser pressure, and superheat therefore need a joint search under an exhaust moisture constraint and a materials temperature limit. The NPTEL comparison at fixed boiler pressure follows these changes in work, thermal efficiency, and vapor fraction. [Lecture 27 · 25:20](https://www.youtube.com/watch?v=TJVk37kchOA&t=1520)

For a single heat source at absolute temperature $T_H$, its exergy input per kg is $(1-T_0/T_H)q_H$ relative to an environment at $T_0$. Changing the source temperature changes that denominator even at fixed heat duty. Thermal efficiency and exergetic efficiency can move in different directions. A plant with distributed heat sources must sum or integrate their separate exergy transfers.

## Open and closed feedwater heating [Lecture 28 · 3:40](https://www.youtube.com/watch?v=yE58JznEXT0&t=220)

Bleed a fraction $y$ of each kg leaving the boiler at an intermediate turbine pressure. An open heater mixes this bleed stream at enthalpy $h_b$ with $(1-y)$ kg of condensed feedwater at enthalpy $h_c$, also pumped to that pressure. Let $h_m$ be the mixed outlet enthalpy, usually chosen as saturated liquid at the heater pressure in the ideal model. An adiabatic heater with no shaft work gives

$$
y h_b+(1-y)h_c=h_m,\qquad
y=\frac{h_m-h_c}{h_b-h_c}.
$$

With $h_b=2650$, $h_c=192.31$, and $h_m=640.09$ kJ/kg, the illustrative bleed is 18.22%. Every kg expands through the high-pressure turbine stage, and 0.818 kg continues through the low-pressure stage. The condenser and the pump upstream of the mixer handle that smaller mass. The pump downstream of the mixer handles the full kg. Relative to a turbine without bleed at the same stage states, the loss of low-pressure turbine work is $y(h_b-h_4)$. Raising feedwater temperature reduces the boiler heat requirement. A fair comparison counts both changes.

A closed feedwater heater transfers heat across a wall. The condensate and feedwater may operate at different pressures, so mixing does not set the pressure of the feedwater. For idealized negligible heat loss, $y(h_b-h_d)=h_{\rm fw,out}-h_{\rm fw,in}$ when a full kg of feedwater passes through and the bleed drains at $h_d$. Drain routing changes the downstream balances. A trap to a lower pressure retains drain enthalpy and may cause partial flashing. Pumping the drain forward adds shaft input. [Lecture 29 · 0:20](https://www.youtube.com/watch?v=BI8wXzaq1C0&t=20)

## Reheat and the actual plant layout [Lecture 29 · 7:20](https://www.youtube.com/watch?v=BI8wXzaq1C0&t=440)

Reheat sends intermediate-pressure steam from the high-pressure turbine back through a heater, then to a low-pressure turbine. Call its intermediate enthalpy $h_a$, reheated enthalpy $h_r$, and actual final exhaust enthalpy $h'_4$. For a simple turbine train without bleed, $w_t=(h_3-h_a)+(h_r-h'_4)$ and $q_H=(h_3-h_2)+(h_r-h_a)$. The reheat duty must appear in the denominator. If a bleed upstream of the reheater removes fraction $y$, multiply each downstream term by $1-y$. After reheat, the low-pressure turbine starts at higher entropy when the heater pressure is unchanged. At the same final pressure and ideal expansion, this raises exhaust vapor fraction in the two-phase region.

At the plant scale, multiple turbine casings and different bleed pressures let designers match the temperatures and pressures encountered in heating and expansion. The economizer heats liquid feedwater ahead of evaporation, the superheater raises inlet steam temperature, and the reheater serves the interstage steam path. A deaerator removes dissolved gases from the feedwater train. The 100 MW design can therefore use reheating to address its exhaust constraint and feedwater heating to lower boiler demand, while recalculating required mass flow from the new net specific work. [Lecture 29 · 19:20](https://www.youtube.com/watch?v=BI8wXzaq1C0&t=1160)

## Numerical laboratory

Run the [Python laboratory](code/chapter_09.py) with standard Python. It accepts specific enthalpies in kJ/kg and reports energy balances, efficiency, and open-heater extraction. It checks closure for the cycle and for the mixing heater. Inconsistent enthalpy ordering or nonpositive net work raises a value error. Property flashes, pressure losses, turbine moisture limits, and finite heat-exchanger temperature differences are external to this model.

## Exercises and worked solutions

### Pump work and units

Estimate the pump work for liquid with $v=0.00101$ m³/kg pumped from 10 to 8000 kPa.

**Solution.** The isentropic enthalpy increment is $v\Delta p=0.00101(7990)=8.07$ kJ/kg. Dividing by 1000 again would lose a factor of 1000 because the product already uses kPa and m³.

### Actual turbine and outlet wetness

Use the running example and a turbine isentropic efficiency of 0.88. Find the actual outlet enthalpy and its vapor fraction.

**Solution.** At the same end pressure, turbine efficiency is actual divided by isentropic work, giving $h_{4,a}=3349.53-0.88(1240.20)=2258.15$ kJ/kg. The mixture has $x=(2258.15-191.81)/(2583.89-191.81)=0.864$. The actual exhaust is drier here, while turbine work falls 148.82 kJ/kg. The loss appears in a larger outlet enthalpy and a larger condenser burden.

### Audit an extraction calculation

What loss of turbine work does the illustrative bleed incur when its downstream exhaust would have been at 2109.33 kJ/kg?

**Solution.** Extraction occurs after the high-pressure stage, which still receives the full flow. The lost downstream work is $0.1822(2650-2109.33)\approx98.5$ kJ/kg of total boiler flow. This figure describes one change in the balance. Pump work, boiler duty, and condenser duty also change.

### Determine the value of reheat

A candidate reheat arrangement adds 350 kJ/kg to boiler duty and produces an additional 160 kJ/kg of net work. Does it improve the 39.12% running-case efficiency?

**Solution.** The incremental ratio is $160/350=45.71\%$, above 39.12%. Direct substitution gives $(1232.14+160)/(3149.66+350)=39.78\%$. This test does not establish a feasible exhaust vapor fraction. Compute it from the reheated-state entropy and the condenser pressure.
