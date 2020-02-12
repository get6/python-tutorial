def spiral(first, second):
    # X유지, Y증가 (0, 1) RIGHT
    # X유지, Y감소 (0, -1) LEFT
    # X증가, Y유지 (1, 0) DOWN
    # X감소, Y유지 (-1, 0) UP
    NEXT_X = [0, 0, 1, -1]
    NEXT_Y = [1, -1, 0, 0]
    # RIGHT, DOWN, LEFT, UP순이지만 TURN이 바뀌기 전 RIGHT인 상태로 
    # TURN 순서는 DOWN, LEFT, UP RIGHT
    TURN = [2, 3, 1, 0] 

    direct, no = 0, 0
    x, y = 0, -1
    arr = [["" for j in range(second)] for i in range(first)]
    print(arr)

    while no < first * second:
        xpos = x + NEXT_X[direct]
        ypos = y + NEXT_Y[direct]
        print(f"X:",x,f"NEXT_X", NEXT_X[direct])
        print(f"Y:",y,f"NEXT_Y", NEXT_Y[direct])
        if -1 < xpos < first and -1 < ypos < second and arr[xpos][ypos] == "":
            print(f"xpos:", xpos, f"ypos:", ypos)
            arr[xpos][ypos] = no
            x = xpos
            y = ypos
            no += 1
        else:
            print(f"direct:", direct)
            direct = TURN[direct]

    for row in arr:
        for no in row:
            print("{:3}".format(no), end=" ")
        print()
    # for i in range(first):
    #     for j in range(second):
    #         print(j, end= ' ')
    #     print()


def p93():
    inputData = input("두 개의 숫자를 입력하세요(예시> 6 6):").split()
    spiral(int(inputData[0]), int(inputData[1]))


p93()
