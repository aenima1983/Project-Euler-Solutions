"""
@author: cosmicchasm1983

"""



#projecteuler.net problem one, June 12, 2019
#calculate the sum of all multiples of 3 and 5 up to a bound
#problem: calculate the sum of all multiples of 3 and 5 up to 1000
#answer: 233168

bound = int(input("Enter upper bound: "))

sums = 0

for i in range(1,bound):
    x = i
    if ((x % 3) == 0) and ((x % 5) == 0):
        sums = sums + x
    elif ((x % 3) == 0):
        sums = sums + x
    elif ((x % 5) == 0):
        sums = sums + x
    else:
        continue

print(sums)
