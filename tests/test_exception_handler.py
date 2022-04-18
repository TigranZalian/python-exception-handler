from exception_handler import exception_handler, errors
import pytest


class MyException(Exception): ...

def on_exception_callback(ex: Exception):
    """ Returns exceptions's class """
    return ex.__class__

@exception_handler()
def function_that_not_raises(a: int, b: int):
    return a + b

@exception_handler()
def function_that_raises_subclass_exception():
    raise MyException()

@exception_handler(exception_class=MyException)
def function_that_raises_parent_exception():
    raise Exception()

@exception_handler(on_exception=on_exception_callback)
def function_that_raises_with_on_exception_cb():
    raise MyException()

@exception_handler(on_exception=on_exception_callback, exception_class=MyException)
def function_that_raises_exact_with_on_exception_cb():
    raise MyException()

@exception_handler(on_exception=on_exception_callback, exception_class=ZeroDivisionError)
def function_divide(a: int, b: int):
    return a / b

class TestExceptionHandler:
    def test_function_that_not_raises(self):
        assert function_that_not_raises(1, 2) == 3
        
    def test_function_that_raises_subclass_exception(self):
        assert function_that_raises_subclass_exception() == None
        
    def test_function_that_raises_parent_exception(self):
        pytest.raises(errors.UnhandledExceptionError, function_that_raises_parent_exception)
        
    def test_function_that_raises_with_on_exception_cb(self):
        assert function_that_raises_with_on_exception_cb() is MyException
        
    def test_function_that_raises_exact_with_on_exception_cb(self):
        assert function_that_raises_exact_with_on_exception_cb() is MyException
        
    def test_function_divide_that_not_raises(self):
        assert function_divide(4, 2) == 2.0
        
    def test_function_divide_that_raises(self):
        assert function_divide(1, 0) is ZeroDivisionError