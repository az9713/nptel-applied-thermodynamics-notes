---
title: Vapor-Compression Refrigeration
lectures: 38
summary: Reconstruct a vapor-compression cycle from its enthalpies, quantify compressor and exchanger penalties, and separate refrigeration duty from power.
source: https://www.youtube.com/watch?v=zl-D7nlr_NY
---

The plant needs to remove heat at 10 kW from a process enclosure. Two suppliers quote the same cooling duty. One promises a lower electrical load by subcooling the liquid before expansion. To compare the proposals, calculate the cooling effect per kg, how much refrigerant must circulate, and how much work the compressor needs per kg. A change can improve one factor while worsening another.

## The refrigerant loop [Lecture 38 · 1:20](https://www.youtube.com/watch?v=zl-D7nlr_NY&t=80)

Call the refrigerant states 1 at compressor suction, 2 at compressor discharge, 3 after condensation, and 4 after expansion. Let $h_i$ be specific enthalpy in kJ/kg and $s_i$ specific entropy in kJ/(kg K) at state $i$. For steady components with negligible flow-speed or elevation effects, take the compressor and valve as adiabatic, and ignore pressure drops in the heat exchangers. The evaporator pressure $p_e$ is below the condenser pressure $p_c$. The idealized saturation endpoints are vapor at 1 and liquid at 3. Let $q_C$ be positive heat absorbed per kg, $q_H$ positive heat rejected per kg, and $w_{\rm in}$ positive compressor work per kg.

| Device | Pressure and phase behavior | Energy balance in kJ/kg |
| --- | --- | --- |
| Compressor $1\to2$ | Raises the pressure of vapor and typically superheats it | $w_{\rm in}=h_2-h_1$ |
| Condenser $2\to3$ | Rejects heat and condenses refrigerant at high pressure | $q_H=h_2-h_3$ |
| Expansion valve $3\to4$ | Lowers pressure at constant enthalpy | $h_4=h_3$ |
| Evaporator $4\to1$ | Absorbs heat and evaporates the remaining liquid | $q_C=h_1-h_4$ |

No shaft work, heat input, or material energy accumulation is available to change enthalpy across the valve. An adiabatic throttle can still produce entropy. If the outlet lies in the liquid–vapor region, its vapor mass fraction is

$$
x_4=\frac{h_3-h_f(p_e)}{h_g(p_e)-h_f(p_e)},
$$

where $h_f$ and $h_g$ are saturated liquid and vapor enthalpy at $p_e$. Flashing uses part of the liquid's enthalpy to form vapor and brings the remaining liquid to the lower saturation temperature. The mixture formula applies only within the saturation endpoints. On a pressure–enthalpy diagram the valve leg follows a line of constant enthalpy, whereas an ideal expander follows an isentrope and produces shaft work. Two-phase expansion hardware adds complexity, while a valve is simple and regulates refrigerant flow. [Lecture 38 · 7:40](https://www.youtube.com/watch?v=zl-D7nlr_NY&t=460)

## Capacity and compressor efficiency [Lecture 38 · 12:40](https://www.youtube.com/watch?v=zl-D7nlr_NY&t=760)

Use R-134a as a property example. Choose evaporator saturation at $-5$ °C and condenser saturation at $30$ °C. Their approximate pressures are 243 and 770 kPa. On the IIR reference convention, which sets saturated liquid enthalpy to 200 kJ/kg and entropy to 1 kJ/(kg K) at 0 °C, rounded suction vapor enthalpy is $h_1=395.66$ and saturated liquid enthalpy at the condenser exit is $h_3=241.72$ kJ/kg. At $p_c$ and $s=s_1$, the isentropic discharge enthalpy is $h_{2s}=419.56$ kJ/kg. Recompute all of these properties together when changing refrigerant, pressure, or reference convention. Relative enthalpy cancels the arbitrary zero only when all states use one reference. [R-134a property model](https://coolprop.org/fluid_properties/fluids/R134a.html) [NIST fluid properties](https://webbook.nist.gov/chemistry/fluid/index.html.en-us.en)

Define compressor isentropic efficiency $\eta_c=(h_{2s}-h_1)/(h_2-h_1)$. With $\eta_c=0.75$ the actual discharge is $h_2=427.53$ kJ/kg and work is 31.87 kJ/kg. The cooling effect is $q_C=153.94$ kJ/kg. At required load $\dot Q_C=10$ kW, refrigerant flow is $\dot m=\dot Q_C/q_C=0.06496$ kg/s. Multiplying work by flow gives 2.070 kW of shaft input. The condenser must reject 12.070 kW. This is the rate-form closure $\dot Q_H=\dot Q_C+\dot W_{\rm in}$. A plot or property table with a different enthalpy zero should give the same differences to property-model accuracy.

The coefficient of performance for cooling, written $\mathrm{COP}_R$, is useful heat removed divided by compressor work. The running case gives

$$
\mathrm{COP}_R=\frac{q_C}{w_{\rm in}}
=\frac{h_1-h_3}{h_2-h_1}=4.83.
$$

A value above one is possible because the delivered service is moving existing heat. If the service instead is heating at the condenser, the same loop has $\mathrm{COP}_{\rm HP}=q_H/w_{\rm in}=\mathrm{COP}_R+1$. Motor losses and auxiliary inputs such as fans and pumps lower equipment performance relative to these shaft-based values. [Lecture 38 · 16:40](https://www.youtube.com/watch?v=zl-D7nlr_NY&t=1000)

## Temperature lift and exergy [Lecture 38 · 17:20](https://www.youtube.com/watch?v=zl-D7nlr_NY&t=1040)

Let $T_C$ and $T_H$ be cold and hot reservoir temperatures in K, with $T_C<T_H$. For a reversible cycle, cyclic entropy accounting gives $q_H/T_H=q_C/T_C$. Substitute into $w_{\min}=q_H-q_C$ to find

$$
\mathrm{COP}_{R,\rm rev}=\frac{T_C}{T_H-T_C},\qquad
w_{\min}=q_C\left(\frac{T_H}{T_C}-1\right).
$$

If the hot sink is the reference environment, this minimum work is the exergy of the cooling service. The corresponding exergetic efficiency is $\mathrm{COP}_R/\mathrm{COP}_{R,\rm rev}$. A cycle taking heat reversibly from 268.15 K to 303.15 K would have $\mathrm{COP}_{R,\rm rev}=7.66$. With those reservoir temperatures and $T_0=T_H$, the running case has an exergetic efficiency of about 63.1%. When a source or sink sits at a different temperature from the corresponding refrigerant saturation temperature, use the external temperatures for the reversible ceiling.

For each steady component and its thermal contact with a reservoir, write the entropy produced per kg of circulating refrigerant as $s_{\rm out}-s_{\rm in}-q/T_b$, where $q$ enters the component and $T_b$ is the reservoir temperature. Thus

$$
s_{{\rm gen},c}=s_2-s_1,\quad
s_{{\rm gen},\mathrm{cond}}=s_3-s_2+\frac{q_H}{T_H},\quad
s_{{\rm gen},v}=s_4-s_3,\quad
s_{{\rm gen},e}=s_1-s_4-\frac{q_C}{T_C}.
$$

Here the subscripts $c$, $\mathrm{cond}$, $v$, and $e$ identify the compressor, condenser, valve, and evaporator. Multiply each by $T_0\dot m$ for the corresponding exergy destruction rate. The sum of the entropy terms reduces to $q_H/T_H-q_C/T_C$ because every refrigerant state appears once as an inlet and once as an outlet. Condenser desuperheating, the cooling of discharge vapor before it reaches saturation, can generate entropy even when the condensation temperature equals $T_H$. [Lecture 38 · 17:20](https://www.youtube.com/watch?v=zl-D7nlr_NY&t=1040) [MIT Unified Engineering, thermodynamics cycle notes](https://web.mit.edu/course/16/16.unified/www/FALL/thermodynamics/notes/notes.html)

The lecture instead specifies a compressor suction volume flow of 0.004 m³/s and $\eta_c=0.73$. With the R-134a properties used here, the saturated suction density is about 12.08 kg/m³, so $\dot m=0.04831$ kg/s. At the same evaporating and condensing temperatures, this gives 7.44 kW cooling, 1.58 kW shaft input and 9.02 kW heat rejection. With $T_0=T_H=303.15$ K, the compressor, condenser and valve destroy about 0.415, 0.014 and 0.183 kW of exergy, respectively. The idealized evaporator operates at $T_C$ throughout and its term is zero. This property-model recalculation closes the energy balance and makes the compressor the largest source of exergy destruction for these assumptions. [Lecture 38 · 11:40](https://www.youtube.com/watch?v=zl-D7nlr_NY&t=700)

## Finite approaches and liquid subcooling [Lecture 38 · 21:00](https://www.youtube.com/watch?v=zl-D7nlr_NY&t=1260)

To remove heat from an enclosure, the refrigerant evaporates below enclosure temperature. To deliver heat to surroundings, the refrigerant condenses above the effective sink temperature. These finite approaches usually increase the compressor lift. They allow heat to flow through finite exchanger surfaces and cause irreversibility. Suction-line superheat, liquid subcooling, and exchanger pressure losses also move the states away from saturation endpoints. Compressor suction superheat inside the cooled enclosure contributes heat pickup. Heat pickup from a warm pipe outside the enclosure raises suction enthalpy without contributing the same useful process duty.

The lecture's wider-lift example changes the evaporator and condenser pressures to 200 and 900 kPa, respectively, and includes suction superheat and liquid subcooling. It reports a shaft demand of about 2.177 kW and a capacity of 2.184 tons of refrigeration, or about 7.68 kW. The cooling COP is about 3.53, approximately 25% below the lecture's saturation-endpoint benchmark of 4.70. Cooling capacity and COP can move in opposite directions when work per kg rises. [Lecture 38 · 23:00](https://www.youtube.com/watch?v=zl-D7nlr_NY&t=1380)

Return to the 10 kW case. Suppose a separate source of cooling reduces condenser-exit liquid enthalpy to 233.13 kJ/kg while suction and discharge pressures and compressor inlet state stay fixed. The valve outlet enthalpy then also falls to 233.13. The cooling effect rises to 162.53 kJ/kg, lowering flow to 0.06153 kg/s and shaft input to 1.961 kW. The modeled COP rises to 5.10. A whole-plant comparison must count any purchased power or useful sink capacity required to provide the subcooling. If cooling for subcooling comes from a suction-liquid exchanger, the suction state and compressor work also change. [Lecture 38 · 23:40](https://www.youtube.com/watch?v=zl-D7nlr_NY&t=1420)

## Numerical laboratory

Run the [Python laboratory](code/chapter_13.py) with standard Python. It accepts suction enthalpy, isentropic discharge enthalpy, condenser-exit liquid enthalpy, compressor efficiency, and useful load. It reports mass flow, power, heat rejection, and COP for the basic and subcooled states. It checks energy conservation and the expected ordering of COP and flow. Invalid state ordering, efficiency, or load raises a value error. The lab consumes property inputs and performs no property lookup.

## Exercises and worked solutions

### Flash fraction

At evaporator pressure, use $h_f=193.32$ and $h_g=395.66$ kJ/kg to compute the quality after throttling without subcooling.

**Solution.** The valve discharges fluid at $h_4=h_3=241.72$ kJ/kg. Therefore $x_4=(241.72-193.32)/(395.66-193.32)=0.239$. About 24% of the mass reaches the evaporator as vapor. Vaporizing the remaining liquid delivers the useful cooling duty.

### Cooling versus heating service

Determine the heating COP when condenser rejection is useful and there are no other purchased inputs.

**Solution.** Divide 12.070 kW by the same 2.070 kW of shaft power, giving 5.83. The difference from 4.83 equals one because condenser rejection includes the compressor input.

### Gate the subcooling proposal

How much auxiliary power can the proposed subcooling consume before it ceases to save purchased power, assuming identical compressor motor efficiencies of 100% for this check?

**Solution.** Base and subcooled shaft powers differ by $2.070-1.961=0.109$ kW. Any auxiliary consumption greater than that cancels the saving. Identical motor efficiencies below unity would rescale the compressor portion of the purchased-power difference.

### Refrigeration capacity and temperature lift

Express 10 kW in tons of refrigeration using $1\ \mathrm{ton}\approx3.517$ kW. Then explain what raising the sink temperature to 313.15 K does to the reversible COP with a 268.15 K cold reservoir.

**Solution.** The capacity is $10/3.517=2.84$ tons. The reversible COP becomes $268.15/(313.15-268.15)=5.96$ instead of 7.66. Required reversible shaft power at 10 kW increases from about 1.31 to 1.68 kW. An actual comparison needs the new condenser pressure and compressor performance.
