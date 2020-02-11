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

        if(val.isdecimal()):  # 숫자인지 검사
            if score[i-1].isdecimal() == False:
                numList.append(i)
        if(val.isalpha()):
            domainIndexList.append(i)

    # print(numList)
    # print(domainIndexList)

    split = []
    for i, val in enumerate(numList):
        if len(numList) != i+1:
            split.append(score[val:numList[i+1]])
        else:
            split.append(score[val:])
    # print(split)

    # split = re.findall('[\d]{1,2}[^\d][*#]?', score)
    split = re.findall('\d{1,2}\w{1}[*#]?', score)
    print(dartGame(split))

def dartGame(split):
    eachSum = []
    for s in split:
        num = ''
        for e in s:
            if e == '*': # 문자 '*'인 경우
                if len(eachSum) > 1:
                    eachSum[-2] *= 2 # 해당 번호 앞에도 두배
                eachSum[-1] *= 2
            elif e == '#': # 문자 '#'인 경우
                eachSum[-1] *= -1
            else: # 무조건 숫자 or 문자
                if e.isnumeric():
                    num += e # 문자열로 더해서 10을 표현할 수 있음
                if e == 'S':
                    eachSum.append(int(num) ** 1)
                elif e == 'D':
                    eachSum.append(int(num) ** 2)
                elif e == 'T':
                    eachSum.append(int(num) ** 3)
    return sum(eachSum)

# p87('1S2D*3T')
# p87('1D2S#10S')
# p87('1D2S0T')
# p87('1S*2T*3S')
# p87('1D#2S*3S')

string = "파이썬의 파이썬 함수인 정규표현식 함수에 대한 예제입니다."

print(re.search('함수', string).start())
print(re.search('함수', string).end())
print(re.match('파이썬', string).start()) # 처음과 같은 지 확인
print(re.findall('함수', string))

