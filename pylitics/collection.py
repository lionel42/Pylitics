from typing import List

import numpy as np

from pylitics.views import ViewEnum

from .spectrum import Point, Spectrum


class PointsCollection:
    """A class that groups points in a spectrum.

    This can be considered as a list of points but for efficiency of
    computation it stores the collection using numpy arrays.
    """

    spectrum: Spectrum

    _axis: List[ViewEnum]
    _array: np.ndarray
    labels: List[str]

    def __init__(self, spectrum: Spectrum) -> None:
        self.spectrum = spectrum
        self._array = np.empty((0, len(spectrum)))
        # Axis makes sure we preserve the order of the views
        self._axis = [v for v in spectrum.views]

    def read_points(self, *points: Point):
        """Read points and add them to the collection."""

        if len(points) == 1 and isinstance(points[0], np.ndarray):
            # Array was given, copy it
            self._array = points[0]
            return
        self._array = np.concatenate(
            (
                self._array,
                np.array(
                    [[point[view] for view in self._axis] for point in points]
                ),
            )
        )

    @property
    def average(self) -> Point:
        p = Point(self.spectrum)
