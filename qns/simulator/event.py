from typing import Optional
from .ts import Time


class Event(object):
    """
    Basic event class in simulator
    """

    def __init__(self, t: Optional[Time] = None, name: Optional[str] = None):
        """
        Args:
            t (Time): the time slot of this event
            name (str): the name of this event
        """
        self.t: Optional[Time] = t
        self.name: Optional[str] = name
        self._is_canceled: bool = False

    def invoke(self) -> None:
        """
        Invoke the event, should be implemented
        """
        raise NotImplemented

    def cancel(self) -> None:
        """
        Cancel this event
        """
        self._is_canceled = True

    @property
    def is_canceled(self) -> bool:
        """
        Returns:
            whether this event has been canceled
        """
        return self._is_canceled

    def __eq__(self, other: object) -> bool:
        return self.t == other.t

    def __lt__(self, other: object) -> bool:
        return self.t < other.t

    __le__ = lambda self, other: self < other or self == other
    __gt__ = lambda self, other: not (self < other or self == other)
    __ge__ = lambda self, other: not (self < other)
    __ne__ = lambda self, other: not self == other

    def __repr__(self) -> str:
        if self.name is not None:
            return f"Event({self.name})"
        return "Event()"