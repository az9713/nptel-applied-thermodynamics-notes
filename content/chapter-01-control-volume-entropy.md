---
title: Entropy balances for open systems
lectures: 1, 2, 3, 4
summary: Track entropy carried by heat and flowing matter, identify irreversibility, and test whether a proposed operating state is admissible.
source: https://www.youtube.com/watch?v=h_LAfSgddUw
---

## What an energy balance leaves undetermined

Two insulated air mixers take the same mass flow of hot air and cold air and deliver the same outlet temperature. One mixes streams entering at the same pressure. The other throttles the hot stream before mixing. Under an ideal-gas model the throttle preserves the hot stream's temperature, so both outlet temperatures satisfy the same energy balance. The throttle nevertheless destroys a pressure difference that might have been used to produce work. What quantity records that loss, and where is it generated?

An **energy balance** tracks energy stored inside a boundary or transferred across it. An **entropy balance** also accounts for entropy generated inside that boundary by irreversible processes such as mixing, friction, or heat transfer through a finite temperature difference. This added term can distinguish models that both conserve energy. It also supplies an admissibility test through its nonnegative sign.

The course introduction uses this distinction to motivate second-law analysis of practical devices. It previews more detailed Rankine, Brayton, and vapor-compression cycles as well as air-standard engine models, moist-air processes, combustion, and compressible nozzle flow. The course later develops **exergy**, the maximum useful work available under specified environment and interaction constraints, and uses it in second-law efficiency comparisons. Exergy requires a stated reference environment. This chapter establishes the entropy balance on which that analysis rests. [Course introduction](https://www.youtube.com/watch?v=h_LAfSgddUw&t=0s)

## Choose the control volume before writing a balance

A **material system** follows the same matter through time. A **control volume** is a region selected for analysis, and its boundary is the **control surface**. For this chapter the surface is stationary. A mixer control volume can surround the chamber alone or enclose the upstream throttle too. The chamber-only balance has an inlet downstream of the throttle. Its calculated entropy generation therefore covers mixing inside the chamber. Moving the inlet upstream of the throttle changes the measured inlet state and adds throttling to the generation attributed to the larger region.

Let $m_{\mathrm{CV}}$ denote the mass in the region, in kilograms, and $\dot m$ a nonnegative stream mass flow rate in kilograms per second. Subscripts $i$ and $e$ denote an inlet and an exit. Conservation of mass gives

$$
\frac{d m_{\mathrm{CV}}}{dt}
=\sum_i\dot m_i-\sum_e\dot m_e.
$$

At steady operation the mass inventory and the thermodynamic fields are time independent, so the sums of the inlet and outlet flow rates agree. An individual parcel can still change temperature or pressure as it moves from its inlet to its outlet.

## Derive the entropy balance from a moving material system

The derivation below reconstructs the finite-time argument and its differential limit. [Entropy change of a control volume, Part 1](https://www.youtube.com/watch?v=TnH4Jt-Wyss&t=3s)

Let $s$ denote specific entropy, in $\mathrm{kJ/(kg\,K)}$. The total entropy $S_{\mathrm{CV}}$ is the integral of $s$ over the mass currently inside the control volume. For each heat-transfer patch $j$, $\dot Q_j$ is the rate of heat into the control volume in kilowatts, and $T_j$ is the absolute local boundary temperature in kelvin. Let $\dot S_{\mathrm{gen}}$ denote the entropy generated within the boundary in $\mathrm{kW/K}$.

At time $t$ select the material already in the control volume together with the mass $\dot m_i dt$ about to enter through each inlet. At $t+dt$ the same matter consists of the current contents of the region plus the mass $\dot m_e dt$ that has just departed each exit. Relative to the change in entropy within the control volume, subtract the entering entropy at the initial instant and add the exiting entropy at the final instant. The first-order material entropy change is therefore

$$
dS_{\mathrm{mat}}
=dS_{\mathrm{CV}}+\sum_e s_e\dot m_e\,dt
-\sum_i s_i\dot m_i\,dt .
$$

One-dimensional port values $s_i$ and $s_e$ are uniform or mass-flux-weighted averages. The approximation in the moving-system comparison becomes exact in the differential limit under regular transport. The second law for that material system gives $dS_{\mathrm{mat}}=\sum_j (\dot Q_j/T_j)dt+\dot S_{\mathrm{gen}}dt$. Rearrange to obtain

$$
\frac{dS_{\mathrm{CV}}}{dt}
=\sum_j\frac{\dot Q_j}{T_j}
+\sum_i\dot m_i s_i-\sum_e\dot m_es_e
+\dot S_{\mathrm{gen}},
\qquad \dot S_{\mathrm{gen}}\ge 0 .
$$

Every term has units of energy per time per kelvin. The heat term can have either sign. Shaft work carries energy without a separate entropy transfer term. Dissipation of that work within the boundary generates entropy. If the temperature or heat flux varies over the surface, replace the patch sum by the surface integral of local inward heat flux divided by local absolute temperature.

A common change to the entropy reference of one conserved species leaves the balance invariant. For single-component flow, adding a constant $c$ to every specific entropy increases the storage derivative by $c\,dm_{\mathrm{CV}}/dt$ and the net transport term by the same quantity through the mass balance. The generation rate is therefore independent of that reference choice. [MIT control-volume derivation, equation 8.41](https://web.mit.edu/snively/www/2_005%20Coursenotes-1.pdf)

## Locate irreversibility in steady flow

Under steady conditions the entropy storage term vanishes. For one inlet and one exit with a common mass flow rate $\dot m$,

$$
\dot S_{\mathrm{gen}}=
\dot m(s_e-s_i)-\sum_j\frac{\dot Q_j}{T_j}.
$$

For an adiabatic device the heat-transfer sum vanishes. In that case the entropy of a single stream rises with generation inside the control volume. If an adiabatic device is internally reversible, generation is zero and the stream's specific entropy is unchanged. In a nonadiabatic device $s_e=s_i$ can coexist with positive generation when heat rejection exports the generated entropy.

For a heater that receives steady thermal power $\dot Q$ from a reservoir at $T_H$ and transfers it across an interface whose cooler face is at $T_C<T_H$, consider the region containing just the intervening wall. Take the wall to be steady with zero mass transfer and no other heat exchange. Its heat terms are $\dot Q/T_H$ and $-\dot Q/T_C$, so

$$
\dot S_{\mathrm{gen,wall}}
=\dot Q\left(\frac{1}{T_C}-\frac{1}{T_H}\right).
$$

For $\dot Q=12\,\mathrm{kW}$, $T_H=600\,\mathrm{K}$ and $T_C=400\,\mathrm{K}$, the wall generates $0.010\,\mathrm{kW/K}$. An analysis of the receiving device alone uses $T_C$ for its inlet heat transfer. Moving the boundary outward to include the wall changes that temperature to $T_H$ and adds the computed $0.010\,\mathrm{kW/K}$ to the entropy generation. [MIT heat interactions and boundary temperature](https://ocw.mit.edu/courses/2-43-advanced-thermodynamics-spring-2024/mit2_43_s24_lec05.pdf)

## Extend the boundary to include the surroundings

Part 2 works with both a device boundary and an enclosing balance with an isothermal ambient reservoir. Let $T_0$ denote that reservoir's absolute temperature. Suppose the device exchanges heat only with this reservoir, through a region with negligible storage. Set $\dot Q$ positive for net heat entering the device. The reservoir then gains entropy at rate $-\dot Q/T_0$. Adding that term to the material-system entropy change derived above and dividing by $dt$ gives

$$
\dot S_{\mathrm{gen,total}}
=\frac{dS_{\mathrm{CV}}}{dt}
+\sum_e\dot m_e s_e-\sum_i\dot m_i s_i-\frac{\dot Q}{T_0}.
$$

In steady operation the storage term vanishes. The difference from device-only generation is $\sum_j \dot Q_j/T_j-\dot Q/T_0$. A device with some heat entering through a cold region and other heat leaving through a hot region can have a small net $\dot Q$ and substantial irreversible heat transfer. Local heat flows can cancel while each transfers entropy. With multiple thermal reservoirs, specify each reservoir and its heat transfer separately. [Part 2, reservoir entropy account](https://www.youtube.com/watch?v=be69wsZFyuM&t=720s)

**Original compressor example.** At steady operation an insulated compressor would equate shaft input with the stream's enthalpy rise if kinetic and gravitational energy changes were negligible. Suppose actual shaft input is $23\,\mathrm{kW}$, the enthalpy rise of the stream is $20\,\mathrm{kW}$ on a rate basis, and the outlet stream carries $0.004\,\mathrm{kW/K}$ more entropy than the inlet stream. Shaft input delivers energy to the region, so $\dot Q=20-23=-3\,\mathrm{kW}$. If the rejected heat reaches a $300\,\mathrm{K}$ reservoir, total generation is $0.004-(-3/300)=0.014\,\mathrm{kW/K}$. The device-only value requires the actual boundary heat-flux and temperature distribution or additional assumptions.

For the lecture's R-134a compressor, inlet volume flow is $0.001\,\mathrm{m^3/s}$ and inlet specific volume is $0.1461\,\mathrm{m^3/kg}$, giving $\dot m=0.006845\,\mathrm{kg/s}$. The slide's inlet and outlet enthalpies are 246.4 and 358.9 kJ/kg, and shaft input is 1.0 kW. Hence $\dot Q=\dot m(358.9-246.4)-1.0=-0.2300\,\mathrm{kW}$. The specific entropy rises from 0.9724 to 1.192 kJ/(kg K). The enlarged boundary at $T_0=300.15\,\mathrm K$ gives $\dot S_{\mathrm{gen,total}}\approx2.27\,\mathrm{W/K}$. Recovering the inside-device value would require the local wall temperatures and heat fluxes. The turbine that loses heat uses the same balance with the shaft work directed outward. [Part 2, compressor states](https://www.youtube.com/watch?v=be69wsZFyuM&t=880s) · [Part 2, turbine losing heat](https://www.youtube.com/watch?v=be69wsZFyuM&t=1240s)

The insulated intercooler illustrates a separate feasibility check. The lecture's numbers give an overall entropy residual of $0.0181(0.8312-0.4365)+0.01924(-0.3327)=0.000743\,\mathrm{kW/K}$. Its drawing also pairs an air outlet at 300 K with a cooling-water inlet at 30 °C, or 303.15 K. A passive counterflow exchanger driven by sensible heat transfer can approach the cold inlet temperature from above. Cooling the air below it would require an additional mechanism or different inlet data. A positive overall residual alone cannot certify that these end states are realizable in the pictured device. [Part 2, intercooler](https://www.youtube.com/watch?v=be69wsZFyuM&t=280s)

## Solve the running mixer problem

Assume dry air at fixed composition can be modeled as an ideal gas with constant specific heat at constant pressure $c_p=1.005\,\mathrm{kJ/(kg\,K)}$ and specific gas constant $R=0.287\,\mathrm{kJ/(kg\,K)}$. Denote absolute temperature by $T$, absolute pressure by $p$, specific volume by $v$, and specific enthalpy by $h$. In this model $dh=c_p\,dT$ and $pv=RT$. The Gibbs relation $T\,ds=dh-v\,dp$ gives

$$
ds=c_p\frac{dT}{T}-R\frac{dp}{p},
\qquad s_b-s_a=c_p\ln\frac{T_b}{T_a}-R\ln\frac{p_b}{p_a}.
$$

Each logarithm has a dimensionless argument formed from absolute values in consistent units. At constant enthalpy, ideal-gas temperature remains fixed, and a pressure drop increases specific entropy. Real-fluid temperature can change in a throttle because real-fluid enthalpy generally depends on pressure as well as temperature.

Feed the chamber with $1\,\mathrm{kg/s}$ each at $400$ and $300\,\mathrm{K}$, both at $100\,\mathrm{kPa}$. There is no shaft work or heat transfer, and changes in kinetic and gravitational energy are negligible. Conservation of mass gives $2\,\mathrm{kg/s}$ at the outlet. Conservation of energy gives

$$
2c_p T_e=c_p(400+300),\qquad T_e=350\,\mathrm K .
$$

Here the numerical factors multiplying enthalpy are mass flow rates in $\mathrm{kg/s}$. Take the chamber outlet to be at $100\,\mathrm{kPa}$. Adding the stream entropy changes gives

$$
\dot S_{\mathrm{gen,chamber}}
=(1\,\mathrm{kg/s})c_p
\left(\ln\frac{350}{400}+\ln\frac{350}{300}\right)
=0.02072\,\mathrm{kW/K}.
$$

One stream loses entropy while warming the colder stream. Their sum is positive. For equal flows at the same pressure, this result is the logarithm of the square of the arithmetic mean divided by the product of the temperatures. The arithmetic mean exceeds or equals the geometric mean and equality occurs only when both temperatures coincide.

Now feed hot air at $200\,\mathrm{kPa}$ through an upstream adiabatic throttle that drops it to $100\,\mathrm{kPa}$. Under the ideal-gas and negligible velocity-change assumptions the throttle leaves its temperature at $400\,\mathrm K$. It adds $(1\,\mathrm{kg/s})R\ln(2)=0.19893\,\mathrm{kW/K}$. The chamber alone still generates $0.02072\,\mathrm{kW/K}$. The larger region generates $0.21966\,\mathrm{kW/K}$ when rounded after addition. One calculation using just the external inlet and exit states reproduces the sum because the internal stream that joins the throttle to the chamber cancels.

Part 3 begins with a second mixing chamber. All ports are at 200 kPa. Liquid water enters at 30 °C and 5 kg/s, steam enters at 200 °C, and the outlet is liquid at 80 °C. Heat rejection to the 27 °C surroundings is 10 kW. Write $h_w,h_s,h_e$ for the water, steam and outlet specific enthalpies. The outlet flow is $5+\dot m_s$ in kg/s, so the steady energy balance with negligible kinetic and gravitational energy changes gives

$$
\dot m_s=\frac{10+5(h_e-h_w)}{h_s-h_e}.
$$

Evaluating the three states with IAPWS-IF97 gives $h_w=125.924$, $h_s=2870.779$, and $h_e=335.070$ kJ/kg. The required steam flow is $0.41635\,\mathrm{kg/s}$. The corresponding specific entropies are $s_w=0.436733$, $s_s=7.508113$, and $s_e=1.075291$ kJ/(kg K). Inserting these in $(5+\dot m_s)s_e-5s_w-\dot m_s s_s+10/300.15$ gives $0.54782\,\mathrm{kW/K}$ for the enlarged region. The lecture slide uses a different steam entropy at the stated pressure and temperature and reports about $0.538\,\mathrm{kW/K}$. The recalculation uses one consistent property formulation for all ports. [Part 3, steam and water mixer](https://www.youtube.com/watch?v=bvY3LzTDqMk&t=5s) · [IAPWS-IF97](https://iapws.org/technical-guidance/release/IF97-Rev)

## Retain entropy storage during a transient

Part 3 considers an insulated rigid tank that discharges air while an internal electrical heater keeps the gas at constant temperature. Choose the tank boundary upstream of any appreciable pressure drop, and assume the contents stay uniform so the escaping gas crosses the boundary with the tank's instantaneous specific entropy $s$. For mass $m$ in the tank, the entropy inventory is $ms$. With no inlet the mass balance gives $dm/dt=-\dot m_e$. Because the tank is insulated, the entropy balance reduces to

$$
\frac{d(ms)}{dt}=-\dot m_es+\dot S_{\mathrm{gen}},
\qquad
\dot S_{\mathrm{gen}}=m\frac{ds}{dt}.
$$

The entropy carried out cancels the loss of stored entropy associated simply with the departing mass. For a well-mixed ideal gas at fixed absolute temperature $T$ and tank volume $V$, $ds=-R\,dp/p$ and $m=pV/(RT)$. A pressure drop from $p_1$ to $p_2$ therefore generates

$$
S_{\mathrm{gen}}=-\frac{V}{T}\int_{p_1}^{p_2}dp
=\frac{V(p_1-p_2)}{T}.
$$

For $V=1\,\mathrm{m^3}$, $T=300\,\mathrm K$, $p_1=1000\,\mathrm{kPa}$ and $p_2=100\,\mathrm{kPa}$, generation inside this boundary is $3.00\,\mathrm{kJ/K}$. Multiplying by $T$ gives $900\,\mathrm{kJ}$ of electrical input, also obtained from the first law because each kilogram carries out enthalpy $h$ while the stored energy decreases by its internal energy $u$. Their difference is $h-u=RT$ per kilogram. The external jet or valve can add entropy outside the chosen boundary. The pressure drop formula applies to this fixed-temperature, internally heated model.

The lecture's second transient uses a rigid tank at constant pressure, a reservoir that supplies heat, and saturated liquid leaving the outlet. Let $m_1,m_2$ be the initial and final tank masses, $u_1,u_2$ the initial and final specific internal energies, $s_1,s_2$ the initial and final specific entropies of the tank contents, and $h_f,s_f$ the constant specific enthalpy and entropy of the saturated liquid withdrawn. Take $Q$ positive for heat supplied to the tank. With no shaft work and negligible bulk kinetic and gravitational energy changes, the integrated energy balance yields $Q=m_2u_2-m_1u_1+(m_1-m_2)h_f$. For an expanded boundary reaching the constant-temperature reservoir, the corresponding entropy account gives

$$
S_{\mathrm{gen,total}}
=m_2s_2-m_1s_1+(m_1-m_2)s_f-\frac{Q}{T_0}.
$$

The constant pressure and fixed volume give a useful simplification. The total enthalpy change equals the total internal energy change because $pV$ is constant. Write each inventory as liquid plus vapor. The saturated liquid withdrawn cancels the corresponding liquid term in the inventory change. If $\Delta m_g$ is the gain in vapor mass and $h_g$ denotes saturated-vapor enthalpy, then $Q=\Delta m_g(h_g-h_f)$. The same decomposition gives $m_2s_2-m_1s_1+(m_1-m_2)s_f=\Delta m_g(s_g-s_f)$, where $s_g$ is saturated-vapor entropy. At liquid–vapor equilibrium the specific Gibbs energies are equal, so $h_g-h_f=T_{\mathrm{sat}}(s_g-s_f)$ for saturation temperature $T_{\mathrm{sat}}$. The enlarged balance becomes

$$
S_{\mathrm{gen,total}}
=Q\left(\frac{1}{T_{\mathrm{sat}}}-\frac{1}{T_0}\right).
$$

In the lecture's 0.600 m³ tank with 8.00 kg initially at 20 bar, use the saturation specific volumes $v_f=0.00117675$ and $v_g=0.09958054\,\mathrm{m^3/kg}$. The initial vapor mass fraction is $(0.600/8.00-v_f)/(v_g-v_f)=0.75021$. Final mass is $0.600/v_g=6.02527$ kg, so $1.97473$ kg of liquid leaves. The small increase in vapor mass takes $44.63$ kJ at $T_{\mathrm{sat}}=485.53$ K. With the reservoir at $523.15$ K the calculated total generation is $6.61$ J/K using IAPWS-IF97. The shorter expression avoids subtracting large rounded inventory terms. It describes the equilibrium tank and its thermal path. Downstream pressure loss after saturated liquid crosses the selected outlet can add generation outside it. [Part 3, heated air discharge](https://www.youtube.com/watch?v=bvY3LzTDqMk&t=300s) · [Part 3, draining a two-phase tank](https://www.youtube.com/watch?v=bvY3LzTDqMk&t=560s)

## Read the captions against the balances

| Recording | Topic locators | Editorial treatment |
| --- | --- | --- |
| Introduction | [00:03](https://www.youtube.com/watch?v=h_LAfSgddUw&t=3s) prerequisites, [02:04](https://www.youtube.com/watch?v=h_LAfSgddUw&t=124s) practical devices and efficiencies, [11:00](https://www.youtube.com/watch?v=h_LAfSgddUw&t=660s) entropy outline, [15:01](https://www.youtube.com/watch?v=h_LAfSgddUw&t=901s) exergy, [18:01](https://www.youtube.com/watch?v=h_LAfSgddUw&t=1081s) application modules | Motivation and links between energy and entropy analysis |
| Entropy, Part 1 | [00:03](https://www.youtube.com/watch?v=TnH4Jt-Wyss&t=3s) material-system entropy, [04:00](https://www.youtube.com/watch?v=TnH4Jt-Wyss&t=240s) internal and external irreversibility, [09:00](https://www.youtube.com/watch?v=TnH4Jt-Wyss&t=540s) inlet and outlet parcels, [14:00](https://www.youtube.com/watch?v=TnH4Jt-Wyss&t=840s) local-temperature heat transfer, [17:08](https://www.youtube.com/watch?v=TnH4Jt-Wyss&t=1028s) steady limit | Reconstructed equations and independently checked signs |
| Entropy, Part 2 | [00:03](https://www.youtube.com/watch?v=be69wsZFyuM&t=3s) insulated mixer, [02:01](https://www.youtube.com/watch?v=be69wsZFyuM&t=121s) refrigerant throttle, [05:02](https://www.youtube.com/watch?v=be69wsZFyuM&t=302s) intercooler, [09:01](https://www.youtube.com/watch?v=be69wsZFyuM&t=541s) insulated turbine, [12:01](https://www.youtube.com/watch?v=be69wsZFyuM&t=721s) surroundings, [14:00](https://www.youtube.com/watch?v=be69wsZFyuM&t=840s) compressor, [20:01](https://www.youtube.com/watch?v=be69wsZFyuM&t=1201s) heat-losing turbine | Device and expanded boundaries. An adiabatic steady throttle with no shaft work and negligible kinetic and gravitational energy changes is isenthalpic by energy conservation even when specific volume changes appreciably. Positive generation makes it irreversible. |
| Entropy, Part 3 | [00:05](https://www.youtube.com/watch?v=bvY3LzTDqMk&t=5s) nonadiabatic steam mixer, [04:02](https://www.youtube.com/watch?v=bvY3LzTDqMk&t=242s) storage and mass balance, [05:02](https://www.youtube.com/watch?v=bvY3LzTDqMk&t=302s) electrically heated air tank, [09:00](https://www.youtube.com/watch?v=bvY3LzTDqMk&t=540s) constant-pressure two-phase discharge | Integrated balances and boundary-specific interpretation |

The timed English captions supplied topic order. Selected slides confirm the displayed states and balances for the control-volume derivation, refrigerant compressor, intercooler and water examples. The ideal-gas mixer, heater wall and 23 kW compressor are original teaching examples.

## Numerical lab

Run the [standalone Python program](code/chapter_01.py) with Python 3. It checks the first-law residual for the air mixer and verifies that removing the internal stream from the combined entropy balance preserves the total. For the draining tank it checks that the latent-heat form reproduces the full energy balance with consistent properties.

```text
Outlet temperature: 350.0 K
Mixer entropy generation: 0.02072 kW/K
Throttle entropy generation: 0.19893 kW/K
Combined entropy generation: 0.21966 kW/K
Draining tank: 1.97473 kg out, 44.63 kJ in, 6.61 J/K generated
```

## Problems with worked solutions

### 1. A steady device with an impossible outlet

An adiabatic single-stream device passes $2\,\mathrm{kg/s}$ of air steadily from $400\,\mathrm K$, $200\,\mathrm{kPa}$ to $300\,\mathrm K$, $200\,\mathrm{kPa}$. Use the chapter's constant-property air model. Can a shaft alone make the proposed states possible?

**Solution.** The pressure terms cancel, so the stream entropy changes by $c_p\ln(300/400)=-0.2891\,\mathrm{kJ/(kg\,K)}$. The required generation is $2(-0.2891)=-0.5782\,\mathrm{kW/K}$, which violates the second law. Shaft work cannot export entropy. A heat rejection path or a changed outlet state is required.

### 2. Heat transfer with zero net power

A steady region has no mass flow. It receives $5\,\mathrm{kW}$ through a $500\,\mathrm K$ surface and rejects $5\,\mathrm{kW}$ through a $300\,\mathrm K$ surface. Calculate entropy generation.

**Solution.** Heat cancels in the energy balance. In the entropy balance it is weighted by reciprocal absolute temperatures. The net entropy transfer into the region is $5/500-5/300=-0.006667\,\mathrm{kW/K}$. Steady storage is zero, so entropy generation is $0.006667\,\mathrm{kW/K}$.

### 3. An internally reversible isentropic limit

An ideal gas enters an adiabatic internally reversible device at $400\,\mathrm K$ and $200\,\mathrm{kPa}$ and exits at $100\,\mathrm{kPa}$. Find its outlet temperature under the same air model and compare the direction of the temperature change with the throttle.

**Solution.** Equal specific entropies require $c_p\ln(T_e/400)=R\ln(100/200)$. Thus $T_e=400(1/2)^{R/c_p}\approx328.2\,\mathrm K$. The ideal-gas throttle instead stays at $400\,\mathrm K$ with a positive entropy rise. The isentropic case can realize the temperature drop through shaft work or acceleration, depending on the energy balance and device.

### 4. A wet outlet from an isenthalpic throttle

For an illustrative single-component fluid let the inlet have $h_i=250\,\mathrm{kJ/kg}$ and $s_i=1.10\,\mathrm{kJ/(kg\,K)}$. At the outlet pressure the saturated liquid and vapor properties are $h_f=200$, $h_g=400\,\mathrm{kJ/kg}$ and $s_f=1.00$, $s_g=1.80\,\mathrm{kJ/(kg\,K)}$. The throttle is adiabatic and steady with no shaft work and negligible changes in kinetic and potential energy. Find its outlet quality and specific generation.

**Solution.** Enthalpy is unchanged. The outlet enthalpy lies between the saturation limits. The vapor mass fraction is $x=(250-200)/(400-200)=0.25$. The mass-weighted entropy is $s_e=1.00+0.25(1.80-1.00)=1.20\,\mathrm{kJ/(kg\,K)}$. Generation per unit mass is $s_e-s_i=0.10\,\mathrm{kJ/(kg\,K)}$.

### 5. A falling entropy inventory

For the heated discharge model, compare the initial and final tank masses using $V=1\,\mathrm{m^3}$, $T=300\,\mathrm K$, and pressures of $1000$ and $100\,\mathrm{kPa}$. Can the stored total entropy decrease even while entropy is generated?

**Solution.** The ideal-gas law gives $m_1=1000/(0.287\cdot300)=11.61\,\mathrm{kg}$ and $m_2=1.161\,\mathrm{kg}$. Use an entropy reference where $s_1=1\,\mathrm{kJ/(kg\,K)}$. Then $s_2=s_1+R\ln(10)\approx1.661\,\mathrm{kJ/(kg\,K)}$. The tank inventory decreases from $11.61$ to about $1.93\,\mathrm{kJ/K}$ while $3.00\,\mathrm{kJ/K}$ is generated. The difference is explained by the entropy exported with the discharged material. The reference affects the tank inventory change because mass leaves, while the calculated generation is reference invariant.
