import math

n = math.factorial(5)  # 5 * 4 * 3 * 2 * 1 = 120
print(n)

# factorial 함수만 import
from math import factorial

n = factorial(5) / factorial(3)
print(n)

# 여러 함수를 import
from math import factorial, acos

n = factorial(3) + acos(1)
print(n)
# acos(X)는 X의 요소에 대한 cos-1(역코사인)을 반환합니다(단위: 라디안). 이 함수는 실수와 복소수 입력값을 모두 받습니다. -1.0 ~ 1.0
# print(acos(-1.0))
# print(acos(0.9))
# print(acos(0.89))
# print(acos(0.7))
# print(acos(1))

# 모든 함수를 import
from math import *

n = sqrt(5) + fabs(-12.5)
print(n)

# factorial() 함수를 f()로 사용 가능
from math import factorial as f

n = f(5) / f(2)
print(n)

import sys

sys.path.append("C:\PySrc")
for i in sys.path:
    print(i)

from mylib import *
i = add(10, 20)
print(i)
i = substract(20, 5)
print(i)

import mylib
i = mylib.add(10, 20)
print(i)
i = mylib.substract(20, 5)
print(i)
