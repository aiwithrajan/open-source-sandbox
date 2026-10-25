import math

def gcd(a: int, b: int) -> int:
    """Calculate greatest common divisor of a and b."""
    return math.gcd(a, b)

def lcm(a: int, b: int) -> int:
    """Calculate least common multiple of a and b."""
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // math.gcd(a, b)
