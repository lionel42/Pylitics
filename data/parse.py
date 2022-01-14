#%%%
import importlib
from pathlib import Path

import numpy as np
import pandas as pd

name = "Country_Year_V-Dem_Core_CSV_v11.1\V-Dem-CY-Core-v11.1.csv"
file = Path(name)
if not file.exists():
    file = Path("data", name)
df_all = pd.read_csv(file)
# %%
# Filter only one year
df = df_all[df_all.year == 2020][::2]
# %%

from pylitics import PointsCollection, Spectrum

c = PointsCollection(
    Spectrum(
        [
            "Egalitarian democracy",
            "Division of power",
        ]
    )
)
c.labels = df["country_text_id"]
c.read_points(
    np.array([df["v2x_egaldem"].to_numpy(), df["v2x_feduni"].to_numpy()]).T
)
# %%

import pylitics.plot
from pylitics.plot import compass, plt

fig, ax = compass(
    c,
    min=0,
    max=1,
)
plt.show()

# %%
