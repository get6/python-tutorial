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

p44()
