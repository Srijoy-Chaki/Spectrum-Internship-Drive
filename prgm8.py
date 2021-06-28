# 8th Task
# Drawing a pattern(Hour Glass Shape)

def hour_glass(row_no):
    # Upper half
    for x in range(row_no,0,-1):
        for s in range(row_no,x,-1):
            print('',end = ' ')
        for j in range(0, x):
            print('* ', end = '')
        print()
    # Lower Half
    for x in range(1, row_no):
        for s in range(0, row_no - x - 1):
            print('',end=' ')
        for j in range(0, x+1):
            print('* ', end='')
        print()

half_row_no = 5
hour_glass(half_row_no)