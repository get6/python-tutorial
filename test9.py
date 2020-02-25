# 함수 Pass by Assignment

# 함수내에서 i, mylist 값 변경
def f(i, mylist):
    i = i + 1
    mylist.append(0)
 
k = 10       # k는 int (immutable)
m = [1,2,3]  # m은 리스트 (mutable)
 
f(k, m)      # 함수 호출
print(k, m)  # 호출자 값 체크
# 출력: 10 [1, 2, 3, 0]

# Default Parameter
def calc(i, j, factor = 2):
    return i * j * factor
 
result = calc(10, 20)
print(result)

# Named Parameter
def report(name, age, score):
    print(name, score)
 
report(age=10, name="Kim", score=80)

def total(*numbers):
    tot = 0
    for n in numbers:
        tot += n
    return tot
 
t = total(1,2)
print(t)
t = total(1,5,2,6)
print(t)

def calc(*numbers):
    count = 0
    tot = 0
    for n in numbers:
        count += 1
        tot += n
    return count, tot
 
count, sum = calc(1,5,2,6)  # (count, tot) 튜플을 리턴
print(count, sum)

def test1():
    return
print(test1())
def test2():
    return False
print(test2())

# 모듈 전까지봤다~!