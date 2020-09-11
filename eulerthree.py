#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 20:55:43 2019

@author: cosmicchasm1983

AFTER EXECUTION, SCROLL UP IN CONSOLE TO LOCATE FACTORIZATION LIST

projecteuler.net problem no. 3: find the largest prime factor of
600851475143

answer: 6857
"""




#projecteuler.net problem no. 3
#prime factor generator
#idea: iterate through all numbers up to a number and check that they 
#divide evenly, then iterate through all numbers up to that factor and check
#for any external factors. copy all generated prime factors to a list,
#and sum them together.
#create a method to facilitate large numbers of iterations
#possibly append values to a list, and constantly cycle through all elements
#via a while loop
#divide divide divide
#define a point in the function that identifies composite numbers
#better and smarter idea: divide the number by i, and recursively define the 
#number each time of even division
#DIRECT RECURSION!!!



import sys


   
def prime(a,lst):
    for i in range(2,a):
        if ((a ** 0.5) % i == 0) and ((a / i) == i):
            lst.append(i)
            lst.append(i)
            print(f"the factorization is: \n\n{lst}\n\n")
            print("this may be bare, but there exists a perfect square...\n")
            sys.exit()
        elif (a % i == 0) and ((a / i) != i):
            #print(f"this number is going to get appended: {i}")
            lst.append(i)
            a = int(a / i)
            if a == 1:
                print(lst)
                print(a)
                sys.stdout.write('scroll up for factorization list\n')
                sys.exit()
            else: 
                #print(f"remaining number: {a}")
                prime(a,lst)
        else:
            #print(f"{i}")
            #print(f"{a}")
            continue
    if len(lst) == 0:
        print(f"{a} is prime")
    #sys.stdout.write('scroll up for factorization list')
    return lst
    return a
            

             
#append number value to 'lst'
#import time
#import alphabet (for assigning new characters to 'for' loop indices)

a = int(input("Number to be split: "))

lst = []

prime(a,lst)





            
#________________________THE ABYSS OF FAILED ATTEMPTS____________________
#for i in range(2,number):
 #   a = i
  #  y = number % a
   # if y == 0:
    #    print('test')
     #   primer(a, lst, number)
    #else:
        #print('oops')
        #continue
        
#def primer(a, lst, number):
 #   j = 0
  #  print('hey!')
   # for h in range(2,a+1):
    ##   if a == h:
      #      lst.append(h)
       # elif x == 0:
        #    print('whoa!')
         #   a = h
          #  primer(a, lst, number)
        #else:
         #   j += 1
          #  print('geez!')
           # continue
        #if j != 0:
         #   exit
        #else:
         #   lst.append(h)
    #exit
    #return j
    #return a
    #return lst

