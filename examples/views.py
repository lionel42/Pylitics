"""Show how to use the pylitics.Views Enum."""

import pylitics


# Access a view
print(pylitics.Views.MULTICULTURALISM)
# Access the value of the view, a string that has been "beautyfied"
print(pylitics.Views.MULTICULTURALISM.value)

# Iterate over the views
for v in pylitics.Views.__members__.items():
    print(v)
# Iterate over the views v 2
for v in pylitics.Views:
    print(v)


# Creating a new kind of enum
from enum import auto
class CustomViews(pylitics.views.ViewEnum):
    MONKEY_LIKELYNESS = auto()
    WALL_BUILDING = auto()

print(CustomViews)