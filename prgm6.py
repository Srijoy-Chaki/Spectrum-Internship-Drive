# 6th Task
# To count the number of occurance of a substring in a given string...

def substringCount(inputString, subString):
    count = 0
    x = 0
    subString_len = len(subString)
    while x < len(inputString):
        check = inputString[x:x + subString_len]
        if check == subString:
            count = count + 1
        x = x + 1
    return count

s = input('Enter a String: ').strip()
f = input('Enter the substring: ').strip()

counter = substringCount(s, f)
print("The number of times", f,"occur in", s,"is",end=' ')
print(counter)