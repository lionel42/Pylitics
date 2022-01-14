"""This package contains all the possible views."""
from enum import Enum, auto


class ViewEnum(Enum):
    def _generate_next_value_(name: str, start, count, last_values):
        # Allows us to use capital naming in the enum but return cleaned name
        return name.lower().capitalize().replace("_", " ")


class Views(ViewEnum):
    LEFT = auto()
    RIGHT = auto()
    LIBERAL_ECONOMY = auto()
    FOREIGN_OPENNESS = auto()
    PATRIOTISM = auto()
    GOVERNMENT_POWER = auto()
    IMMIGRATION = auto()
    MILITARY = auto()
    SCIENCE = auto()
    TECHNOLOGY = auto()
    SOCIAL_STATE = auto()
    LIBERAL_SOCIETY = auto()
    FEMINISM = auto()
    MULTI_GENDER = auto()
    MULTICULTURALISM = auto()
    ENVIRONNEMENT_PROTECTION = auto()
    POLICE_SUPPORT = auto()
    URBAN = auto()
    CONSERVATISM = auto()
