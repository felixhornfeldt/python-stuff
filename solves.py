"""
Link: https://github.com/zhiwehu/Python-programming-exercises/blob/master/100%2B%20Python%20challenging%20programming%20exercises.txt
"""
#----------------------------------------#
# Question 1
# Level 1

# Question:
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

def q1():
    n = [x for x in range(2000,3201) if x%7 == 0 and x%5 != 0]
    return n

# print(q1())

#----------------------------------------#
# Question 2
# Level 1

# Question:
# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320

def q2(n):
    if n == 0:
        return 1
    return n * q2(n-1)
    
# print(q2(8))

#----------------------------------------#
# Question 3
# Level 1

# Question:
# With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

def q3(n):
    d = {}
    for i in range(1,n+1):
        d[i] = i*i
    
    return d

# print(q3(20))

#----------------------------------------#
# Question 4
# Level 1

# Question:
# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

def q4(s):
    a = s.split(',')
    b = tuple()
    for i in a:
        b = b + (i,)
    
    return [a,b]

# print(q4("34,67,55,33,12,98"))

#----------------------------------------#
# Question 5
# Level 1

# Question:
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

class Q5():
    def __init__(self):
        self.stig = ""

    def getString(self, string):
        self.stig = string
    
    def printString(self):
        print(self.stig.upper())

# q5 = Q5()
# q5.getString(input())
# q5.printString()

#----------------------------------------#
# Question 6
# Level 2

# Question:
# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
# Example
# Let us assume the following comma separated input sequence is given to the program:
# 100,150,180
# The output of the program should be:
# 18,22,24

def q6(s):
    a = [int(i) for i in s.split(',')]

    op = []
    for i in a:
        q = ((2 * 50 * i) / 30)**(1/2)
        op.append(round(q))
    
    return op

# print(q6('100,150,180'))

#----------------------------------------#
# Question 7
# Level 2

# Question:
# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,¡­Y-1.
# Example
# Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 

def q7(x,y):
    arr = []

    for x in range(0,x):
        tp = []
        for i in range(0,y):
            tp.append(x*i)
        arr.append(tp)

    return arr

# print(q7(3,5))

#----------------------------------------#
# Question 8
# Level 2

# Question:
# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world

def q8(s):
    return sorted(s.split(','))
    
# print(','.join(q8("without,hello,bag,world")))

#----------------------------------------#
# Question 9
# Level 2

# Question£º
# Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT

def q9():

    pass