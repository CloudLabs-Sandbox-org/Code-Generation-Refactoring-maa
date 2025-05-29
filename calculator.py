# Create a basic calculator
def add(x, y):
    """Add two numbers."""
    return x + y    

def subtract(x, y):
    """Subtract two numbers."""
    return x - y

def multiply(x, y):
    """Multiply two numbers."""
    return x * y

def divide(x, y):
    """Divide two numbers."""
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

def modulus(x, y):
    """Modulus of two numbers."""
    return x % y

def power(x, y):
    """x raised to the power y."""
    return x ** y

def square(x):
    """Square of a number."""
    return x ** 2

def cube(x):
    """Cube of a number."""
    return x ** 3

def sqrt(x):
    """Square root of a number."""
    if x < 0:
        raise ValueError("Cannot take square root of negative number.")
    return x ** 0.5

def cbrt(x):
    """Cube root of a number."""
    return x ** (1/3)

def abs_val(x):
    """Absolute value of a number."""
    return abs(x)

def max_val(x, y):
    """Maximum of two numbers."""
    return max(x, y)

def min_val(x, y):
    """Minimum of two numbers."""
    return min(x, y)

def factorial(x):
    """Factorial of a number."""
    if x < 0:
        raise ValueError("Cannot take factorial of negative number.")
    if x == 0:
        return 1
    result = 1
    for i in range(1, int(x)+1):
        result *= i
    return result

def percentage(x, y):
    """x percent of y."""
    return (x / 100) * y

def average(x, y):
    """Average of two numbers."""
    return (x + y) / 2

def negate(x):
    """Negate a number."""
    return -x

def reciprocal(x):
    """Reciprocal of a number."""
    if x == 0:
        raise ValueError("Cannot take reciprocal of zero.")
    return 1 / x

def round_num(x, n=0):
    """Round a number to n decimal places."""
    return round(x, n)

def floor_num(x):
    """Floor of a number."""
    import math
    return math.floor(x)

def ceil_num(x):
    """Ceiling of a number."""
    import math
    return math.ceil(x)

def log_base10(x):
    """Log base 10 of a number."""
    import math
    if x <= 0:
        raise ValueError("Logarithm undefined for non-positive values.")
    return math.log10(x)

def log_basee(x):
    """Natural log (base e) of a number."""
    import math
    if x <= 0:
        raise ValueError("Logarithm undefined for non-positive values.")
    return math.log(x)

def sin_deg(x):
    """Sine of x degrees."""
    import math
    return math.sin(math.radians(x))

def cos_deg(x):
    """Cosine of x degrees."""
    import math
    return math.cos(math.radians(x))

def tan_deg(x):
    """Tangent of x degrees."""
    import math
    return math.tan(math.radians(x))

def sinh(x):
    """Hyperbolic sine of x."""
    import math
    return math.sinh(x)

def cosh(x):
    """Hyperbolic cosine of x."""
    import math
    return math.cosh(x)

def tanh(x):
    """Hyperbolic tangent of x."""
    import math
    return math.tanh(x)

def exp(x):
    """e raised to the power x."""
    import math
    return math.exp(x)