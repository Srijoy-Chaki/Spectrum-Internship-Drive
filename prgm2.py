# 2nd Task
# Finding number of trailing zeros in the factorial of a number

try:
    num = int(input('Please enter a number: '))
except:
    print("Sorry!!\nThere is an error")
    quit()

factorial = 1
for x in range(1, num + 1):
    factorial = factorial * x

n = factorial
counter = 0
while True:
    remainder = n % 10
    if remainder == 0:
        counter = counter + 1
    else:
        break
    n = n // 10

print("The number of trailing zeros in the factorial of",num,"is", end = ' ')
print(counter)

