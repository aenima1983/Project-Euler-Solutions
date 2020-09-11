#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 13:26:38 2019

@author: cosmicchasm1983
"""

#fibonacci calculator. a direct result of projecteuler.net's inspiration.
#problem two, June 12, 2019.
#Considering the terms of the sequence whose values do not exceed 4 million, 
#find the sum of all even-valued terms.

#exceeding term: 34, at 5702887
#end answer: 4613732

def italiano(x,fibs):
    fib = 1
    fibs.append(fib)
    fibs.append(fib)
    for i in range(2,x):
        if (i == 0) or (i == 1):
            continue
        else:
            fibs.append(fibs[i-1] + fibs[i-2])
    print(fibs[i])
    
fibs = [] #list to be referenced throughout the code

y = int(input("Solve the problem (1), discover (0), or observe sequence\n\t> ")) #prompt for process 

if y == 0:
    x = int(input("How many terms? "))
    italiano(x,fibs)
elif y == 1:
    
    italiano(34,fibs)
    bigsum = 0
    for element in fibs:
        if (element % 2 == 1):
            continue
        else:
            bigsum = bigsum + element
    
    print(f"The sum is equal to: {bigsum}")
elif (y == 2):
    x = int(input("How many terms? "))
    italiano(x,fibs)
    largesum = 0
    for element in fibs:
        largesum = largesum + (element**2)
    print(largesum)
    print(fibs)
        
                
            



