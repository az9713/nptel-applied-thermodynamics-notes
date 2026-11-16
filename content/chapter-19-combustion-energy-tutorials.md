---
title: Combustion Energy Tutorials
lectures: 56–60
summary: Reconcile heat release with exhaust conditions, estimate frozen flame temperature, and close a reacting equilibrium model.
source: https://www.youtube.com/watch?v=32K6nWIdvwc
---

At fixed fuel input, a hot stack can deliver less recovered heat than a cooler stack. The comparison also depends on how much chemical energy remains in species such as carbon monoxide. The same enthalpy balance exposes both effects once the species amounts and phases are fixed.

## Separate chemical and sensible contributions

Using the rich ethanol products of Chapter 18, substitute the computed amounts into the steady-flow enthalpy sum. At inlet and outlet reference conditions, the result is the reaction enthalpy for those products. If the outlet is hotter, add each product's sensible rise to that reference result. If the product contains CO, the conversion of some carbon to CO rather than $\mathrm{CO_2}$ leaves about $282.98$ kJ per mole CO of potential further heat release at 298.15 K with oxygen available. This number is the magnitude of $\Delta_f\bar h^\circ_{\mathrm{CO_2}}-\Delta_f\bar h^\circ_{\mathrm{CO}}$ using $-393.51$ and $-110.53$ kJ/mol. It isolates the contribution of those carbon species. [Tutorial 10 Part 1 · Rich ethanol and hot products](https://www.youtube.com/watch?v=32K6nWIdvwc&t=20) · [NIST carbon monoxide](https://webbook.nist.gov/cgi/cbook.cgi?ID=C630080&Mask=1)

The lecture's values in kJ/mol, with liquid ethanol and vapor water, give $\Delta_r\bar h^\circ=3(-241.845)+(16/11)(-393.546)+(6/11)(-110.541)-(-235.310)=-1122.95$ kJ/mol ethanol, or 24.38 MJ/kg released. For the dry decane analysis in Chapter 18, liquid fuel formation enthalpy would give the wrong inlet reference because the lecture specifies gaseous decane. Using its $-249.659$ kJ/mol formation enthalpy, the 500 K sensible increments 6.947, 8.301, 5.943, 5.920 and 6.097 kJ/mol for water, carbon dioxide, CO, nitrogen and oxygen, and the measured products scaled by $1/1.148$, gives $q\simeq-5.50$ MJ/mol decane. [Tutorial 10 Part 1 · Ethanol at reference conditions and decane at 500 K](https://www.youtube.com/watch?v=32K6nWIdvwc&t=640)

For the fuel-gas blend in Chapter 18, use the balanced oxygen coefficient $1.055$ and the two carbon dioxide terms in the proper places. At the reference state there is 0.55 mol carbon dioxide in the products, and 0.02 mol carbon dioxide in the fuel blend. Their net formation-enthalpy contribution is $0.53\Delta_f\bar h^\circ_{\mathrm{CO_2}}$. Summing the net formation terms for carbon dioxide, water vapor, CO, methane and acetylene gives about $-468.2$ kJ/mol blend. The blend's own oxygen affects the required air but makes no direct formation-enthalpy contribution. [Tutorial 10 Part 1 · Fuel-gas blend](https://www.youtube.com/watch?v=32K6nWIdvwc&t=1460)

If the unknown hydrocarbon of Chapter 18 is specified to be a liquid alkane $\mathrm{C}_{n}\mathrm{H}_{2n+2}$, its hydrogen-to-carbon ratio is $2+2/n$. The measured $2(10.402)/9.6\approx2.167$ identifies $n\approx12$ in this exercise. Using $\Delta_f\bar h^\circ_{\rm fuel}=-351$ kJ/mol for liquid dodecane, the reference-state reaction with vapor water gives $12(-393.52)+13(-241.83)+351=-7515.03$ kJ/mol fuel. This is $-44.12$ MJ/kg fuel or $-8.50$ MJ/kg supplied oxygen using 27.63 mol oxygen supplied per mol fuel. Condensing 13 mol water at the reference state adds roughly $13(44.00)$ kJ/mol fuel to the heat recovered, giving a higher heating value of 47.48 MJ/kg fuel. [Tutorial 10 Part 1 · Alkane identification and heating value](https://www.youtube.com/watch?v=32K6nWIdvwc&t=1880)

## Use internal energy for rigid vessels

The lecture starts with 2 kmol graphite and 2 kmol oxygen at 298.15 K. Its 1000 K endpoint contains 1 kmol of $\mathrm{CO_2}$, 1 kmol of CO and 0.5 kmol of $\mathrm{O_2}$ by oxygen balance. For negligible work and changes in kinetic and potential energy, $Q=\Delta U=\Delta H-\bar R(n_{g,2}T_2-n_{g,1}T_1)$ using ideal gases and neglecting the condensed volume. The initial reactants have zero reference enthalpy. Using the lecture's formation and sensible terms, $H_2=(-393546+33425)+(-110541+21697)+0.5(22721)=-437605$ kJ after rounding. Then $Q=-437604.5-8.314(2.5\times1000-2\times298.15)=-453432$ kJ, so about 453.4 MJ leaves the vessel. The $pV$ correction depends on both gas amount and temperature. [Tutorial 10 Part 2 · Rigid-vessel heat transfer](https://www.youtube.com/watch?v=lJIyU7cwtQ8&t=20)

## Solve for oxidizer flow at a specified outlet temperature

In the lecture's adiabatic dodecane example, liquid fuel enters at 298 K and air at 700 K. Complete combustion with $a$ mol oxygen per mol fuel gives 12 mol carbon dioxide, 13 mol water vapor, $(a-18.5)$ mol excess oxygen and $3.76a$ mol nitrogen. For a 1700 K exit, the two sides of $H_r=H_p$ in kJ per mole fuel are

$$
\begin{aligned}
H_r&=-351+a[12.59+3.76(12.01)],\\
H_p&=12(-393.52+73.48)+13(-241.83+57.76)
+(a-18.5)(47.81)+3.76a(45.31).
\end{aligned}
$$

Equating the expressions gives $a=42.18$ and an air–fuel mass ratio of 34.01 kg/kg fuel. Each additional mole of oxygen supplied with its nitrogen carries $47.81+3.76(45.31)-[12.59+3.76(12.01)]=160.43$ kJ of net sensible enthalpy between the air inlet and product outlet. This slope makes the temperature constraint determine the oxidizer flow in the complete-combustion model. [Tutorial 10 Part 2 · Air requirement](https://www.youtube.com/watch?v=lJIyU7cwtQ8&t=640)

## Estimate a flame temperature without dissociation

For the lecture's methane example with separately supplied oxygen and argon, all reactants enter at 298 K and the target outlet is 1800 K. The enthalpy residual for stoichiometric methane and pure oxygen is $(-393.522+79.432)+2(-241.826+62.693)-(-74.873)=-597.483$ kJ/mol methane. To bring the residual to zero at 1800 K, use either $597.483/51.674=11.56$ mol excess oxygen, giving $\phi=2/(2+11.56)=0.1475$, or add argon to the stoichiometric pair. With $c_{p,\rm Ar}=0.52$ kJ/(kg K) and $M_{\rm Ar}=0.039948$ kg/mol, each mole of argon gains $0.52(0.039948)(1800-298)=31.20$ kJ, giving 19.15 mol argon per mol methane or 9.57 mol argon per mol oxygen. [Tutorial 10 Part 3 · Oxygen and argon dilution](https://www.youtube.com/watch?v=kXMpQ7zVwvw&t=20)

For a transparent approximation, take methane and dry air at 298.15 K, complete combustion at $\lambda\ge1$, all product water vapor, and positive mean molar heat capacities. For $\mathrm{CO_2}$, $\mathrm{H_2O}$, $\mathrm{N_2}$ and $\mathrm{O_2}$ take 0.054, 0.044, 0.034 and 0.035 kJ/(mol K). These are stipulated approximations for this exercise. Then

$$
T_{\rm out}=298.15+
\frac{802.3}{0.054+2(0.044)+7.52\lambda(0.034)+2(\lambda-1)(0.035)}.
$$

The temperatures are about 2316 K at $\lambda=1$ and 1730 K at $\lambda=1.5$. The model keeps product composition frozen at the assumed complete-combustion amounts and spreads the same chemical energy over more gas at the higher air rate. An accurate calculation uses species enthalpy functions and admits equilibrium dissociation where appropriate. A sealed adiabatic rigid vessel instead holds total internal energy constant. [Tutorial 10 Part 3 · Flame-temperature models](https://www.youtube.com/watch?v=kXMpQ7zVwvw&t=620)

The lecture also uses sensible-enthalpy tables to find the flame temperature for graphite and 150% theoretical air. One mole of graphite produces one mole of carbon dioxide with 0.5 mol residual oxygen and 5.64 mol nitrogen. The sum of their sensible enthalpies must equal the 393.546 kJ/mol formation-energy release. The tabulated sums are 381.425 and 409.624 kJ/mol at 1800 and 1900 K. Linear interpolation gives $1800+100(393.546-381.425)/(409.624-381.425)\approx1843$ K under frozen composition. [Tutorial 10 Part 3 · Graphite flame temperature](https://www.youtube.com/watch?v=kXMpQ7zVwvw&t=640)

For the sealed ethane example, $0.05$ kg of fuel and stoichiometric air occupy $0.7\,\mathrm{m^3}$ at 298 K. Each mole of $\mathrm{C_2H_6}$ with $3.5(\mathrm{O_2}+3.76\mathrm{N_2})$ gives $2\mathrm{CO_2}+3\mathrm{H_2O}+13.16\mathrm{N_2}$. The reacting gas inventories per mole fuel are 17.66 mol initially and 18.16 mol finally. Solve $H_p(T)-H_r(298)=\bar R[18.16T-17.66(298)]$ for the frozen adiabatic temperature, which is about 2891 K from the lecture's tabulated enthalpies. With $n_f=0.05/30.07$ kmol fuel, $p_1=n_f(17.66)\bar R(298)/0.7\simeq104$ kPa and $p_2=n_f(18.16)\bar R(2891)/0.7\simeq1.04$ MPa. Dissociation becomes important for realistic product temperatures in this range. [Tutorial 10 Part 3 · Ethane in a rigid vessel](https://www.youtube.com/watch?v=kXMpQ7zVwvw&t=1180)

## Solve dissociation with dimensionless activities

At fixed $T$ and $p$, start with one mole $\mathrm{O_2}$. Let $\alpha$ be the fraction dissociated in $\mathrm{O_2}\rightleftharpoons2\mathrm O$. The mixture has $1-\alpha$ moles $\mathrm{O_2}$ and $2\alpha$ moles $\mathrm O$, for total $1+\alpha$. At an interior equilibrium, the Gibbs energy is stationary with respect to the reaction extent $\xi$: $dG/d\xi=2\mu_{\mathrm O}-\mu_{\mathrm{O_2}}=0$. Each ideal-gas chemical potential is $\mu_i=\mu_i^\circ(T)+\bar RT\ln(y_i p/p^\circ)$, with reference pressure $p^\circ$. The standard Gibbs contribution is $\Delta_r\bar g^\circ=2\mu_{\mathrm O}^\circ-\mu_{\mathrm{O_2}}^\circ$. Solving the stationarity condition for the dimensionless activities gives

$$
K_p=\exp[-\Delta_r\bar g^\circ/(\bar RT)]
=\frac{(y_{\mathrm O}p/p^\circ)^2}{y_{\mathrm{O_2}}p/p^\circ}
=\frac{4\alpha^2}{1-\alpha^2}\frac{p}{p^\circ}.
$$

The lecture uses $T=3000$ K and $p=p^\circ=1$ atm, with $\Delta_r\bar g^\circ=109.108$ kJ/mol from the tabulated formation Gibbs energy of atomic oxygen. This gives $K_p\simeq0.0126$ and $\alpha=\sqrt{K_p/(4+K_p)}\simeq0.0560$. The residual molecular-oxygen mole fraction is about 0.894. A higher pressure at the same temperature lowers the dissociated fraction for this reaction, which increases total moles. To include dissociation in an adiabatic flame-temperature calculation, solve for equilibrium composition at every trial temperature and evaluate the enthalpy residual with that composition. [Tutorial 10 Part 4 · Oxygen dissociation](https://www.youtube.com/watch?v=TZAhb1KaZPs&t=1800)

## Supply the missing equation in a rich-product model

For a restricted rich decane model permitting $\mathrm{CO_2}$, $\mathrm{CO}$, $\mathrm{H_2O}$ and $\mathrm{H_2}$ plus inert nitrogen, three element balances constrain four reactive species amounts. The water–gas shift relation $\mathrm{CO+H_2O}\rightleftharpoons\mathrm{CO_2+H_2}$ provides a fourth equation if equilibrium at a specified temperature is assumed. Its ideal-gas equilibrium quotient is $y_{\mathrm{CO_2}}y_{\mathrm{H_2}}/(y_{\mathrm{CO}}y_{\mathrm{H_2O}})$ because $\Delta\nu=0$. Solve inside bounds that keep each species amount nonnegative. The calculated composition depends on the allowed species set, especially when radicals or additional species become appreciable. [Tutorial 10 Part 5 · Rich combustion equilibrium](https://www.youtube.com/watch?v=dW7RnzgzEi0&t=20)

The lecture sets $\phi=1.25$, $T=2200$ K and $p=1$ atm, so the oxygen input is $15.5/1.25=12.4$ mol per mol fuel. Let $b$ be moles CO. Carbon balance gives $10-b$ mol carbon dioxide. Oxygen balance then gives $24.8-b-2(10-b)=4.8+b$ mol water, and hydrogen balance gives $11-(4.8+b)=6.2-b$ mol hydrogen. In this direction the given Gibbs energies give $\Delta_r\bar g^\circ=-396.346-(-302.576-124.030)=30.260$ kJ/mol. Therefore

$$
\frac{(10-b)(6.2-b)}{b(4.8+b)}=\exp[-30.260/(0.008314\times2200)]\simeq0.19121.
$$

The left side decreases from infinity to zero for $0<b<6.2$. Solving gives about 4.64 mol CO, 5.36 mol carbon dioxide, 9.44 mol water and 1.56 mol hydrogen, with 46.624 mol nitrogen. The lecture's intermediate labeling and the substitution on the slide interchange the hydrogen and water factors. The equation above puts the species on their respective sides and reproduces the reported final composition. [Tutorial 10 Part 5 · Equilibrium quotient and back-substitution](https://www.youtube.com/watch?v=dW7RnzgzEi0&t=680)

## Numerical laboratory

Run the [Python laboratory](code/chapter_19.py). It evaluates the frozen-temperature estimates, the oxygen dissociation example and the rich-decane water–gas shift, checking the enthalpy, equilibrium and atom-balance residuals.

## Exercises and worked solutions

### Change the pressure at fixed temperature

Increase the oxygen dissociation pressure to $2p^\circ$ and hold $K_p=0.0126$. What happens to $\alpha$?

**Solution.** Set $\alpha=\sqrt{0.0126/(8+0.0126)}=0.0397$. Higher pressure favors the smaller mole-number side, decreasing the dissociation fraction from 5.60% to 3.97%.

### Know when the pressure factor cancels

Can you use the oxygen dissociation quotient and the water–gas shift quotient with every partial pressure measured in kPa and ignore $p^\circ$?

**Solution.** In the ideal water–gas shift quotient, the pressure units and powers of $p^\circ$ cancel between two gas moles on either side. In oxygen dissociation there is one extra pressure factor in the numerator, so use $p_i/p^\circ$ with the same units in both. The standard Gibbs energy defines the reference for that dimensionless equilibrium quotient.

### Compare equal-temperature rigid and flow endpoints

At 298.15 K consider one mole methane and enough oxygen for complete oxidation to $\mathrm{CO_2(g)+2H_2O(l)}$. Both the reactants and products are evaluated at that temperature. With ideal gases and negligible liquid volume, compute $Q_{\rm rigid}-Q_{\rm steady}$ for a rigid closed batch with no other work and a steady-flow device with no shaft work.

**Solution.** The gas inventory drops from 3 to 1 mol, so $\Delta n_g=-2$. The batch heat is $\Delta U=\Delta H-\Delta n_g\bar RT$. The flow heat is $\Delta H$, so $Q_{\rm rigid}-Q_{\rm steady}=2\bar RT\approx4.96$ kJ/mol fuel. The batch heat entering is less negative, or the released heat has lower magnitude, by that amount.

### Solve a fixed-temperature water–gas shift teaching model

Start with 1 mol CO and 1 mol water vapor. Allow only the water–gas shift reaction and take its dimensionless equilibrium constant in the stated direction to be 4 at the imposed temperature. Find the equilibrium extent.

**Solution.** At extent $\xi$, both reactants have $1-\xi$ mol and both products have $\xi$ mol. Total moles and pressure cancel from the quotient, so $4=\xi^2/(1-\xi)^2$. On $0<\xi<1$, this gives $\xi=2/3$ mol and keeps every species nonnegative.
