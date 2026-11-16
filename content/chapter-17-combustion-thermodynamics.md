---
title: Combustion Thermodynamics
lectures: 50–53
summary: Balance reacting mixtures, compare heating values on a common water reference, and formulate the combustor energy and entropy balances.
source: https://www.youtube.com/watch?v=zn4DDSNWeUA
---

A stack analyzer reports carbon dioxide and oxygen on a dry basis. A heat balance needs the water that this measurement excludes. A useful calculation therefore closes the element balances first, specifies the product phases, and only then assigns energies to the streams.

## Count elements on a fixed fuel basis

For complete oxidation of a gas containing carbon, hydrogen, and oxygen, one mole of $\mathrm{C}_{x}\mathrm{H}_{y}\mathrm{O}_{z}$ needs $\nu_{\mathrm{O_2,st}}=x+y/4-z/2$ moles of oxygen to form $x$ moles $\mathrm{CO_2}$ and $y/2$ moles $\mathrm{H_2O}$. This follows by matching the two sources of oxygen atoms to the product requirement $2x+y/2$. Approximate dry air by $\mathrm{O_2}+3.76\,\mathrm{N_2}$ per mole of oxygen supplied. This approximation groups the inert gases into nitrogen.

Let $\lambda$ be actual divided by stoichiometric dry-air supply, for fixed fuel. The fuel–air equivalence ratio is $\phi=1/\lambda$. Percent theoretical air is $100\lambda$, and percent excess air is $100(\lambda-1)$. With $\lambda<1$ the supplied oxygen cannot form only $\mathrm{CO_2}$ and water from the fuel. A rich calculation requires a product-species model or measured composition. In a lean complete-combustion model for methane using 20% excess air, the reaction is

$$
\mathrm{CH_4}+2.4(\mathrm{O_2}+3.76\,\mathrm{N_2})
\longrightarrow\mathrm{CO_2}+2\,\mathrm{H_2O}+0.4\,\mathrm{O_2}+9.024\,\mathrm{N_2}.
$$

The dry mole fraction of $\mathrm{O_2}$ is $0.4/10.424=3.84\%$. On a wet basis, it is $0.4/12.424=3.22\%$. At 101.325 kPa the product vapor partial pressure is $101.325(2/12.424)=16.31$ kPa. Compare it with saturation pressure to predict condensation during constant-pressure cooling, under the ideal gas and water phase-equilibrium assumptions. Inlet air humidity adds water to the product side and changes this dew point even at unchanged dry-air supply. [Lecture 50 · Stoichiometry and exhaust dew point](https://www.youtube.com/watch?v=zn4DDSNWeUA&t=980)

The same balances can recover air supply from measured dry exhaust. The lecture reports 9.00% $\mathrm{CO_2}$, 2.00% $\mathrm{CO}$, 2.11% $\mathrm{O_2}$, and 86.89% $\mathrm{N_2}$ from methane burned with dry air. On a basis of 100 mol dry products, carbon balance requires $9+2=11$ mol methane and hydrogen balance requires 22 mol water. Oxygen balance gives $(2\times9+2+2\times2.11+22)/2=23.11$ mol oxygen supplied. The nitrogen check gives $3.76(23.11)\approx86.89$ mol. Complete oxidation of that fuel would need 22 mol oxygen, so $\lambda=23.11/22=1.0505$, corresponding to 5.05% excess air and $\phi\approx0.952$. The measured carbon monoxide is consistent with incomplete oxidation despite overall excess air. At 100 kPa, $p_v=100(22/122)\approx18.03$ kPa, giving a dew point near 58 °C. [Lecture 50 · Inverting a dry analysis](https://www.youtube.com/watch?v=zn4DDSNWeUA&t=980)

## Retain enthalpy of formation when species change

Let $\bar h_i$ denote molar enthalpy of species $i$. Choose 298.15 K and standard pressure $p^\circ=1$ bar as reference, with standard formation enthalpies defined relative to elements in their standard states.

$$
\bar h_i(T)=\Delta_f\bar h_i^\circ+
\big[\bar h_i(T)-\bar h_i(298.15\,\mathrm K)\big].
$$

For an ideal gas of fixed composition the bracket is the integral of molar $\bar c_{p,i}(T)$. A phase change needs a consistent phase reference. The zero standard formation enthalpies of elemental $\mathrm{O_2(g)}$ and $\mathrm{N_2(g)}$ leave their sensible enthalpies in a hot-stream balance. Estimate an enthalpy change with bond energies by breaking reactant bonds and forming product bonds only where data and phase assumptions justify that estimate. Tabulated species formation enthalpies provide the needed reference values directly. [Lecture 51 · Formation and sensible enthalpy](https://www.youtube.com/watch?v=0TUCq-D4hRw&t=320)

## Specify water phase when reporting heat release

For a steady-flow reaction with no shaft work and negligible changes in speed and elevation, the heat entering per mole of fuel is total product enthalpy minus total reactant enthalpy on the same fuel basis. At 298.15 K use, in kJ/mol, $\Delta_f\bar h^\circ_{\mathrm{CH_4(g)}}=-74.87$, $\Delta_f\bar h^\circ_{\mathrm{CO_2(g)}}=-393.51$, $\Delta_f\bar h^\circ_{\mathrm{H_2O(g)}}=-241.826$, and $\Delta_f\bar h^\circ_{\mathrm{H_2O(l)}}=-285.830$. Complete methane oxidation gives a lower heating value of about 802.3 kJ/mol with vapor products and a higher heating value of about 890.3 kJ/mol with liquid water, both expressed as positive heat release. Their difference, 88.0 kJ/mol fuel, corresponds to condensing two moles of water at the reference state. The heating value differs from heat recoverable when exhaust leaves hot. [Lecture 52 · Methane heating value](https://www.youtube.com/watch?v=6GW8hiVuf2o&t=740) · [NIST methane](https://webbook.nist.gov/cgi/cbook.cgi?ID=C74828&Mask=1) · [NIST carbon dioxide](https://webbook.nist.gov/cgi/cbook.cgi?ID=C124389&Mask=1) · [NIST water](https://webbook.nist.gov/cgi/cbook.cgi?ID=C7732185&Mask=3)

## Couple flame temperature and entropy to product assumptions

For steady adiabatic combustion with no shaft work, solve

$$
\sum_{\rm out}n_i\bar h_i(T_{\rm out})=\sum_{\rm in}n_i\bar h_i(T_{\rm in}).
$$

If the product species and amounts are specified, the unknown is temperature. When equilibrium determines the hot-product composition, the temperature and composition satisfy the enthalpy and element constraints together. High-temperature dissociation often reduces temperature relative to a complete-oxidation estimate at the same initial state. Excess air carries product sensible enthalpy and generally lowers temperature on the lean side at fixed inlet conditions.

In the lecture's stoichiometric methane example, both reactants enter at 298.15 K. Under complete oxidation with all product water vapor, subtract the product formation enthalpies from both sides to get

$$
\Delta\bar h_{\mathrm{CO_2}}(T)+2\Delta\bar h_{\mathrm{H_2O}}(T)
+7.52\Delta\bar h_{\mathrm{N_2}}(T)=802.3\ \mathrm{kJ/mol_{fuel}},
$$

where $\Delta\bar h_i(T)$ is each species' molar sensible enthalpy rise from 298.15 K. With positive heat capacities and frozen product amounts, the left side increases with temperature. The lecture brackets the solution with property-table entries at 2300 and 2400 K and interpolates to about 2330 K. The same equation with temperature-dependent equilibrium species replaces this complete-combustion estimate when dissociation matters. [Lecture 53 · Adiabatic flame temperature](https://www.youtube.com/watch?v=F14AY9ge4F0&t=400) · [Cantera equilibrium example](https://www.cantera.org/3.2/userguide/flame-temperature.html)

For the steady entropy balance, the third-law reference supplies absolute species entropies. For an ideal-gas species $i$, the molar identity $T\,d\bar s_i=d\bar h_i-\bar v_i\,dp_i$, with $\bar v_i=\bar RT/p_i$, integrates to

$$
\bar s_i(T,p_i)=\bar s_i^\circ(T_{\rm ref})
+\int_{T_{\rm ref}}^T\frac{\bar c_{p,i}(\theta)}{\theta}\,d\theta
-\bar R\ln\frac{p_i}{p^\circ}.
$$

Here $\bar R$ is the universal molar gas constant and $p_i$ is the species' actual partial pressure in its own stream. A pure ideal-gas inlet uses its full stream pressure. With each $n_i$ expressed per mole fuel, steady entropy generation is $\sum_{\rm out}n_i\bar s_i-\sum_{\rm in}n_i\bar s_i-\sum_j q_j/T_j$, where $q_j$ is heat entering per mole fuel across a boundary at temperature $T_j$. Adiabatic operation sets the heat term to zero. Chemical reaction and mixing can still generate entropy and destroy exergy in the amount $T_0s_{\rm gen}$ per mole fuel, where $T_0$ is the environment temperature. [Lecture 53 · Absolute entropy and entropy generation](https://www.youtube.com/watch?v=F14AY9ge4F0&t=780)

## Numerical laboratory

The [Python laboratory](code/chapter_17.py) checks methane product atom balances, dry and wet fractions, and the difference between heating values.

## Exercises and worked solutions

### Read excess oxygen consistently

For the stated methane model, how much oxygen remains when the excess-air percentage doubles from 20% to 40%?

**Solution.** At 40% excess air, oxygen fed is $2(1.4)=2.8$ mol/mol fuel. The remaining oxygen is 0.8 mol, double the 20% excess result. Its measured mole fraction rises by less than a factor of two because the total product inventory also increases.

### Identify the latent energy

How do heating values change between vapor and liquid water products if one mole of fuel forms three moles of water at the reference temperature?

**Solution.** The higher value exceeds the lower value by $3(285.830-241.826)\simeq132.0$ kJ/mol fuel. This relation uses the same reactant state, complete oxidation and reference temperature in both heating-value definitions.

### Include water vapor in the incoming air

One mole of water vapor enters with the reactants in the stated methane model. Assume it passes through and all water remains vapor. What does the ideal-gas oxygen analyzer read on wet and dry bases?

**Solution.** The oxygen amount remains 0.4 mol and the dry product total remains 10.424 mol. The wet total rises to $12.424+1=13.424$. The dry reading stays 3.84%, while the wet reading falls to $0.4/13.424=2.98\%$. The same dry oxygen measurement can therefore coexist with different exhaust dew points.

### Derive the mixing entropy correction

At fixed temperature and total pressure equal to $p^\circ$, form an ideal 50:50 molar mixture from two pure ideal-gas streams at the same temperature and pressure. Find the entropy change per mole of mixture.

**Solution.** In the mixture $p_i/p^\circ=1/2$ for either species, so each species gains $-\bar R\ln(1/2)$. Weighting by the two mole fractions gives $\bar R\ln2\approx5.76$ J/(mol K) of mixture. A reversible means of mixing could exchange work or entropy with surroundings. A simple insulated free mixer generates this entropy under the stated endpoint conditions.
