v = 2 + 3j
print(v.real)  # 2
print(v.imag)  # 3
print(5 % 2)   # 1
print(5 // 2)  # 2
a = 8     # 0000 1000
b = 11    # 0000 1011
c = a & b # 0000 1000  (8)
d = a ^ b # 0000 0011  (3)
print(c)
print(d)
a = a * 10
a *= 10
a = [1,2,3,4]
b = 5 in a    # False
print(b)
a = "ABC"
b = a
print(a is b)  # True

s = '아리랑\n아리랑\n아라리요'
print(s)
p = "이름: %s 나이: %d" % ("김유신", 65)
print(p)
print("이름: %s 나이: %d" % ("김유신", 65))
# 출력: 이름: 김유신 나이: 65
 
p = "X = %0.3f, Y = %10.2f" % (3.141592, 3.141592)
print(p)
# 출력: X = 3.142, Y =       3.14
path = 'C:\Temp\test.csv'
print(path)
path = r'C:\Temp\test.csv'
print(path)
departure, _, arrival = "Seattle-Seoul".partition('-')
print(departure)
# 출력 : Seattle
print(_)
print(arrival)

s = "Hello"
b = s.encode()
print(b)    # b'Hello'
s2 = b.decode()  
print(s2)   # 'Hello'
 
# 특정 인코딩 방식을 지정한 경우
x = "안녕".encode("UTF-8")
print(x)
y= x.decode("UTF-8")
print(y)