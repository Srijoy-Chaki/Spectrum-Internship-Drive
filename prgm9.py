# 9th task
# To find the nth smallest number

try:
    a = list(map(int,input('Enter the space separated numbers: ').split()))               # eg: Enter the numbers as 7 15 3 4 18 1
    n = int(input('Enter the value of n to find the nth smallest integer from the above list of integers: '))
except:
    print("Sorry!!\nThere is an error")
    quit()

def getposition(arr, position):
    a.sort()
    req_num = a[position - 1]
    return req_num

if n == 1:
    print('1st smallest number is', end=' ')
elif n == 2:
    print('2nd smallest number is', end=' ')
elif n == 3:
    print('3rd smallest number is', end=' ')
else:
    print('{}th smallest number is'.format(n), end =' ')
print(getposition(a, n))