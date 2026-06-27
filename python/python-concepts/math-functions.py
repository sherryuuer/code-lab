# List of Functions in Python Math Module
from math import *


# print(ceil(x))	# Returns the smallest integer greater than or equal to x.
x = 20
y = 3

result = copysign(x, y)
print(result)
# Returns x with the sign of y

# print(fabs(x))	
# Returns the absolute value of x
# print(factorial(x))
# Returns x!
# print(floor(x))
# Returns the largest integer less than or equal to x
print(fmod(x, y))
# Returns the remainder when x is divided by y
# frexp(x)	Returns the mantissa and exponent of x as the pair (m, e)

list1 = [3, 4, 5]
print(fsum(list1))
# fsum更注重浮点数的精确度，sum是python内置的
# Returns an accurate floating point sum of values in the iterable

# isfinite(x)	Returns True if x is neither an infinity nor a NaN (Not a Number)

# isinf(x)	Returns True if x is a positive or negative infinity
# isnan(x)	Returns True if x is a NaN
# ldexp(x, i)	Returns x * (2**i)
# modf(x)	Returns the fractional and integer parts of x

x = 34.5
print(trunc(x))	
# Returns the truncated integer value of x 返回阶段整数值

# exp(x)	Returns e**x
# expm1(x)	Returns e**x - 1
# log(x[, b])	Returns the logarithm of x to the base b (defaults to e)
# log1p(x)	Returns the natural logarithm of 1+x
# log2(x)	Returns the base-2 logarithm of x
# log10(x)	Returns the base-10 logarithm of x
# pow(x, y)	Returns x raised to the power y
# sqrt(x)	Returns the square root of x
# acos(x)	Returns the arc cosine of x
# asin(x)	Returns the arc sine of x
# atan(x)	Returns the arc tangent of x
# atan2(y, x)	Returns atan(y / x)
# cos(x)	Returns the cosine of x
# hypot(x, y)	Returns the Euclidean norm, sqrt(x*x + y*y)
# sin(x)	Returns the sine of x
# tan(x)	Returns the tangent of x
# degrees(x)	Converts angle x from radians to degrees
# radians(x)	Converts angle x from degrees to radians
# acosh(x)	Returns the inverse hyperbolic cosine of x
# asinh(x)	Returns the inverse hyperbolic sine of x
# atanh(x)	Returns the inverse hyperbolic tangent of x
# cosh(x)	Returns the hyperbolic cosine of x
# sinh(x)	Returns the hyperbolic cosine of x
# tanh(x)	Returns the hyperbolic tangent of x
# erf(x)	Returns the error function at x
# erfc(x)	Returns the complementary error function at x

x = 2
res = gamma(x)
print(res)
# Returns the Gamma function at x
# lgamma(x)	Returns the natural logarithm of the absolute value of the Gamma function at x
# print(pi)	Mathematical constant, the ratio of circumference of a circle to it's diameter (3.14159...)
# print(e)	mathematical constant e (2.71828...)
