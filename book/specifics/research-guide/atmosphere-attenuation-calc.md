---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.16.6
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---
# Atmospheric attenuation

In the previous section, we stated our desired frequency range without proof. In this section, we will prove it. To do so, we calculate the atmospheric attenuation (that is, the effect of the atmosphere on space-to-ground power transmission) specific cases as well as the general case. We will be using these values to determine a suitable microwave range for the Elara space swarms.

```{code-cell} ipython3
import itur
import astropy.units as u
from astropy.table import Table
import numpy as np
import matplotlib.pyplot as plt
```

```{code-cell} ipython3
# Vector graphics
%config InlineBackend.figure_format = 'svg'
# Serif text
plt.rcParams["font.family"] = "serif"
plt.rcParams['mathtext.fontset'] = 'stix'
```

We use the [Recommendation ITU-R P.618 model](https://www.itu.int/rec/R-REC-P.618/en) created by the International Telecommunications Union, as implemented by the [ITU-Rpy](https://itu-rpy.readthedocs.io/en/latest/index.html) library, to perform our calculations. To give a sense of the model, the following is a graph of atmospheric attenuation for an older version of the model (P.676):

![](img/attenuation.svg)

## Gaseous attenuation

The first case of attenuation is the attenuation due to atmospheric gases in the atmosphere. We will do the calculations here, using the Recommendation ITU-R P.618 model (which we will henceforth refer to as *"the ITU-R reference model"* or as simply _"the ITU-R model"_), as we discussed.

```{code-cell} ipython3
# reference conditions
rho = 7.5 * u.g / u.m**3 # water vapour density
P = 1013 * u.hPa # atmospheric pressure
T = 25 * u.deg_C # temperature 
```

The ITU-R model can be chosen to yield an approximate or exact solution, depending on the level of accuracy required. We will use the approximate mode for now, though once the precision is necessary, we will need to use the exact mode.

```{code-cell} ipython3
MODE = "approx"
```

In general, the attenuation is a function of both atmospheric conditions (water vapour, density, rain, dust, and cloud conditions) as well as the angle of elevation of the power satellites relative to a receiver station, which will change continuously as the power satellites orbit. We can see the effect of elevation angle on attenuation quite distinctly. For instance, with otherwise identical parameters, an elevation angle of 90 degrees (i.e. satellite directly above the receiver station) has _drastically_ lower attenuation as compared to an elevation angle of 5 degrees (i.e. satellite at the edge of the horizon relative to the receiver station:

```{code-cell} ipython3
Att5 = itur.gaseous_attenuation_slant_path(1, 5, rho, P, T) # for elevation angle of 5 deg
Att5
```

```{code-cell} ipython3
Att90 = itur.gaseous_attenuation_slant_path(1, 90, rho, P, T) # for elevation angle of 5 deg
Att90
```

```{code-cell} ipython3
print("For 90 deg: " + str(round((1- 10**(-(Att90/u.dB).value/10)) * 100, 2)) + "%")
```

```{code-cell} ipython3
print("For 5 deg: " + str(round((1- 10**(-(Att5/u.dB).value/10)) * 100, 2)) + "%")
```

We will enter in the conditions that result in maximum attenuation (power loss due to the atmosphere) as our **baseline value** (i.e. with the minimum elevation angle supported by the ITU-R model, which is 5 degrees). This means that this is an estimate of the worst-case power losses, which is important to design for to ensure that the system is robust.

```{code-cell} ipython3
el = 5 * u.deg # lowest elevation angle (nearly completely horizontal = longest distance = max attenuation)
f = np.linspace(1, 100, 1000) * u.GHz
```

```{code-cell} ipython3
Att = itur.gaseous_attenuation_slant_path(f, el, rho, P, T, mode=MODE)
```

```{code-cell} ipython3
plt.semilogy(f, Att)
plt.xlabel('Frequency [GHz]')
plt.ylabel('Gaseous Attenuation [dB]')
plt.grid(which='both', linestyle=':')
```

Note that these attenuation values are in _decibels_, which are a logarithmic unit:

```{code-cell} ipython3
Att.unit
```

To extract the raw values we make it dimensionless by dividing by `u.dB` to cancel out the units, then apply the typical log formula $\ell = 10^{-\mathrm{dB}/10}$ where $\ell$ is the percent loss in linear (instead of logarithmic) units.

```{code-cell} ipython3
Att_dimensionless = Att/u.dB
```

```{code-cell} ipython3
loss_linear = 1 - 10**(-Att_dimensionless/10)
```

We now pick the frequencies whose attenuation values that corresponds to <10% loss (which is >90% transmittance):

```{code-cell} ipython3
percent = u.def_unit("%", u.dimensionless_unscaled) #define new percent unit
```

```{code-cell} ipython3
# pick out the frequencies corresponding to
# attenuations with less than 10% loss
f_range = f[loss_linear <= 0.1]
# and pick out the respective attenuations
loss_percents = loss_linear[loss_linear <= 0.1] * 100 * percent
```

```{code-cell} ipython3
c = 299792458 * u.m / u.s
```

```{code-cell} ipython3
c
```

```{code-cell} ipython3
wavelengths = (c/f_range).to("cm")
```

```{code-cell} ipython3
freq_table = Table([
    np.round(f_range, 2),
    np.round(wavelengths, 2),
    np.round(loss_percents, 3)], 
    names=["Frequency", "Wavelength", "Gaseous attenuation losses (worst-case)"], 
    descriptions=None, dtype=None, meta=None)
```

```{code-cell} ipython3
freq_table
```

Based on the gaseous attenuation, the suitable frequencies are between 1 and 6.75 GHz, corresponding approximately to 4.4 - 30 cm. We will now examine the other sources of attenuation. This includes the contribution due to rain, clouds, and scintillation (rapid changes of refractive index as electromagnetic waves pass through the atmosphere due to turbulence and other effects). While the specific modelling of each is rather complex, the full model is thankfully implemented in code so we can compute it readily.

For this, we will use the `atmospheric_attenuation_slant_path` method, which also takes into account the Earthbound receiver diameter and the latitude and longitude of the receiver. We will use two test locations for calculating the attenuation. The first is the Bering sea, located at 54.393203° N, 172.369927° W, representing (_in theory_) close to the worst-case attenuation due to its remoteness and high lattitude (which both increase atmospheric losses). The second is Hawaii, located at 19.8987° N, 155.6659° W, representing (_in theory_) close to the most favorable conditions and therefore the best-case attenuation. (See [this GPS coordinates viewer](https://www.gps-coordinates.net/) for an interactive way to view these coordinates). From this we can calculate a range of values. Note that _we are not planning to put a power receiver station at either location_. Their general location on the planet is simply a reference point for planning.

```{code-cell} ipython3
# Calculate other sources of attenuation (dust, rain, clouds) and also the total attenuation
# args: lat, lon, f, el, p, D
# D: earth-station antenna diameter (m)
# we will use 10m as a conservative estimate
# as attenuation is highest for small-diameter receivers
D = 10

# for lat/long. we will calculate using two values:
# 1) that of approx. the Bering sea (because further north there are basically no human settlements)
# 2) close to the equator (Hawaii)
# Note that we must set the longitude with a negative sign as
# itur expects a longitude value with respect to the east (not the west)
lat1, long1 = (54.393203, -172.369927)
lat2, long2 = (19.8987, -155.6659)

# Just like before we use 5 degree elevation anlge as it is the 
# lowest elevation = highest attenuation
# and we design for the highest-attenuation conditions as our baseline value

# This parameter controls the percentage of time the rain
# attenuation is exceeded - we want our system to work even
# in the most extreme storm conditions
R_percent = 0.5

# Bering sea location
Att_location1 = itur.atmospheric_attenuation_slant_path(lat1, long1, f, el, R_percent, D, mode=MODE)
# Hawaii location
Att_location2 = itur.atmospheric_attenuation_slant_path(lat2, long2, f, el, R_percent, D, mode=MODE)
```

```{code-cell} ipython3
plt.semilogy(f, Att_location1, label="Bering Sea location")
plt.semilogy(f, Att_location2, label="Hawaii location")
plt.xlabel('Frequency [GHz]')
plt.ylabel('Total Attenuation [dB]')
plt.grid(which='both', linestyle=':')
plt.legend()
plt.show()
```

> It does appear that the tropical ocean may contribute to the attenuation in a way that was not entirely expected, making it so that the Hawaii test location has a higher attenuation than the Bering Sea test location at most frequencies.

We will now do the same analysis as previously, just for both the test locations:

```{code-cell} ipython3
def attenuation_losses(att):
    # same formula as before in modified form
    loss_linear = 1 - 10**(-Att/(10 * u.dB))
    # pick out the frequencies corresponding to
    # attenuations with less than 10% loss
    f_range = f[loss_linear <= 0.1]
    # convert to wavelengths
    wavelengths = (c/f_range).to("cm")
    # and pick out the respective attenuations
    loss_percents = loss_linear[loss_linear <= 0.1] * 100 * percent
    return f_range, wavelengths, loss_percents
```

```{code-cell} ipython3
def generate_att_table(att):
    f_range, wavelengths, loss_percents = attenuation_losses(att)
    return Table([
        np.round(f_range, 2),
        np.round(wavelengths, 2),
        np.round(loss_percents, 3)], 
    names=["Frequency", "Wavelength", "Gaseous attenuation losses (worst-case)"], 
    descriptions=None, dtype=None, meta=None)
```

```{code-cell} ipython3
Att_table_1 = generate_att_table(Att_location1)
Att_table_2 = generate_att_table(Att_location2)
```

```{code-cell}
Att_table_1
```

```{code-cell}
Att_table_2
```