def p68():
    num = 2
    num = eval('num+5')
    print('2+5의 결과값 =', num)
    print(f'2+5의 결과값 =', num)  # f-string 사용
    exec('print("num+6의 결과값 =", num+6)')

    # exec 적용 객체 사용
    one = {}
    exec("a=1+10+pow(2,2)", one)
    print(one['a'])

    two = 2
    # exec 단일 실행 문구
    exec('print(5*two)')


# p68()

MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                    'C': '-.-.', 'D': '-..', 'E': '.',
                    'F': '..-.', 'G': '--.', 'H': '....',
                    'I': '..', 'J': '.---', 'K': '-.-',
                    'L': '.-..', 'M': '--', 'N': '-.',
                    'O': '---', 'P': '.--.', 'Q': '--.-',
                    'R': '.-.', 'S': '...', 'T': '-',
                    'U': '..-', 'V': '...-', 'W': '.--',
                    'X': '-..-', 'Y': '-.--', 'Z': '--..',
                    '1': '.----', '2': '..---', '3': '...--',
                    '4': '....-', '5': '.....', '6': '-....',
                    '7': '--...', '8': '---..', '9': '----.',
                    '0': '-----', ', ': '--..--', '.': '.-.-.-',
                    '?': '..--..', '/': '-..-.', '-': '-....-',
                    '(': '-.--.', ')': '-.--.-'}

MORSE_CODE_DICT_KEY = list(MORSE_CODE_DICT.keys())
MORSE_CODE_DICT_VALUE = list(MORSE_CODE_DICT.values())

morsecode = {}

for i, val in enumerate(MORSE_CODE_DICT):    
    morsecode[MORSE_CODE_DICT_VALUE[i]] = val

# print(morsecode)
def p70(morse):
    alpha = morse.split(" ")
    print(alpha)
    print("모스부호 결과값:", end="")
    for i in alpha:
        print(morsecode[i].lower(), end="")

# p70('he sleeps early')
# p70('.... . ... .-.. . . .--. ... . .- .-. .-.. -.--')

def isPassRule(numbers):
    if len(numbers) < 1:
        print("항이 없습니다.")
        return False
    
    if numbers[0] == 0:
        print("첫번째 항이 0입니다.")
        return False
    
    if not(numbers[0] <= 3000):
        print("첫번째 항이 3000이하가 아닙니다.")
        return False
    
    if not(numbers[0] == len(numbers) -1):
        print("첫번째 값이 뒤에 수열을 나타내는 n개의 정수가 아닙니다.")
        return False
    return True

def isJollyJumpers(numbers):
    n = numbers[0]
    for i in range(1, n+1):
        temporary = abs(numbers[i] - numbers[i-1])
        print(temporary)
        if temporary == 1:
            pass
        else:
            return False
    return True

def p71():
    while True:
        try:
            value = input()
            print(value)
            print(value.strip())
            print(value.split())
            lineInput = list(map(int, value.strip().split()))
            print(f'입력 값:{lineInput}')
        except (ValueError, TypeError) as e:
            print(e)
            break
        
        if not isPassRule(lineInput):
            continue

        if isJollyJumpers(lineInput):
            print("Jolly")
        else:
            print("Not jolly")

p71()