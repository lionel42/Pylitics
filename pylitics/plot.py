import matplotlib.pyplot as plt
import numpy as np

from .collection import PointsCollection


def compass(
    points_collection: PointsCollection,
    axes_position: float = 0.5,
    min=None,
    max=None,
    figsize=(5, 5),
    **kwargs,
):
    """Plot a 2D compass.

    :param axes_position: The value at which to set the middle.
    :param kwargs: Are sent to the ax.scatter function.
    """

    if len(points_collection.spectrum) != 2:
        raise ValueError(f"{compass.__name__} can only plot 2D spectrum.")

    figure, ax = plt.subplots(1, 1, figsize=figsize)
    ax.axis("off")
    ax.scatter(
        points_collection._array[:, 0],
        points_collection._array[:, 1],
        **kwargs,
    )
    if hasattr(points_collection, "labels"):
        for x, y, lab in zip(
            points_collection._array[:, 0],
            points_collection._array[:, 1],
            points_collection.labels,
        ):

            ax.text(x, y, lab)

    if min is None:
        min = np.nanmin(points_collection._array)

    if max is None:
        max = np.nanmax(points_collection._array)

    ## ax.set_xlim(min, max)
    ## ax.set_ylim(min, max)
    center = axes_position
    print(f"{min=}, {max=}")
    arrow_kwargs = {
        "length_includes_head": True,
        "head_width": 0.03,
        "color": "black",
    }
    ax.arrow(center, center, float(min) - center, 0, **arrow_kwargs)
    ax.arrow(center, center, 0, float(max) - center, **arrow_kwargs)
    ax.arrow(center, center, float(max) - center, 0, **arrow_kwargs)
    ax.arrow(center, center, 0, float(min) - center, **arrow_kwargs)

    # Labels
    ax.text(
        max,
        center,
        points_collection.spectrum[0].value,
        ha="left",
        va="center",
        rotation=-90,
    )
    ax.text(
        center,
        max,
        points_collection.spectrum[1].value,
        ha="center",
        va="bottom",
    )

    return figure, ax
