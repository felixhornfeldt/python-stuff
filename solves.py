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

    for z in range(0,x):
        tp = []
        for i in range(0,y):
            tp.append(z*i)
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
    lines = []

    while True:
        string = input()
        if string:
            lines.append(string)
        else:
            break    
        
    for x in lines:
        print(x.upper())

# q9()

#----------------------------------------#
# Question 10
# Level 2

# Question:
# Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world

def q10():
    inp = input()
    arr = inp.split(" ")
    op = []
    for x in arr:
        if x in op:
            continue
        else:
            op.append(x)
    
    return sorted(op)

# print(" ".join(q10()))

#----------------------------------------#
# Question 11
# Level 2

# Question:
# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
# Example:
# 0100,0011,1010,1001
# Then the output should be:
# 1010
# Notes: Assume the data is input by console.

def q11(s):
    arr = s.split(",")
    op = []
    for i in arr:
        q = 3
        a = 0
        z = 0
        while q >= 0:
            a += (2**q)*int(i[z])
            z += 1
            q -= 1
            
        if a%5 == 0:
            op.append(i)

    return op

# print(",".join(q11(input())))

#----------------------------------------#
# Question 12
# Level 2

# Question:
# Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.

def q12():
    num = [str(x) for x in range(1000,3001) if int(str(x)[0])%2 == 0 and int(str(x)[1])%2 == 0 and int(str(x)[2])%2 == 0 and int(str(x)[3])%2 == 0]
    
    return num

# print(",".join(q12()))

#----------------------------------------#
# Question 13
# Level 2

# Question:
# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3

def q13(s):
    arr = [x for x in s if x != " "]
    l = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U", "V", "W", "X", "Y", "Z", "Å", "Ä", "Ö"] 
    n = [str(x) for x in range(0,10)]
    lt = 0
    nt = 0
    for x in arr:
        if x.upper() in l:
            lt += 1
        elif x in n:
            nt += 1
        else:
            pass
    
    return ("LETTERS "+str(lt)+"\nDIGITS "+str(nt))

# print(q13(input()))

#----------------------------------------#
# Question 14
# Level 2

# Question:
# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9

def q14(s):
    arr = [x for x in s if x != " "]
    ul = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U", "V", "W", "X", "Y", "Z", "Å", "Ä", "Ö"] 
    dl = [x.lower() for x in ul]
    uln = 0
    dln = 0
    for x in arr:
        if x in ul:
            uln += 1
        elif x in dl:
            dln += 1
        else:
            pass
    
    return ("UPPER CASE "+str(uln)+"\nlower case "+str(dln))

# print(q14(input()))

#----------------------------------------#
# Question 15
# Level 2

# Question:
# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106

def q15(n):
    n1 = int("%s%s" % (n,n))
    n2 = int("%s%s%s" % (n,n,n))
    n3 = int("%s%s%s%s" % (n,n,n,n))

    return (n+n1+n2+n3)

# print(q15(int(input())))

#----------------------------------------#
# Question 16
# Level 2

# Question:
# Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
# Suppose the following input is supplied to the program:
# 1,2,3,4,5,6,7,8,9
# Then, the output should be:
# 1,3,5,7,9

def q16(s):
    op = [x for x in s.split(",") if int(x)%2 != 0]

    return ",".join(op)

# print(q16(input()))

#----------------------------------------#

# Question 17
# Level 2

# Question:
# Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
# D 100
# W 200

# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
# 500

def q17():
    trans = {"D":0,"W":0}
    while True:
        t = input()
        if t:
            t = t.split(" ")
            trans[t[0]] += int(t[1])
        else: 
            break
    
    return (trans['D']-trans['W'])

# print(q17())

#----------------------------------------#
# Question 18
# Level 3

# Question:
# A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
# Example
# If the following passwords are given as input to the program:
# ABd1234@1,a F1#,2w3E*,2We3345
# Then, the output of the program should be:
# ABd1234@1

def q18():
    s = input()
    s = [x for x in s.split(",") if len(x) >= 6 and len(x) <= 12]
    s_arr = ["$","#","@"]
    op = []
    for x in s:
        u = False
        l = False
        d = False
        spec = False
        for i in x:
            if i.isupper():
                u = True
            if i.islower():
                l = True
            if i.isdigit():
                d = True
            if i in s_arr:
                spec = True
        
        if u and l and d and spec:
            op.append(x)
    
    return op
    

# print(q18())

#----------------------------------------#
# Question 19
# Level 3

# Question:
# You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers. The tuples are input by console. The sort criteria is:
# 1: Sort based on name;
# 2: Then sort based on age;
# 3: Then sort by score.
# The priority is that name > age > score.
# If the following tuples are given as input to the program:
# Tom,19,80
# John,20,90
# Jony,17,91
# Jony,17,93
# Json,21,85
# Then, the output of the program should be:
# [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]

def q19():
    inputs = []
    while True:
        inp = input()
        if inp:
            inputs.append(inp)
        else:
            break
    
    return sorted([tuple(x.split(",")) for x in inputs], key=lambda x: (x[0],x[1],x[2]))

# print(q19())

#----------------------------------------#
# Question 20
# Level 3

# Question:
# Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

class Q20():
    def __init__(self):
        pass

    def generator(self, n):
        return (",".join([str(x) for x in range(0,n) if x%7==0]))
    pass

q_20 = Q20()

# print(q_20.generator(700))

#----------------------------------------#
# Question 21
# Level 3

# Question£º
# A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# ¡­
# The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
# Example:
# If the following tuples are given as input to the program:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# Then, the output of the program should be:
# 2

def q21():
    arr = []
    while True:
        inp = input()
        if inp:
            arr.append(tuple(inp.split(" ")))
        else:
            break

    org_poi = [0,0]
    for x in arr:
        if x[0].upper() == "UP":
            org_poi[1] += int(x[1])
        elif x[0].upper() == "DOWN":
            org_poi[1] -= int(x[1])
        elif x[0].upper() == "LEFT":
            org_poi[0] -= int(x[1])
        elif x[0].upper() == "RIGHT":
            org_poi[0] += int(x[1])
    
    return (round((org_poi[0]**2+org_poi[1]**2)**(1/2)))

# print(q21())

#----------------------------------------#
# Question 22
# Level 3

# Question:
# Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically. 
# Suppose the following input is supplied to the program:
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
# Then, the output should be:
# 2:2
# 3.:1
# 3?:1
# New:1
# Python:5
# Read:1
# and:1
# between:1
# choosing:1
# or:2
# to:1

def q22():
    inp = input().split(" ")
    d = {}

    for x in inp:
        if x not in d.keys():
            d[x] = 1
        else:
            d[x] += 1
    
    return d

print(q22())