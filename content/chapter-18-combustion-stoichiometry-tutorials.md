---
title: Combustion Stoichiometry Tutorials
lectures: 54–55
summary: Use explicit species assumptions to solve rich combustion, analyze exhaust composition, and infer an equivalence ratio from mass flows.
source: https://www.youtube.com/watch?v=ml1fhdGuMc0
---

Element conservation fixes how many carbon atoms leave a burner. It cannot by itself allocate them among carbon monoxide, carbon dioxide, soot, and unburned hydrocarbons. A combustion worksheet has to show which species the model permits before a calculation can infer product composition.

## Close a rich ethanol example

Consider one mole of ethanol, $\mathrm{C}_{2}\mathrm{H}_{5}\mathrm{OH}$, at [fuel–air equivalence ratio](chapter-17-combustion-thermodynamics.html#count-elements-on-a-fixed-fuel-basis) $\phi=1.10$. Complete oxidation would require 3 moles $\mathrm{O_2}$. The supplied oxygen is $a=3/1.10=2.72727$ mol. The restricted product model assumes all hydrogen becomes water, all nitrogen remains $\mathrm{N_2}$, and carbon occurs only as $\mathrm{CO_2}$ and $\mathrm{CO}$. There is no residual oxygen in this model. Let $b$ and $c$ be moles of $\mathrm{CO_2}$ and $\mathrm{CO}$. Hydrogen balance fixes water at 3 mol. Then

$$
b+c=2,\qquad 2b+c+3=1+2a.
$$

The final $1$ accounts for the oxygen atom in the ethanol. The solution is $b=2a-4=1.45455$ mol, $c=0.54545$ mol, and $3.76a=10.25455$ mol nitrogen. A dry analyzer would see $c/(b+c+3.76a)=4.45\%$ CO in this restricted model. Larger richness eventually makes $b$ negative, showing the model must expand its product species. If the product set also allows $\mathrm{H_2}$, the three element balances and inert nitrogen do not determine all the unknowns. A measured species fraction or an equilibrium relation can supply the missing condition. [Tutorial 9 Part 1 · Rich product model](https://www.youtube.com/watch?v=ml1fhdGuMc0&t=20)

## Infer excess air from dry exhaust

The lecture's decane exhaust contains 10.56% $\mathrm{CO_2}$, 0.92% $\mathrm{CO}$, 4.91% $\mathrm{O_2}$ and 83.61% $\mathrm{N_2}$ by mole on a dry basis. On a 100 mol dry-product basis, the carbon balance gives $(10.56+0.92)/10=1.148$ mol fuel and the hydrogen balance gives $11(1.148)=12.628$ mol water if all hydrogen goes to water. With inert nitrogen and dry air represented by $\mathrm{O_2}+3.76\mathrm{N_2}$, the nitrogen balance gives $83.61/3.76=22.2367$ mol oxygen supplied. The oxygen balance gives $[2(10.56)+0.92+2(4.91)+12.628]/2=22.244$ mol, within 0.008 mol of the nitrogen-based result. The two independent estimates need only agree within the precision of the dry analysis.

Complete combustion of 1.148 mol decane requires $15.5(1.148)=17.794$ mol oxygen, giving $\phi=17.794/22.2367=0.8002$ and $124.97\%$ theoretical air. The measured CO can coexist with excess oxygen because supplied oxygen does not ensure complete oxidation. Including water gives 112.628 mol wet products, so the wet $\mathrm{CO_2}$ fraction is $10.56/112.628=0.09376$. The mean wet molar mass is $\sum_i n_i M_i/112.628=28.57$ g/mol. [Tutorial 9 Part 1 · Dry-product analysis](https://www.youtube.com/watch?v=ml1fhdGuMc0&t=540)

For a separate teaching case, assume complete, lean combustion of one mole of $\mathrm{C}_{10}\mathrm{H}_{22}$ with dry air. The carbon dioxide and water coefficients are 10 and 11. Stoichiometric oxygen is $10+22/4=15.5$. With $a$ moles oxygen supplied, the excess oxygen is $a-15.5$. Use dry mole fractions of 0.12043 $\mathrm{CO_2}$ and 0.03733 $\mathrm{O_2}$ as rounded inputs. Their ratio eliminates the unknown dry-product total.

$$
a=15.5+10\frac{y_{\mathrm{O_2,dry}}}{y_{\mathrm{CO_2,dry}}}
\simeq18.60.
$$

The inferred excess air is 20%. The nitrogen coefficient is $3.76a$, about 69.94 mol. Add 11 mol water to the denominator before computing wet fractions. An oxygen measurement alone attributes all deviation to excess air only if the fuel and assumptions are fixed.

## Sum oxygen demands for a fuel mixture

For an ideal-gas mixture, volume fraction at common temperature and pressure equals mole fraction. The lecture's blend contains 0.10 mol CO, 0.45 mol $\mathrm{H_2}$, 0.35 mol $\mathrm{CH_4}$, 0.04 mol $\mathrm{C_2H_2}$, and 0.02 mol each of $\mathrm{O_2}$, $\mathrm{N_2}$ and $\mathrm{CO_2}$ per mole of blend. The first four species require respectively $1/2$, $1/2$, 2 and $5/2$ mol oxygen per mole. The oxygen already in the blend offsets the external requirement.

$$
a_{\rm st}=0.10(0.5)+0.45(0.5)+0.35(2)+0.04(2.5)-0.02=1.055.
$$

The blend has a molar mass of 12.445 g/mol, so the stoichiometric air–fuel mass ratio is $1.055(31.998+3.76(28.014))/12.445=11.64$ kg/kg. At 20% excess air, $a=1.266$. Each mole of blend makes $0.10+0.35+2(0.04)+0.02=0.55$ mol $\mathrm{CO_2}$ and $0.45+2(0.35)+0.04=1.19$ mol water, leaving $a-a_{\rm st}=0.211$ mol oxygen and $3.76a+0.02=4.78016$ mol nitrogen. Dividing by 6.73116 mol total yields wet mole fractions of 8.17%, 17.68%, 3.13% and 71.02%, respectively. [Tutorial 9 Part 1 · Fuel gas mixtures](https://www.youtube.com/watch?v=ml1fhdGuMc0&t=1180)

## Separate air delivery from fuel delivery

In a flowing premixer with vaporizing liquid fuel, bulk dry-air delivery can be estimated from $\dot m_{\rm air}=\rho_{\rm air}UA$ for a uniform profile. The evaporated fuel rate depends on the liquid and transport conditions. The resulting mixture has

$$
\phi=\frac{\dot m_f}{\dot m_{\rm air}}\left(\frac{A}{F}\right)_{\rm st}.
$$

The lecture uses a $0.010\,\mathrm{m^2}$ flow cross section, a $0.050\,\mathrm{m^2}$ methanol-saturated wick and air at 320 K and 101325 Pa. Using $R=288.2\,\mathrm{J/(kg\,K)}$ gives $\rho_{\rm air}=1.099\,\mathrm{kg/m^3}$. At $U=0.5$ and $2.5\,\mathrm{m/s}$, the respective air rates are 0.005493 and 0.02747 kg/s. Multiplying the given evaporation fluxes of 0.017 and $0.027\,\mathrm{kg/(m^2\,s)}$ by the wick area gives 0.000850 and 0.001350 kg/s of fuel. From the methanol formula $\mathrm{CH_3OH}$, one mole of fuel requires $1+4/4-1/2=1.5$ mol oxygen, yielding $(A/F)_{\rm st}=6.429$ kg/kg. The two equivalence ratios are therefore 0.995 and 0.316. The air flow increases fivefold while evaporation increases by a factor of $0.027/0.017\approx1.59$. [Tutorial 9 Part 2 · Premixed evaporating fuel](https://www.youtube.com/watch?v=ZLa9RnWKEsc&t=0)

## Recover an unknown hydrocarbon's atomic ratio

For a hydrocarbon that forms only $\mathrm{CO_2}$ and water with dry air, use a 100 mol dry-product basis with 9.6 mol $\mathrm{CO_2}$, 7.3 mol $\mathrm{O_2}$ and 83.1 mol $\mathrm{N_2}$. Nitrogen implies $83.1/3.76=22.101$ mol of incoming oxygen. Oxygen balance fixes water at $2(22.101-9.6-7.3)=10.402$ mol. Carbon and hydrogen in the original fuel therefore have the atomic ratio $9.6/[2(10.402)]\simeq0.4615$. Exhaust stoichiometry determines this ratio, while molecular size needs independent information. Theoretical oxygen is $9.6+10.402/2=14.801$ mol on the same basis, so the air supply is $100(22.101/14.801)=149.32\%$ of theoretical. [Tutorial 9 Part 2 · Unknown hydrocarbon fuel](https://www.youtube.com/watch?v=ZLa9RnWKEsc&t=640)

## Numerical laboratory

Run the [Python laboratory](code/chapter_18.py). It solves the restricted rich-ethanol products, verifies element conservation, and uses the two dry-decane exhaust examples to recover excess air and compare independent oxygen and nitrogen balances.

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
