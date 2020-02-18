def funcLRU(cacheSize, cities):
    if not(0 <= cacheSize <= 30):
        print('에러:cache의 size를 벗어남')
        return
    if not(0 < len(cities)<= 100000):
        print('에러:도시의 개수를 벗어남')
        return
    citiesLower = []
    for city in cities:
        if not(0 < len(city) <=20):
            print('에러:도시 이름은 20자 이하여야 합니다.')
            return
        if not(city.isalpha()):
            print('에러:도시 이름은 공백, 숫자, 특수문자 등이 없는 영문자여야 합니다.')
            return
        citiesLower.append(city.lower())
    if(cacheSize == 0):
        print(len(cities)*5)
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
            if(len(citiesCache) == cacheSize):
                del citiesCache[0]
                citiesCache.append(city)
            else:
                citiesCache.append(city)
    print(runtime)

def p102():
    testCases = [
        [3, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']],
        [3, ['Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul']],
        [2, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'SanFrancisco', 'Seoul', 'Rome', 'Paris', 'Jeju', 'NewYork', 'Rome']],
        [5, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'SanFrancisco', 'Seoul', 'Rome', 'Paris', 'Jeju', 'NewYork', 'Rome']],
        [2, ['Jeju', 'Pangyo', 'NewYork', 'newyork']],
        [0, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']],
        [31, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']],
        [0, ['Jej*', 'Pangyo', 'Seoul', 'NewYork', 'LA']],
        [0, ['Jejdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd']],
    ]
    for testCase in testCases:
        funcLRU(testCase[0], testCase[1])

p102()