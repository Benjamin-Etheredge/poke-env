# -*- coding: utf-8 -*-
from enum import Enum, unique, auto


@unique
class Field(Enum):
    """Represent a non null field in a battle."""

    ELECTRIC_TERRAIN = auto()
    GRASSY_TERRAIN = auto()
    MISTY_TERRAIN = auto()
    PSYCHIC_TERRAIN = auto()
    TRICK_ROOM = auto()

    def __str__(self) -> str:
        return f"{self.name} (field) object"

    @staticmethod
    def from_showdown_message(message: str) -> "Field":
        """Returns the Field object corresponding to the message.

        :param message: The message to convert.
        :type message: str
        :return: The corresponding Field object.
        :rtype: Field
        """
        message = message.replace("move: ", "")
        message = message.replace(" ", "_")
        return Field[message.upper()]
