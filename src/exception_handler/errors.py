from typing import Type


class UnhandledExceptionError(Exception):
    def __init__(self, ex: Exception, expected_ex: Type[Exception]) -> None:
        msg =  f"\n> Expected '{expected_ex.__name__}' and its subclasses to handle, but got '{ex.__class__.__name__}' instead."
        msg += f"\n> '{ex.__class__.__name__}' is not subclass of '{expected_ex.__name__}'."
        super().__init__(msg)
