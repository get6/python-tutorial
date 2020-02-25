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

numbers = range(2, 11, 2)
 
for x in numbers:
    print(x)
 
for x in range(1, 11, 2):
    print(x)

a = []
b = list()
if a == b:
    print(True)
else:
    print(False)

a = ["AB", 10, False]

mylist = "This is a book That is a pencil".split()
i = mylist.index('book')  # i = 3
n = mylist.count('is')    # n = 2
print(i, n)

# [표현식 for 요소 in 컬렉션 [if 조건식]]
list = [n ** 2 for n in range(10) if n % 3 == 0]
print(list)
# 출력: [0, 9, 36, 81]
list = [n for n in range(10)]
print(list)

sum = 0
for i in range(11): # 10까지
    sum += i
print(sum)

t = ("AB", 10, False) # Tuple은 immutable 타입
print(t)
# t[0] = "BA" # 'tuple' object does not support item assignment
print(t[0])
print(t[1])
print(t[2])
t1 = (123)
print(type(t1))  # int 타입
 
t2 = (123,)
print(type(t2))  # tuple 타입

firstname, lastname = ("John", "Kim")
print(lastname, ",", firstname)
# 출력: Kim, John

# 1. Tuple List로부터 dict 생성
persons = [('김기수', 30), ('홍대길', 35), ('강찬수', 25)]
mydict = dict(persons)
# mydict["홍대길"] = 130 # dict 클래스로 변하게되면 수정 가능
age = mydict["홍대길"]
print(age)   # 35
 
# 2. Key=Value 파라미터로부터 dict 생성
scores = dict(a=80, b=90, c=85)
print(scores['b'])  #90

scores = {"철수": 90, "민수": 85, "영희": 80}
v = scores.get("민수")  # 85
print(v)
v = scores.get("길동")  # None
print(v)
# v = scores["길동"]    # 에러 발생
 
# 멤버쉽연산자 in 사용
if "길동" in scores:
    print(scores["길동"])
 
scores.clear()  # 모두 삭제
print(scores)

persons = [('김기수', 30), ('홍대길', 35), ('강찬수', 25)]
mydict = dict(persons)
print(mydict)
mydict.update({'홍대길':33,'강찬수':26})
print(mydict)

# set 정의
myset = { 1, 1, 3, 5, 5 }
print(myset)    # 출력: {1, 3, 5}
 
# 리스트를 set으로 변환
mylist = ["A", "A", "B", "B", "B"]
s = set(mylist)
print(s)        # 출력: {'A', 'B'}

myset = {1, 3, 5}
 
# 하나만 추가
myset.add(7)
print(myset)
 
# 여러 개 추가
myset.update({4,2,10})
print(myset)
 
# 하나만 삭제
myset.remove(1)
print(myset)
 
# 모두 삭제
myset.clear()
print(myset)

a = {1, 3, 5}
b = {1, 2, 5}
 
# 교집합
i = a & b
# i = a.intersection(b)
print(i)
 
# 합집합
u = a | b
# u = a.union(b)
print(u)
 
# 차집합
d = a - b
# d = a.difference(b)
print(d)

# 함수전 까지