#%%
import numpy as np
from pylitics import Spectrum, Views
from pylitics.collection import PointsCollection

spectrum = Spectrum([Views.LEFT, Views.CONSERVATISM])

print(spectrum)


collection = PointsCollection(spectrum)

collection._array = np.array(
    [
        [0.2, 1.0],
        [0.3, 0.4],
    ]
)

from pylitics.plot import compass, plt

fig, ax = compass(collection, min=0, max=1)
plt.show()
#%%
