import math
from math import pi

vec = [-5,-3,-1,1,3,5,7]
print(vec)
vec2 = [x*2 for x in vec]
print(vec2)
vec3 = [x for x in vec if x > 0]
print(vec3)
vec4 = [abs(x) for x in vec]
print(vec4)
vstr = ['proc ess  ', "finish ed", " with", "exit ", " code"]
vec5 = [strItem.rsplit() for strItem in vstr]
print(vec5)
vec6 = [strItem.strip() for strItem in vstr]
print(vec6)
vvec = [[1,2,3],[4,5,6],[7,8,9],[7,8,9]]
vec7 = [num for n in vvec for num in n]
print(vec7)
vec8 = [(x, x**2) for x in range(10)]
print(vec8)
vec9 = [str(round(pi, i)) for i in range(1,10)]
print(vec9)
vec10 = [[row[i] for row in vvec] for i in range(3)]
print(vec10)
vec11 = list(zip(*vvec))
print(vec11)
del vec9[0]
print(vec9)
del vec9[1:5]
print(vec9)
del vec9[:]
print(vec9)
del vec9
# 变量vec9已被删除，此时print会直接抛异常
print(vec9)
