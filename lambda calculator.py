##################################################
# Title: Lambda Calculator
# Author: Jerry Hobby
# Description: A simple calculator that uses lambda functions to perform operations.
# It demonstrates lambda functions and how they can be used to perform calculations.
#
# The calculator can perform the following operations:
# - tan(x)
# - asin(x)
# - acos(x)
# - atan(x)
# - sinh(x)
# - cosh(x)
# - tanh(x)
# - asinh(x)
# - acosh(x)
# - atanh(x)
# - factorial(x)
# - cos(x)
# - sin(x)
# - add(x, y)
# It also includes a tests function to test the operations.
# The calculate function is used to calculate the result of an operation.
# The calculate_test function is used to calculate the result of an operation and print it.
##################################################

from math import tan as math_tan, asin as math_asin, acos as math_acos, atan as math_atan
from math import sinh as math_sinh, cosh as math_cosh, tanh as math_tanh
from math import asinh as math_asinh, acosh as math_acosh, atanh as math_atanh
from math import factorial as math_fact, cos as cos, sin as sin
from operator import add as add

tan = lambda x: math_tan(x)
asin = lambda x: math_asin(x)
acos = lambda x: math_acos(x)
atan = lambda x: math_atan(x)
sinh = lambda x: math_sinh(x)
cosh = lambda x: math_cosh(x)
tanh = lambda x: math_tanh(x)
asinh = lambda x: math_asinh(x)
acosh = lambda x: math_acosh(x)
atanh = lambda x: math_atanh(x)
fact = lambda x: math_fact(x)

# Dictionary to map lambda functions to their names
operation_names = {
    tan: "tan",
    asin: "asin",
    acos: "acos",
    atan: "atan",
    sinh: "sinh",
    cosh: "cosh",
    tanh: "tanh",
    asinh: "asinh",
    acosh: "acosh",
    atanh: "atanh",
    fact: "fact",
    add: "add",
    cos: "cos",
    sin: "sin"
}

def verbose(enabled=True):
    def decorator(func):
        def wrapper(operation, *args):
            if enabled:
                operation_name = operation_names.get(operation.__name__, operation.__name__)
                result = func(operation, *args)
                print(f"{operation_name}{args} = {result}")
                return result
            else:
                return func(operation, *args)
        return wrapper
    return decorator


@verbose(enabled=True)  # Change to False to disable verbosity
def calculate(operation, *args):
    return operation(*args)


# Function to test the lambda functions
# It calculates the result and prints it



def tests():
  print("Running tests...")

  # Example usage
  calculate(add, 1, 2)  # 3
  calculate(cos, 0)  # 1.0
  calculate(sin, 0)  # 0.0
  calculate(tan, 0.5)  # 0.5463024898437905
  calculate(asin, 0.5)  # 0.5235987755982989
  calculate(acos, 0.5)  # 1.0471975511965979
  calculate(atan, 0.5)  # 0.4636476090008061
  calculate(sinh, 0.5)  # 0.5210953054937474
  calculate(cosh, 0.5)  # 1.1276259652063807
  calculate(tanh, 0.5)  # 0.46211715726000974
  calculate(asinh, 0.5)  # 0.48121182505960347
  calculate(acosh, 1.5)  # 0.9624236501192069
  calculate(atanh, 0.5)  # 0.5493061443340548
  calculate(fact, 5)  # 120


def main():
  tests()


if __name__ == "__main__":
  main()

