result = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        if str(i * j) == str(i * j)[::-1] and i * j > result:
            result = i * j
print(result)
print()

input1 = "1.0"
input2 = "1.1.99"

array1 = input1.split(".")
array2 = input2.split(".")

for i in range(len(array1)):
    if int(array1[i]) > int(array2[i]):
        print(input1 + " > " + input2)
        break
    elif int(array1[i]) < int(array2[i]):
        print(input2 + " > " + input1)
        break
print()

x = "1.23.12"  # input('버전을 입력하세요 :')
y = "1.1223"  # input('비교할 버전을 입력하세요 :')
if x == y:
    print(x, "==", y)
else:
    splitX = x.split(".")
    splitY = y.split(".")
    print(splitX, splitY)
    if len(splitX) < len(splitY):
        rangelen = len(splitX)
    else:
        rangelen = len(splitY)
    for i in range(rangelen):
        if splitX[i] > splitY[i]:
            print(x, " > ", y)
            break
        elif splitX[i] < splitY[i]:
            print(x, " < ", y)
            break
    else:
        if len(x) > len(y):
            print("최종버전 비교")
            print(x, " > ", y)
        elif len(x) < len(y):
            print("최종버전 비교")
            print(x, " < ", y)
print()

inputNum = int(input("숫자를 입력하세요:"))
result = 0

for x in range(1, inputNum + 1):
    for y in range(1, x):
        if x % y == 0:
            print(result)


for i in range(1, inputNum + 1):
    for j in range(1, i):
        if i % j == 0:
            result += int(j)

    if result == i:
        print("%d" % (result))

    retult = 0
