import re


def comma(n):
    if n[0] == '-':
        # 음수 시작은 음수를 제외
        return '-' + comma(n[1:])
    if len(n) <= 3:
        # 999원 이하 단위는 콤마 X
        return n
    if n.find('.') == -1:
        # 들어온 값을 뒤에서 3자리씩 자르고 앞에 ','을 붙이고 재귀 호출
        return comma(n[:-3]) + ',' + n[-3:]
    else:
        return comma(n[:n.find('.')]) + n[n.find('.'):]


def p79():
    print(comma('123456789.654321'))

# p79()


amazonList = ['a1', 'a2', 'a3', 'a4', 'a5', 'b1', 'b2', 'b3', 'b4', 'b5']


def p81_1(amazonList):
    # a4, a5를 지우면 b1 index가 앞으로 오기에 반복이 다 되지 않음
    amazonResult = []
    index = amazonList.index('b1')

    for i in range(index):
        amazonResult.append(amazonList[i])
        if index + i <= len(amazonList) - 1:
            amazonResult.append(amazonList[index+i])
    print(amazonResult)


def p81_2(amazonList):
    amazonResult = []
    index = amazonList.index('b1')

    for i in range(index):
        amazonResult.append(amazonList[i])
        if index + i <= len(amazonList) - 1:
            amazonResult.append(amazonList[index + i])
            temp = index + i

    print(amazonResult + amazonList[temp + 1:])


def p81_3(amazonList):
    index = amazonList.index('b1')

    j = 0
    for i in range(0, len(amazonList)-1, 2):
        print(i)
        amazonList.insert(i + 1, amazonList[index + j])
        amazonList.pop(index + j + 1)
        j += 1
    print(amazonList)


# p81_1(amazonList)
# p81_2(amazonList)
# p81_3(amazonList)

def p87(score):
    numList = []
    domainIndexList = []
    for i, val in enumerate(score):
        if(val.isdecimal()): # 숫자인지 검사
            numList.append(val)
        if(val.isalpha()):
            domainIndexList.append(i)
    
    # print(numList)
    print(domainIndexList)

    for i in domainIndexList:
        print(i)
        print(score[:i])

    split = re.findall('[0-9]{1,2}[^0-9][*#]?', score)
    print(split)


p87('1S2D*3T')
