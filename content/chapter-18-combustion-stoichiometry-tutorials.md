---
title: Combustion Stoichiometry Tutorials
lectures: 54–55
summary: Use explicit species assumptions to solve rich combustion, analyze exhaust composition, and infer an equivalence ratio from mass flows.
source: https://www.youtube.com/watch?v=ml1fhdGuMc0
---

Element conservation fixes how many carbon atoms leave a burner. It cannot by itself allocate them among carbon monoxide, carbon dioxide, soot, and unburned hydrocarbons. A combustion worksheet has to show which species the model permits before a calculation can infer product composition.

## Close a rich ethanol example

Consider one mole of ethanol, $\mathrm{C}_{2}\mathrm{H}_{5}\mathrm{OH}$, at equivalence ratio $\phi=1.10$. Complete oxidation would require 3 moles $\mathrm{O_2}$. The supplied oxygen is $a=3/1.10=2.72727$ mol. The restricted product model assumes all hydrogen becomes water, all nitrogen remains $\mathrm{N_2}$, and carbon occurs only as $\mathrm{CO_2}$ and $\mathrm{CO}$. There is no residual oxygen in this model. Let $b$ and $c$ be moles of $\mathrm{CO_2}$ and $\mathrm{CO}$. Hydrogen balance fixes water at 3 mol. Then

$$
b+c=2,\qquad 2b+c+3=1+2a.
$$

The final $1$ accounts for the oxygen atom in the ethanol. The solution is $b=2a-4=1.45455$ mol, $c=0.54545$ mol, and $3.76a=10.25455$ mol nitrogen. A dry analyzer would see $c/(b+c+3.76a)=4.45\%$ CO in this restricted model. Larger richness eventually makes $b$ negative, showing the model must expand its product species. If the product set also allows $\mathrm{H_2}$, the three element balances and inert nitrogen do not determine all the unknowns. A measured species fraction or an equilibrium relation can supply the missing condition. [Tutorial 9 Part 1 · Rich product model](https://www.youtube.com/watch?v=ml1fhdGuMc0&t=20)

## Infer excess air from dry exhaust

Assume complete, lean combustion of one mole of $\mathrm{C}_{10}\mathrm{H}_{22}$ with dry air. The carbon dioxide and water coefficients are 10 and 11. Stoichiometric oxygen is $10+22/4=15.5$. With $a$ moles oxygen supplied, the excess oxygen is $a-15.5$. Suppose the reported dry mole fractions are 0.12043 $\mathrm{CO_2}$ and 0.03733 $\mathrm{O_2}$, rounded teaching inputs. Their ratio eliminates the unknown dry-product total:

$$
a=15.5+10\frac{y_{\mathrm{O_2,dry}}}{y_{\mathrm{CO_2,dry}}}
\simeq18.60.
$$

The inferred excess air is 20%. The nitrogen coefficient is $3.76a$, about 69.94 mol. Add 11 mol water to the denominator before computing wet fractions. An oxygen measurement alone attributes all deviation to excess air only if the fuel and assumptions are fixed. If CO is measured, carbon balance scales the sum $\mathrm{CO_2}+\mathrm{CO}$ under a carbon-only-in-oxides model. Check the oxygen and nitrogen balances against that inferred scaling. [Tutorial 9 Part 1 · Dry-product analysis](https://www.youtube.com/watch?v=ml1fhdGuMc0&t=540)

## Sum oxygen demands for a fuel mixture

At ideal-gas conditions volume fraction equals mole fraction. On a one-mole mixture basis, each component contributes its stoichiometric oxygen demand times its mole fraction. For example, 0.10 mol CO, 0.04 mol hydrogen and 0.03 mol methane require $0.10(0.5)+0.04(0.5)+0.03(2)=0.13$ mol oxygen before counting the remaining components. An oxygen component in the fuel stream offsets the external oxygen requirement. Carbon dioxide and nitrogen in the fuel stream carry mass and sensible energy while contributing no oxygen demand in this complete-oxidation model. [Tutorial 9 Part 1 · Fuel gas mixtures](https://www.youtube.com/watch?v=ml1fhdGuMc0&t=1180)

## Separate air delivery from fuel delivery

In a flowing premixer with vaporizing liquid fuel, bulk dry-air delivery can be estimated from $\dot m_{\rm air}=\rho_{\rm air}UA$ for a uniform profile. The evaporated fuel rate depends on the liquid and transport conditions. The resulting mixture has

$$
\phi=\frac{\dot m_f}{\dot m_{\rm air}}\left(\frac{A}{F}\right)_{\rm st}.
$$

If air delivery rises fivefold and the evaporated fuel rate only doubles, $\phi$ falls to 40% of its starting value. This conclusion needs rate ratios, without assuming that evaporation scales linearly with speed. When converting a stoichiometric molar air amount to a mass ratio, multiply by the air-species molar masses and divide by fuel molar mass. [Tutorial 9 Part 2 · Premixed evaporating fuel](https://www.youtube.com/watch?v=ZLa9RnWKEsc&t=200)

## Numerical laboratory

Run the [Python laboratory](code/chapter_18.py). It solves the restricted rich-ethanol products, verifies element conservation, and recovers excess air from the rounded dry decane analysis.

## Exercises and worked solutions

### Find where the restricted model fails

Find where the rich-ethanol formula gives zero carbon dioxide.

**Solution.** Set $b=2a-4=0$ to find $a=2$, so $\phi=3/2$. Greater richness would demand negative $\mathrm{CO_2}$ with three moles water fixed. The modeled species or hydrogen allocation must change.

### Convert the molar ratio to a mass ratio

Calculate actual kg air per kg decane using 18.60 mol $\mathrm{O_2}$, accompanying nitrogen, $M_{\mathrm{O_2}}=31.998$, $M_{\mathrm{N_2}}=28.014$, and $M_{\rm fuel}=142.286$, on a consistent molar-mass scale.

**Solution.** The actual mass ratio is $18.60(31.998+3.76(28.014))/142.286=17.95$ kg air/kg decane. The factor 18.60 includes the excess oxygen and all its accompanying nitrogen.

### Include an oxygen-bearing fuel blend

Find the stoichiometric oxygen requirement for one mole of a gas containing 30% methane, 20% carbon monoxide, 10% oxygen, and 40% nitrogen by mole.

**Solution.** Methane and CO require $0.30(2)+0.20(0.5)=0.70$ mol oxygen. The blend supplies 0.10 mol. The external oxidizer must supply 0.60 mol oxygen per mol blend, accompanied by 2.256 mol nitrogen in the stated dry-air model. The original 0.40 mol nitrogen also appears in the product.

### Recover a dry basis from an analyzer reading

An exhaust stream contains 10 mol $\mathrm{CO_2}$ and 11 mol $\mathrm{H_2O}$, and its measured dry $\mathrm{CO_2}$ fraction is 0.12043. Find the wet $\mathrm{CO_2}$ fraction.

**Solution.** The dry total is $10/0.12043\approx83.04$ mol. The wet total is $83.04+11=94.04$ mol. The wet $\mathrm{CO_2}$ fraction is about $10/94.04=0.1063$.
