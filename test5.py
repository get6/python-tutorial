def spiral(first, second):
    NEXT_X = [0, 0, 1, -1]
    NEXT_Y = [1, -1, 0, 0]
    TURN = [2, 3, 1, 0]

def p93():
    inputData = input("두 개의 숫자를 입력하세요(예시> 6 6):")
    spiral(int(inputData[0], int(inputData[1])))

p93()
