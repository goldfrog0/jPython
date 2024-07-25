#!/usr/bin/env python3
from math import isclose

#This does not work due to imprecision in float type
print(.1 + .2 == .3)

a: float = 0.999
b: float = 1.000

print(f'{a} == {b}?', isclose(a, b, abs_tol=.01))
