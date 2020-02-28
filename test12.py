def calc(values):
    sum = None
    # try...except...else
    try:
        sum = values[0] + values[1] + values[2]
    except IndexError  as err:
        print('인덱스에러')
    except Exception as err:
        print(str(err))
    else: 
        print('에러없음')
    finally:
        print(sum)

def calc2(values):
    sum = None
    try:
       sum = values[0] + values[1] + values[2]
    except (IndexError, ValueError):
        print('오류발생')
 
    print(sum)

# 테스트
# calc([1,2,3,6]) # 출력: 에러없음 6
# calc([1,2])     # 출력: 인덱스에러 None

def check():
    pass

# pass 를 사용한 예
try:
    check()
except FileExistsError:
    pass

# total = -1
total = 0
# raise 를 사용한 예
if total < 0 :
    raise Exception('Total Error')
    # raise Exception, 'Total Error'

try:
    fp = open('test.txt', 'r')
    try:
        lines = fp.readlines()
        print(lines)
    finally:
        fp.close()
except IOError:
    print('파일에러')


try:
    # 반드시 리소스를 해제
    with open('test.txt', 'r') as fp:
        lines = fp.readlines()
        print(lines)
except IOError:
    print('파일에러')