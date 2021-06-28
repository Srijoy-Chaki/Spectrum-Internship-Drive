# 5th task
# To find first n perfect numbers

try:
    n = int(input('Enter the number of prefect numbers to be obtained: '))
except:
    print("Sorry!!\nThere is an error")
    quit()


def isperfect(number):
    lst = []
    half_num = number // 2
    if half_num == 0:
        return 0
    else:
        for x in range(1, half_num + 1):
            rem = number % x
            if rem == 0:
                lst.append(x)
        add = sum(lst)

        if add == number:
            return 1
        else:
            return 0


integer = 1
lst2 = []
counter = 0
while True:
    perfect_no = isperfect(integer)
    if perfect_no == 1:
        lst2.append(integer)
        counter = counter + 1
    integer = integer + 1
    if counter == n:
        break
print("The first", n,"perfect numbers are", end = ' ')
for req_no in lst2:
    print(req_no, end = ' ')
