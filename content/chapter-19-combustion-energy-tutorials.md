---
title: Combustion Energy Tutorials
lectures: 56–60
summary: Reconcile heat release with exhaust conditions, estimate frozen flame temperature, and close a reacting equilibrium model.
source: https://www.youtube.com/watch?v=32K6nWIdvwc
---

At fixed fuel input, a hot stack can deliver less recovered heat than a cooler stack. The comparison also depends on how much chemical energy remains in species such as carbon monoxide. The same enthalpy balance exposes both effects once the species amounts and phases are fixed.

## Separate chemical and sensible contributions

Using the rich ethanol products of Chapter 18, substitute the computed amounts into the steady-flow enthalpy sum. At inlet and outlet reference conditions, the result is the reaction enthalpy for those products. If the outlet is hotter, add each product's sensible rise to that reference result. If the product contains CO, the conversion of some carbon to CO rather than $\mathrm{CO_2}$ leaves about $282.98$ kJ per mole CO of potential further heat release at 298.15 K with oxygen available. This number is the magnitude of $\Delta_f\bar h^\circ_{\mathrm{CO_2}}-\Delta_f\bar h^\circ_{\mathrm{CO}}$ using $-393.51$ and $-110.53$ kJ/mol. It isolates the contribution of those carbon species. [Tutorial 10 Part 1 · Rich ethanol and hot products](https://www.youtube.com/watch?v=32K6nWIdvwc&t=20) · [NIST carbon monoxide](https://webbook.nist.gov/cgi/cbook.cgi?ID=C630080&Mask=1)

For a rigid closed vessel, use $Q=U_2-U_1$ if all work is zero and external energy changes are negligible. As a reference-temperature example, react 2 kmol graphite with 2 kmol $\mathrm{O_2}$ to form 2 kmol $\mathrm{CO_2}$. Assuming ideal gases and negligible $pV$ of graphite, $U=H-n_g\bar RT$ for conversion between total energy and enthalpy at each endpoint. The gas mole number and temperature match at the endpoints, so $Q\simeq-787.02$ MJ. For other reactions or endpoint temperatures, retain the $n_g\bar RT$ correction. For adiabatic steady-flow dilution, instead use the enthalpies of the fuel and oxidizer at their own inlet temperatures and constrain the product temperature to solve for the needed air rate. [Tutorial 10 Part 2 · Rigid vessel and air requirement](https://www.youtube.com/watch?v=lJIyU7cwtQ8&t=20)

## Estimate a flame temperature without dissociation

For a transparent approximation, take methane and dry air at 298.15 K, complete combustion at $\lambda\ge1$, all product water vapor, and positive mean molar heat capacities. For $\mathrm{CO_2}$, $\mathrm{H_2O}$, $\mathrm{N_2}$ and $\mathrm{O_2}$ take 0.054, 0.044, 0.034 and 0.035 kJ/(mol K). These are stipulated approximations for this exercise. Then

$$
T_{\rm out}=298.15+
\frac{802.3}{0.054+2(0.044)+7.52\lambda(0.034)+2(\lambda-1)(0.035)}.
$$

The temperatures are about 2316 K at $\lambda=1$ and 1730 K at $\lambda=1.5$. The model keeps product composition frozen at the assumed complete-combustion amounts and spreads the same chemical energy over more gas at the higher air rate. An accurate calculation uses species enthalpy functions and admits equilibrium dissociation where appropriate. A sealed adiabatic rigid vessel instead holds total internal energy constant. [Tutorial 10 Part 3 · Flame-temperature models](https://www.youtube.com/watch?v=kXMpQ7zVwvw&t=620)

## Solve dissociation with dimensionless activities

At fixed $T$ and $p$, start with one mole $\mathrm{O_2}$. Let $\alpha$ be the fraction dissociated in $\mathrm{O_2}\rightleftharpoons2\mathrm O$. The mixture has $1-\alpha$ moles $\mathrm{O_2}$ and $2\alpha$ moles $\mathrm O$, for total $1+\alpha$. For ideal gases let each activity be $y_i p/p^\circ$ with reference pressure $p^\circ$. Use $\Delta_r\bar g^\circ$ for the standard molar Gibbs energy change of the reaction at $T$, evaluated for the stated stoichiometry. The dimensionless equilibrium constant $K_p$ then satisfies

$$
K_p=\exp[-\Delta_r\bar g^\circ/(\bar RT)]
=\frac{(y_{\mathrm O}p/p^\circ)^2}{y_{\mathrm{O_2}}p/p^\circ}
=\frac{4\alpha^2}{1-\alpha^2}\frac{p}{p^\circ}.
$$

With illustrative $K_p=0.0126$ and $p=p^\circ$, $\alpha=\sqrt{K_p/(4+K_p)}\simeq0.0560$. The residual molecular-oxygen mole fraction is about 0.894. A higher pressure at the same temperature lowers the dissociated fraction for this reaction, which increases total moles. Factors of $p/p^\circ$ maintain a dimensionless $K_p$ and encode the pressure effect. [Tutorial 10 Part 4 · Oxygen dissociation](https://www.youtube.com/watch?v=TZAhb1KaZPs&t=1800)

## Supply the missing equation in a rich-product model

For a restricted rich decane model permitting $\mathrm{CO_2}$, $\mathrm{CO}$, $\mathrm{H_2O}$ and $\mathrm{H_2}$ plus inert nitrogen, three element balances constrain four reactive species amounts. The water–gas shift relation $\mathrm{CO+H_2O}\rightleftharpoons\mathrm{CO_2+H_2}$ provides a fourth equation if equilibrium at a specified temperature is assumed. Its ideal-gas equilibrium quotient is $y_{\mathrm{CO_2}}y_{\mathrm{H_2}}/(y_{\mathrm{CO}}y_{\mathrm{H_2O}})$ because $\Delta\nu=0$. Solve inside bounds that keep each species amount nonnegative. The calculated composition depends on the allowed species set, especially when radicals or additional species become appreciable. [Tutorial 10 Part 5 · Rich combustion equilibrium](https://www.youtube.com/watch?v=dW7RnzgzEi0&t=20)

## Numerical laboratory

Run the [Python laboratory](code/chapter_19.py). It evaluates the frozen-temperature estimates and solves the oxygen dissociation example, checking the enthalpy and equilibrium residuals.

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
