# 7th Task
# Finding triplets

try:
    a = list(map(int, input('Enter the space separated numbers: ').split()))       # eg: Enter the numbers as 12 4 5 11 19
    k = int(input('Enter the number to which the triplet is summed up to: '))
except:
    print("Sorry!!\nThere is an error")
    quit()

lst = [(x,y,z) for x in a for y in a for z in a if x + y + z == k and x != y and y != z and z != x]
if len(lst)==0:
    print("Sorry!!\nNo such triplet exist in the given list of integers which will sum up to {}".format(k))
    quit()
triplet = list(lst[0])
triplet.sort()
print("One of the triplet is: ", end ='')
for x in triplet:
    print(x, end = ' ')