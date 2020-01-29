import math


def p38():
    inputNum = int(input("숫자를 입력하세요 :"))
    result = 0

    for i in range(1, inputNum + 1):
        for j in range(1, i):
            if i % j == 0:
                result += j
                print("%d %d " % (i, j))

        if result == i:
            print("완전수 :%d " % (result))

        result = 0


def p40():
    print(sum(range(1, 11)))
    print(sum(range(1, 11)) ** 2)
    print(sum(x**2 for x in range(1, 11)))
    print(abs(sum(range(1, 101)) ** 2))
    print(sum(x**2 for x in range(1, 101)))
    print(sum(range(1, 101)) ** 2 - sum(x**2 for x in range(1, 101)))


def p41(n):
    for i in range(1, n + 1):
        print('0' * (n - i) + "X" * i)


def p44():
    print(isinstance(list(range(1, 101)), str))
    print(isinstance(str(list(range(1, 101))), str))
    print(type(list(range(1, 101))) == str)
    print(type(str(list(range(1, 101)))) == str)
    print(str(list(range(1, 10001))).count('8'))
    sumi = 0
    for i in str(list(range(1, 10001))):
        if i == "8":
            sumi += 1
            pass
    print(sumi)


def p46():
    List = [1, 2, 3, 4]
    List.append(5)
    print(List)


def p47():
    List1 = ['b', 'c', 'a']
    List2 = [4, 2, 3, 1]
    List1.sort()
    List1.reverse()
    List2.sort()
    print(List1)
    print(List2)


def p49():
    List = [2, 1, 2, 3, 4]
    List.remove(1)
    print(List)

    List = [1, 1, 1, 2, 3]
    print(List.count(1))

    List = [1, 2]
    List.extend([3, 4])
    print(List)

    List = [1, 2, 3]
    List.insert(4, 5)
    print(List)
    print(List.index(0))
    pass


def sumEachNum(n):
    sumValue = n
    while n > 0:
        sumValue += n % 10
        n //= 10
    return sumValue


rangeNum = 15


def p53():

    generatorExist = [sumEachNum(i) for i in range(rangeNum)]
    print(generatorExist)

    generatorNoExist = [i for i in range(
        rangeNum) if not (i in generatorExist)]
    print(generatorNoExist)

    print(sum(generatorNoExist))
    print()


def getSelfNumber(n):
    sumValue = n
    while n > 0:
        print("값 {}".format(sumValue))
        sumValue += n % 10
        print("나머지 {}".format(n % 10))
        # 소수점까지 계산해줌
        # n = n / 10
        n = n // 10
        print("나누기 {}".format(n))
        pass
    return sumValue


# inputRange = int(input('숫자를 입력하세요 :'))


def p54(inputRange):
    first = 0
    fibonacci = 1
    nextfibonach = 0

    while first < inputRange:
        print(first, end=', ')
        nextfibonach = first + fibonacci
        first = fibonacci
        fibonacci = nextfibonach


def fibonacci(n):
    a = [0, 1]
    while n >= (a[-1] + a[-2]):
        a.append(a[-1] + a[-2])
    print(a)
    pass


# p54(inputRange)
# print()
# fibonacci(inputRange)

def p57(num):
    result = False
    for i in range(1, num + 1):
        if num % i == 0:
            result = not result
            if result == True:
                print("{}번째 스위치 켜짐".format(i))
            elif result == False:
                print("{}번째 스위치 꺼짐".format(i))

    if result == False:
        print("no")
    else:
        print("yes")


# p57(inputRange)

def p60():
    num = 120
    sum = 0
    for i in range(1, num+1):
        print(math.sqrt(i))
        print(math.sqrt(i) % 1)
        if(math.sqrt(i) % 1 == 0):
            print("석방된 죄수번호방 %d" % i)
            sum += 1

    print("석방된 죄수는 %d명입니다." % sum)

# p60()


def p62(a, b, c):
    s = (a+b+c)/2
    print(s)
    heron = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print(heron)
    r = heron/s
    print(r)

# p62(12,12,10)

def p64(digit):
    multiplier = pow(2,digit)
    rSum = 0
    # while multiplier > 0:
    #     rSum += multiplier % 10
    #     multiplier //= 10
    # print(rSum)
    multiplier = str(multiplier)
    for i in multiplier:
        print(i)
        rSum += int(i)
    print("2^1000의 각 자릿수의 합=", rSum)

# p64(1000)
print(eval('+'.join(str(2**1000))))
print(eval('+'.join(str(pow(2,1000)))))
print(sum(int(num) for num in str(pow(2,1000))))