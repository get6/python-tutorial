def funcLRU(cacheSize, cities):
    if not (0 <= cacheSize <= 30):
        print("에러:cache의 size를 벗어남")
        return
    if not (0 < len(cities) <= 100000):
        print("에러:도시의 개수를 벗어남")
        return
    citiesLower = []
    for city in cities:
        if not (0 < len(city) <= 20):
            print("에러:도시 이름은 20자 이하여야 합니다.")
            return
        if not (city.isalpha()):
            print("에러:도시 이름은 공백, 숫자, 특수문자 등이 없는 영문자여야 합니다.")
            return
        citiesLower.append(city.lower())
    if cacheSize == 0:
        print(len(cities) * 5)
        return
    citiesCache = []
    runtime = 0
    for city in citiesLower:
        if city in citiesCache:
            runtime += 1
            citiesCache.remove(city)
            citiesCache.append(city)
        else:
            runtime += 5
            if len(citiesCache) == cacheSize:
                del citiesCache[0]
                citiesCache.append(city)
            else:
                citiesCache.append(city)
    print(runtime)


def p102():
    testCases = [
        [
            3,
            [
                "Jeju",
                "Pangyo",
                "Seoul",
                "NewYork",
                "LA",
                "Jeju",
                "Pangyo",
                "Seoul",
                "NewYork",
                "LA",
            ],
        ],
        [
            3,
            [
                "Jeju",
                "Pangyo",
                "Seoul",
                "Jeju",
                "Pangyo",
                "Seoul",
                "Jeju",
                "Pangyo",
                "Seoul",
            ],
        ],
        [
            2,
            [
                "Jeju",
                "Pangyo",
                "Seoul",
                "NewYork",
                "LA",
                "SanFrancisco",
                "Seoul",
                "Rome",
                "Paris",
                "Jeju",
                "NewYork",
                "Rome",
            ],
        ],
        [
            5,
            [
                "Jeju",
                "Pangyo",
                "Seoul",
                "NewYork",
                "LA",
                "SanFrancisco",
                "Seoul",
                "Rome",
                "Paris",
                "Jeju",
                "NewYork",
                "Rome",
            ],
        ],
        [2, ["Jeju", "Pangyo", "NewYork", "newyork"]],
        [0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]],
        [31, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]],
        [0, ["Jej*", "Pangyo", "Seoul", "NewYork", "LA"]],
        [0, ["Jejdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd"]],
    ]
    for testCase in testCases:
        funcLRU(testCase[0], testCase[1])


# p102()


def overturnList(argList):
    # 2차원 배열을 받았다고 가정하면 
    # 1차원 배열에 요소값이 2차원 배열에 요소값 위치로 옮겨지게 된다.
    # 2차원 배열에 요소값은 1차원 배열에 순서로 적용이 된다.
    # argListTmp = list(zip(argList[0], argList[1], argList[2], argList[3], argList[4]))
    argListTmp = list(zip(*argList))
    return [list(argListTmp[i]) for i in range(len(argListTmp[0]))]


def pung(argList):
    # argListTmp = [[] for i in range(0, 5)]
    argListTmp = list(argList)
    # set(parameter) 들어온 인자에 중복되는 숫자를 줄여준다.
    for i in range(0, 5):
        if (len(set(argListTmp[i][0:5])) == 1) and not (0 in argListTmp[i][0:5]):
            # 전부 다 같은 숫자인 경우와 임시변수에 0이 존재하지 않을 경우
            argListTmp[i][0:5] = [-1, -1, -1, -1, -1]
        if (len(set(argListTmp[i][0:4])) == 1) and not (0 in argListTmp[i][0:4]):
            # 처음부터 4개까지 다 같은 숫자인 경우
            argListTmp[i][0:4] = [-1, -1, -1, -1]
        if (len(set(argListTmp[i][1:5])) == 1) and not (0 in argListTmp[i][1:5]):
            # 1부터 4개까지 다 같은 숫자인 경우
            argListTmp[i][1:5] = [-1, -1, -1, -1]
        if (len(set(argListTmp[i][0:3])) == 1) and not (0 in argListTmp[i][0:3]):
            # 처음부터 3개까지 다 같은 숫자인 경우
            argListTmp[i][0:3] = [-1, -1, -1]
        if (len(set(argListTmp[i][1:4])) == 1) and not (0 in argListTmp[i][1:4]):
            # 1부터 3개까지 다 같은 숫자인 경우
            argListTmp[i][1:4] = [-1, -1, -1]
        if (len(set(argListTmp[i][2:5])) == 1) and not (0 in argListTmp[i][2:5]):
            # 2부터 3개까지 다 같은 숫자인 경우
            argListTmp[i][2:5] = [-1, -1, -1]
    return argListTmp


def p114():
    matrix = []
    # 입력 형식
    # for i in range(5):
    #     matrix.append(list(map(int, input().split())))
    matrix = [
        [2, 4, 1, 2, 1],
        [3, 4, 2, 3, 3],
        [2, 4, 1, 2, 2],
        [4, 4, 4, 1, 2],
        [4, 2, 3, 3, 2],
    ]

    # matrixTmp = [[] * 5 for i in range(0, 5)]
    matrixTmp = [[] for i in range(0, 5)]

    isValidCalc = True
    while isValidCalc:
        matrixTmp = list(matrix)
        verticalMatrix = overturnList(matrixTmp)
        verticalMatrix = pung(verticalMatrix)
        verticalMatrix = overturnList(verticalMatrix)

        matrix = pung(matrix)

        isValidCalc = False
        for i in range(0, 5):
            for j in range(0, 5):
                if (matrix[i][j] == -1) or (verticalMatrix[i][j] == -1):
                    matrix[i][j] = -1
                    isValidCalc = True

        matrixTmp = list(matrix)
        verticalMatrix = overturnList(matrixTmp)
        for i in range(0, 5):
            if -1 in verticalMatrix[i]:
                cnt = verticalMatrix[i].count(-1)
                for j in range(0, cnt):
                    verticalMatrix[i].remove(-1)
                    verticalMatrix[i].insert(0, 0)
        matrix = overturnList(verticalMatrix)

    print("최종")
    for i in range(0, 5):
        print(matrix[i])


p114()


def p118():
    s = ""
    print(len(s))
    s = "문자열입니다ㅎ!aA"
    print(len(s))
    listA = []
    print(len(listA))
    listA = [1, "한글", 1.5]
    print(len(listA))
    tupleA = (1, 1, 2, 3)
    print(len(tupleA))
    setTupleA = set((1, 1, 2, 3, 2))  # 중복 제거
    print(len(setTupleA))
    setListA = set([1, 1, 2, 3])  # 중복 제거
    print(len(setListA))


# p118()


def p119():
    a = [5, 6, 7, 8, 9]
    b = ["c", "d", "e", "f", "g"]
    for x in zip(a, b):
        print(x)

    for x, y in zip(a, b):
        print(x, y)


# p119()
