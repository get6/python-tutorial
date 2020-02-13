def spiral(first, second):
    # X유지, Y증가 (0, 1) RIGHT
    # X유지, Y감소 (0, -1) LEFT
    # X증가, Y유지 (1, 0) DOWN
    # X감소, Y유지 (-1, 0) UP
    NEXT_X = [0, 0, 1, -1]
    NEXT_Y = [1, -1, 0, 0]
    # RIGHT, DOWN, LEFT, UP순이지만 TURN이 바뀌기 전 RIGHT인 상태로
    # TURN 순서는 DOWN, UP, LEFT, RIGHT / no가 들어가야 할 순서이다.
    TURN = [2, 3, 1, 0]

    direct = 0  # 위치값 찾기 처음은 RIGHT
    no = 0  # 담길 값, 1씩 증가하면서 넣기 때문에 배열 요소값이 바뀌어야함
    x = 0  # 이전 2차원 배열 요소값
    y = -1  # 이전 1차원 배열 요소값
    arr = [["" for j in range(second)] for i in range(first)]  # print 대상
    # print(arr)

    while no < first * second:
        xpos = x + NEXT_X[direct]  # 2차원 배열 위치 세로크기, direct값에 따라 증감소가 이뤄짐
        ypos = y + NEXT_Y[direct]  # 1차원 배열 위치 가로크기, direct값에 따라 증감소가 이뤄짐
        if -1 < xpos < first and -1 < ypos < second and arr[xpos][ypos] == "":
            # if -1 < xpos < first and -1 < ypos < second:
            # 2차원 배열값이 -1보다 크고 세로크기보다 작아야함
            # 1차원 배열값이 -1보다 크고 가로크기보다 작아야함
            # 해당 요소에 빈값이어야함
            # print(f"xpos:", xpos, f"ypos:", ypos, f"no:", no)
            arr[xpos][ypos] = no
            x = xpos
            y = ypos
            no += 1
        else:
            # print(f"direct:", direct)
            # print(f"xpos:", xpos, f"ypos:", ypos, f"no:", no)
            direct = TURN[direct]

    for row in arr:
        for no in row:
            print("{:4}".format(no), end=" ")  # {:3}은 간격으로 보임
        print()
    # for i in range(first):
    #     for j in range(second):
    #         print(j, end= ' ')
    #     print()


def p93():
    inputData = input("두 개의 숫자를 입력하세요(예시> 6 6):").split()
    spiral(int(inputData[0]), int(inputData[1]))


# p93()
# print 함수 예제(1)
print('1. Hello Python')
print("2. Hello Python")
print('3. Hello "Python"')
print('4. Hello', 'Python.')
print('5. Hello' + 'Python')
# print 함수 예제(2)
print('6. Hello \
Python') # 한 줄
print('''7. Hello 
Python''') # 여러줄
print("""8. Hello 
Python""") # 여러줄
# print 함수 예제(3)
print('9. Hello', end=' ')
print('Python') # 마지막 효과 변경
print('10. Hello', 'Python', sep='*') # , 목록들을 결합하는 방식
# print 함수 예제(4)
print('11. Hello Python'.center(30 * 2)) # 인자값이 없으면 에러
print('12. Hello Python'.rjust(30 * 2))
print('13. Hello Python'.ljust(30))
print('hello python(14)'.capitalize())
print('15. Hello Python'.upper())
# print 함수 예제(5)
number = [ 16, 17,18,19,20]
# {인덱스:폭과 포맷}
for no in number:
    # 0번째 인덱스에 폭을 2만큼 사용하여 출력
    print('{0:2} Hello'.format(no) )
print()
for no in number:
    # 0번째 인덱스에 폭을 5만큼 오른쪽 정렬하여 출력
    print('{0:>5} Hello'.format(no) )