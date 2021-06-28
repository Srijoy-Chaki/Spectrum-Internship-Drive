# 3rd Task
# Finding prime numbers in first n integers...

try:
    n = int(input("Enter a number: "))
except:
    print("Sorry!!\nThere is an error")
    quit()

def isPrime(number):
    count = 0
    for factor in range(1, number + 1):
        remainder = number % factor
        if remainder == 0:
            count = count + 1
    if count == 2:
        return 1
    else:
        return 0


print("The prime numbers from 1 to",n,"are", end = ' ')
for integers in range(1, n + 1):
    prime_num = isPrime(integers)
    if prime_num == 1:
        print(integers, end = ' ')