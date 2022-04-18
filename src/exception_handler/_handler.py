from functools import wraps
from .errors import UnhandledExceptionError
from typing import Callable, Union, TypeVar
from typing_extensions import ParamSpec


FuncRT = TypeVar("FuncRT")
Ex = TypeVar("Ex")
ExceptCbRT = TypeVar("ExceptCbRT")
FuncParams = ParamSpec("FuncParams")

def exception_handler(
    exception_class: Ex = Exception,
    on_exception: Callable[[Ex], ExceptCbRT] = lambda ex: None
):
    def decorator(func: Callable[FuncParams, FuncRT]) -> Callable[FuncParams, Union[FuncRT, ExceptCbRT]]:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Union[FuncRT, ExceptCbRT]:
            try:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if issubclass(e.__class__, exception_class):
                        raise
                    raise UnhandledExceptionError(e, exception_class)
            except exception_class as e:
                return on_exception(e)
        return wrapper
    return decorator
