# Python Exception Handler

### Code Example

```py
from exception_handler import exception_handler


@exception_handler(
    exception_class = ZeroDivisionError,
    on_exception = lambda ex: print("Oops... ZeroDivisionError :(")
)
def divide_two_numbers(a: int, b: int):
    print(f"Running: {a}/{b}")
    result = a / b
    print(f"Result: {result}")
    return result
```

### Usage

* Handle `ZeroDivisionError` with `on_exception` callback.

```py
r1 = divide_two_numbers(1, 0)
print("Returned value:", r1)

r2 = divide_two_numbers(1, 1)
print("Returned value:", r2)
```

This will output:

```bash
Running: 1/0
Oops... ZeroDivisionError :(
Returned value: None
Running: 1/1
Result: 1.0
Returned value: 1.0
```

* Try to handle unexpected exception

```py
divide_two_numbers(1, "1")
```

This will throw `exception_handler.errors.UnhandledExceptionError`,
because `1 / "1"` throws a `TypeError` which is not a subclass of `ZeroDivisionError`.
Also `UnhandledExceptionError` instance has `unhandled_exception` attribute which is `TypeError`
