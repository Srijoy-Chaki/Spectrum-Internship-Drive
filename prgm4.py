# 4th task
# Finding the Greatest Common Divisor

try:
    a = list(map(int, input('Enter the space seperated numbers: ').split()))     # eg: Enter the numbers as 16 8 256 1024
except:
    print("Sorry!!\nThere is an error")
    quit()

def gcd(num1,num2):
    if num1 == 0:
        return num2
    elif num2 == 0:
        return num1
    elif num1 == num2:
        return num1
    elif num1 > num2:
        return gcd(num1-num2, num1)
    return gcd(num1, num2-num1)

x = a[0]
y = a[1]
z = gcd(x, y)
for i in range(2, len(a)):
    z = gcd(z, a[i])

print('The greatest common divisor of the given list of numbers is',z)