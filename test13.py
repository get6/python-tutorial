# List Comprehension
# [출력표현식 for 요소 in 입력Sequence [if 조건식]]
oldlist = [1, 2, "A", False, 3]
newlist = [i * i for i in oldlist if type(i) == int]
print(newlist)

# Set Comprehension
# {출력표현식 for 요소 in 입력Sequence [if 조건식]}
oldlist = [1, 1, 2, 3, 3, 4]
newlist = {i * i for i in oldlist}
print(newlist)  # 순서를 보장하지 않음

# Dictionary Comprehension
# {Key:Value for 요소 in 입력Sequence [if 조건식]}
id_name = {1: "박진수", 2: "강만진", 3: "홍수정"}
name_id = {val: key for key, val in id_name.items()}
print(name_id)


def isodd(val):
    return val % 2 == 1


mydict = {x: x * x for x in range(101) if isodd(x)}
# print(mydict)

for n in [1,2,3,4,5]:
    # print(n)
    pass

for c in "Hello World":
    # print(c)
    pass

# mylist = [1,2,3]
# Python 2
# it = iter(mylist)
# print(it)
# print(next(it))
# print(next(it))
# print(next(it))

# Python 3
# it = mylist.__iter__()
# print(it)
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())

class MyCollection:
    def __init__(self):
        self.size = 10
        self.data = list(range(self.size))

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= self.size:
            # 11 >= 10일 때 에러 발생
            raise StopIteration

        n = self.data[self.index]
        self.index += 1
        return n

coll = MyCollection()
for x in coll:
    # print(x)
    pass

# Generator 함수
def gen():
    yield 1
    yield 2
    yield 3

# Generator 객체
g = gen()
# print(type(g)) # <class 'generator'>

# next() 함수 사용
n = next(g); print(n) # 1
n = next(g); print(n) # 2
n = next(g); print(n) # 3

for x in gen():
    print(x)

g = (n*n for n in range(1001))

# g는 generator 객체
print(type(g)) # <class 'generator'>

# 리스트로 일괄 변환시
# mylist = list(g)
# print(mylist)

# 10개 출력
for i in range(10):
    value = next(g)
    # print(value)

# 나머지 모두 출력
for x in g:
    # print(x)
    pass

import threading

def sum(low, high):
    total = 0
    for i in range(low, high):
        total += i
    
    print('Subthread', total)

t = threading.Thread(target=sum, args=(1, 100000))
t.start()
t2 = threading.Thread(target=sum(1, 100000))
t2.start()
print('Main Thread')

# 예제(A)
import threading, requests, time