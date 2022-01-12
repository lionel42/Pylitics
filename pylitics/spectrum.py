"""Representing the political spectrum."""


from dataclasses import dataclass
from typing import TYPE_CHECKING, List

from .views import ViewEnum

if TYPE_CHECKING:
    import numpy as np


@dataclass
class Spectrum:
    """Model of a political spectrum."""

    views: List[ViewEnum]


class Point:
    """A point in the political spectrum.

    Can represent literally anything (a person, political party, country.)
    The values mean where the point is located in the spectrum.
    The weights mean how each spectrum dimension is important compared to
        other spectrum parts.
    The std is the standard deviation from the value for each dimenstion of
        the spectrum.
    """

    spectrum: Spectrum
    values: List[float] | np.ndarray
    weights: List[float] | np.ndarray
    std: List[float] | np.ndarray

    def __init__(
        self,
        values: List[float] | np.ndarray,
        weights: List[float] | np.ndarray = None,
        std: List[float] | np.ndarray = None,
        spectrum: Spectrum = None,
    ) -> None:
        self.values = values
        if spectrum is not None:
            if len(self.values) != len(spectrum):
                raise ValueError(
                    f"Values should have the same lenght as spectrum. \n"
                    f"Got {len(spectrum) = } and {len(self.values) =} "
                )
            self.spectrum = spectrum
        self.values = values
        if weights is not None:
            # Give average weights is not given
            self.weights = [0.5 for _ in self.values]
        else:
            if len(weights) != len(self.values):
                raise ValueError(
                    f"Values should have the same lenght as spectrum. \n"
                    f"Got {len(weights) = } and {len(self.values) =} "
                )
            self.weights = weights

        if std is not None:
            self.std = std

    def __getattribute__(self, __name: ViewEnum) -> float:
        if isinstance(__name, ViewEnum):
            return self.values[self.spectrum.views.index(__name)]
        else:
            raise TypeError(
                f"Indexing {type(self).__name__} should be done"
                f" using {type(ViewEnum).__name__}"
            )
