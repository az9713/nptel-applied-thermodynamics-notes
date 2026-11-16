---
title: Modified Brayton Cycles
lectures: 33–34
summary: Quantify how intercooling, reheat, and regeneration interact at fixed compressor inlet temperature, turbine inlet temperature, and overall pressure ratio.
source: https://www.youtube.com/watch?v=tbbWu9G-9MY
---

The gas-turbine candidate for the 100 MW plant has two separate objectives. It needs sufficient net work per kg to keep air handling manageable, and it needs to limit purchased heat. Split compression and expansion can raise the first performance measure while worsening the second. A recuperator, which transfers exhaust heat to compressed air, can improve the second measure when the two streams reach it at useful temperatures.

## Intercooling and the optimal intermediate pressure [Lecture 32 · 20:20](https://www.youtube.com/watch?v=XgrDwGKL1FU&t=1220) [Lecture 33 · 0:00](https://www.youtube.com/watch?v=tbbWu9G-9MY&t=0)

Let the overall pressure ratio be $r_p=p_{\rm high}/p_{\rm low}$, and let $r_1,r_2$ be stage ratios whose product is $r_p$. For cold air at $T_c$ in K, assume both compressors are isentropic and that the intercooler returns the air to $T_c$ before the second stage. Ignore pressure losses, take constant specific heat $c_p$ and heat-capacity ratio $\gamma=c_p/c_v$, and set $a=(\gamma-1)/\gamma$. Then the shaft input in kJ/kg is

$$
w_c=c_pT_c(r_1^a+r_2^a-2).
$$

At a fixed product $r_1^a r_2^a=r_p^a$, the sum is smallest when both factors are equal. This follows from $(r_1^{a/2}-r_2^{a/2})^2\ge0$. Consequently $r_1=r_2=\sqrt{r_p}$ and the intermediate pressure is the geometric mean of the endpoints. For $n$ reversible stages with complete intercooling and equal ratios, $w_c=n c_p T_c(r_p^{a/n}-1)$. Since $n(e^{a\ln(r_p)/n}-1)\to a\ln r_p$, the limiting shaft input is $RT_c\ln r_p$, the isothermal compression result when $R=ac_p$.

For the 300 K case with $r_p=10$, $c_p=1.005$ kJ/(kg K), and $\gamma=1.4$, two equal stages each exit at approximately 416.85 K. Together they need 234.87 kJ/kg, a reduction of 45.74 kJ/kg from single-stage ideal compression. At fixed turbine inlet temperature, the main heater must now begin from the cooler 416.85 K discharge rather than 579.21 K. Additional heat input can exceed the work gained, lowering thermal efficiency. The intercooler is a real heat exchanger with a finite approach temperature and possibly significant pressure drop. Either effect changes the optimum stage split.

## Reheat and useful expansion work [Lecture 33 · 8:20](https://www.youtube.com/watch?v=tbbWu9G-9MY&t=500)

Split the turbine into two stages and restore the temperature to $T_h$ between them without pressure loss. For stage ratios $r_1,r_2$ with $r_1r_2=r_p$, the isentropic shaft output is

$$
w_t=c_pT_h(2-r_1^{-a}-r_2^{-a}).
$$

For fixed product $r_p^{-a}$, the same sum-of-squares argument shows that equal stage ratios maximize this work. With $T_h=1500$ K, equal stages at total ratio 10 each exhaust at 1079.53 K. The second stage contributes a separate enthalpy drop made available by heat added between stages. Reheat also warms the ultimate exhaust relative to the single-stage expansion. Its effect on efficiency depends on both external heating and rejection.

For $n$ equal expansion stages each starting at $T_h$, the work is $n c_pT_h(1-r_p^{-a/n})$. Letting $n$ grow at fixed overall ratio gives $RT_h\ln r_p$, the reversible isothermal expansion output. The limit requires heat supplied all along the expansion. With a finite number of stages the heat enters between turbines and the last stage exhaust remains below $T_h$.

Use $X=r_p^{a/2}$ for the compression temperature factor per stage. In the model combining full intercooling with full reheat, the positive magnitudes are

$$
w_c=2c_p T_c(X-1),\qquad w_t=2c_p T_h(1-1/X),\qquad
q_{H,0}=c_p(T_h-T_cX)+c_p(T_h-T_h/X).
$$

The two terms of $q_{H,0}$ represent the main heater and the reheater. With the running inputs the model yields 610.3 kJ/kg net work and 1511.1 kJ/kg heat input, or 40.39% efficiency. Compare the simple cycle at the same boundary temperatures and pressure ratio, which gives 446.1 kJ/kg and 48.21%. The modified cycle needs roughly 164 kg/s per 100 MW instead of 224 kg/s, but its external heat requirement per MW rises. Compressor and turbine count, flow capacity, and energy cost are separate engineering criteria.

## Regeneration and the temperature gate [Lecture 34 · 4:20](https://www.youtube.com/watch?v=2EDD3tBhzcI&t=260)

Let $T_f$ denote the last compressor discharge and $T_e$ the last turbine exhaust. A passive regenerator can transfer heat to the compressed stream only when $T_e>T_f$. For equal mass flow rates and the same constant $c_p$ on each side, heat exchanger effectiveness $\varepsilon$ is actual recovery divided by the maximum $c_p(T_e-T_f)$. Thus

$$
q_{\rm rec}=\varepsilon c_p\max(0,T_e-T_f),\qquad
q_H=q_{H,0}-q_{\rm rec}.
$$

Here $0\le\varepsilon\le1$. An inactive or bypassed heat exchanger has zero recovery. When pressure drops are zero and turbine inlet temperatures stay fixed, compressor and turbine work are unchanged. Energy conservation requires that external heat rejection also drop by $q_{\rm rec}$. At $\varepsilon=0.8$ the combined cycle recovers 532.8 kJ/kg, giving $q_H=978.3$ kJ/kg and $\eta=62.38\%$. The second turbine inlet remains at 1500 K because the reheater compensates separately. The main heater alone uses the preheated stream. [Lecture 34 · 11:20](https://www.youtube.com/watch?v=2EDD3tBhzcI&t=680)

A regenerator insulated from its surroundings still generates entropy when the streams exchange heat across a finite temperature difference. For the equal-capacity model call their outlet temperatures $T_{f,o}$ and $T_{e,o}$. With negligible pressure drop, the total entropy rise per kg passing each side is

$$
s_{\rm gen}=c_p\ln(T_{f,o}/T_f)+c_p\ln(T_{e,o}/T_e).
$$

Recovered heat and destroyed exergy are different quantities. The entire plant can consume less external exergy while the new regenerator itself generates entropy. The ideal calculation also excludes exhaust-side and compressor-side pressure loss. These losses can change turbine output and compressor input, and can overturn the calculated economic benefit. When absolute temperatures are fixed, a simple ideal Brayton cycle has $T_e=T_h/r_p^a$ and $T_f=T_c r_p^a$. Its temperature gate closes exactly at the simple-cycle maximum-work ratio. With intercooled compression and reheated expansion the two corresponding temperature factors are $\sqrt{r_p^a}$, increasing the range where useful recovery is possible. [Lecture 34 · 17:40](https://www.youtube.com/watch?v=2EDD3tBhzcI&t=1060)

The lecture follows the 300–1300 K, pressure-ratio-30 [air-table example in Chapter 10](chapter-10-brayton-cycles.html#variable-heat-capacities-and-the-air-table-lecture-31-820). In the basic case the compressor discharge is about 770 K and the turbine exhaust is cooler, so heat recovery cannot preheat the air. Intercooling lowers the compressor discharge and reheat raises the exhaust. The lecture compares their separate effects and then combines them with heat recovery. Its second-law column uses the same gross convention, with turbine work as product and compressor input plus source heat exergy as resources. [Lecture 33 · 5:00](https://www.youtube.com/watch?v=tbbWu9G-9MY&t=300) · [Lecture 34 · 18:20](https://www.youtube.com/watch?v=2EDD3tBhzcI&t=1100)

| Air-table cycle | Net work (kJ/kg) | Thermal efficiency | Second-law efficiency |
| --- | ---: | ---: | ---: |
| Basic | 362.70 | 59.8% | 89.1% |
| Intercooling alone | 474.72 | 52.3% | 79.2% |
| Reheat alone | 548.12 | 48.7% | 76.56% |
| Intercooling, reheat and regeneration | 660.14 | 61.36% | 86.1% |

For the last row, use the enthalpy form $q_{\mathrm{rec}}=\varepsilon(h_e-h_f)$ for identical streams with the same mass flow and $h_e>h_f$. This includes variable heat capacities. In the lossless pressure model the recovery does not change the work of either turbine or compressor. The net work of 660.14 kJ/kg divided by external heat input of 1075.92 kJ/kg gives 61.36%.

## Numerical laboratory

Run the [Python laboratory](code/chapter_11.py) with standard Python. Its input is the boundary temperatures in K, the overall pressure ratio, $\varepsilon$, and gas constants. It calculates two-stage shaft work, external heat input, internal recovery, and efficiency. It checks that the two external heat transfers differ by the predicted net work and that changing heat recovery alone leaves shaft work unchanged. Invalid efficiencies or a cycle with nonpositive net work raise a value error.

## Exercises and worked solutions

### Intermediate pressure

For ambient pressure 100 kPa and exit pressure 1000 kPa, select the ideal split with complete intercooling.

**Solution.** The first compressor ratio is $\sqrt{10}=3.1623$, giving 316.23 kPa. The second ratio is $1000/316.23=3.1623$. Equal ratios minimize the sum of the two stage temperature rises under the stated assumptions.

### Temperature feasibility

Can the simple 300–1500 K ideal Brayton cycle at $r_p=25$ regenerate?

**Solution.** With $\gamma=1.4$, the single-stage ratio factor $25^{2/7}\approx2.509$. The cold-side inlet is approximately 753 K, while the hot-side inlet is approximately 598 K. Heat would flow from compressed air to exhaust, defeating the intended duty. The stage calculation must bypass the exchanger or set recovery to zero.

### Recover enough heat to reach 50%

Find the minimum $\varepsilon$ for the running modified cycle to reach 50% efficiency.

**Solution.** With 610.3 kJ/kg of net work, input must be at most 1220.6 kJ/kg. The required recovery is $1511.1-1220.6=290.5$ kJ/kg. Since 80% effectiveness gave 532.8 kJ/kg, the reversible upper bound in this model is $532.8/0.8=666.0$ kJ/kg. Divide to get $\varepsilon_{\min}\approx0.436$. Allowing pressure drop would change the required minimum.

### End temperatures and entropy generation

Explain whether $\varepsilon=1$ implies zero regenerator entropy generation in this specific idealization.

**Solution.** Equal capacity rates and zero losses make the two streams exchange inlet temperatures when $\varepsilon=1$. The sum $c_p\ln(T_e/T_f)+c_p\ln(T_f/T_e)$ is then zero. Counterflow can approach that limit as the local temperature difference tends to zero and the required heat-transfer area tends to infinity. At intermediate effectiveness and nonzero inlet temperature difference the two outlet temperatures remain closer together than the two inlets and the total entropy increases.
