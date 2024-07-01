1.You are given three numbers A, B & C. Print the largest amongst these three numbers.

Input Description:
Three numbers are provided to you.

Output Description:
Find and print the largest among the three

Sample Input :
1
2
3
Sample Output :
3

Answer:

def largest(a,b,c):
    if a>=b and a>=c:
        largest=a
    elif b>=c:
        largest=b
    else:
        largest=c
    return largest
a=int(input())
b=int(input())
c=int(input())

print(largest(a,b,c))

---------------------------------------------------------------------------------------------------------------

2. You are provided with a number check whether its odd or even. 

Print "Odd" or "Even" for the corresponding cases.

Note: In case of a decimal, Round off to nearest integer and then find the output. Incase the input is zero, print "Zero".

Input Description:
A number is provided as the input.

Output Description:
Find out whether the number is odd or even. Print "Odd" or "Even" for the corresponding cases. Note: In case of a decimal, Round off to nearest integer and then find the output. In case the input is zero, print "Zero".

Sample Input :
2
Sample Output :
Even

Answer:

A=float(input())
if(A%2==0):
 print("Even")
elif(A%2!=0):
 print("Odd")
else:
 print("Zero")

 ------------------------------------------------------------------------------------------------------------------

 3.You are given Two Numbers, A and B. If C = A + B. Find C.

Note: Round off the output to a single decimal place.

Input Description:
You are provided with two numbers A and B.

Output Description:
Find the sum of the two numbers (A + B)

Sample Input :
1
1
Sample Output :
2

Answer:

a=int(input())
b=int(input())
sum=a+b
print(sum)

-----------------------------------------------------------------------------------------------------------------------

4.You are given a number A in Kilometers. Convert this into B: Meters and C: Centi-Metres.

Input Description:
A number "A" representing some distance in kilometer is provided to you as the input.

Output Description:
Convert and print this value in meters and centimeters.

Sample Input :
2
Sample Output :
2000
200000

Answer:

A=int(input())
B=A*1000
C=A*100000
print(B)
print(C)

-----------------------------------------------------------------------------------------------------------------------

5. You are provided with a number, "N". Find its factorial.

Input Description:
A positive integer is provided as an input.

Output Description:
Print the factorial of the integer.

Sample Input :
2
Sample Output :
2

Answer:

N=int(input())
fact=1

for i in range(1,N+1):
  fact=fact*i
print(fact)

-------------------------------------------------------------------------------------------------------------------------

6. Print the First 3 multiples of the given number "N". (N is a positive integer)

Note: print the characters with a single space between them.

Input Description:
A positive integer is provided to you as an input.

Output Description:
Print the First 3 multiples of the number with single spaces between them as an output.

Sample Input :
2
Sample Output :
2 4 6

Answer:

N= int(input())
print(*[N * i for i in range(1, 4)])

--------------------------------------------------------------------------------------------------------------------------

7. You are given with a number "N", find its cube.

Input Description:
A positive integer is provided.

Output Description:
Find the cube of the number.

Sample Input :
2
Sample Output :
8

Answer:

N=int(input())
cube=N*N*N
print(cube)

--------------------------------------------------------------------------------------------------------------------------
8. The area of an equilateral triangle is ¼(√3a2) where "a" represents a side of the triangle. You are provided with the side "a". Find the area of the equilateral triangle.

Input Description:
The side of an equilateral triangle is provided as the input.

Output Description:
Find the area of the equilateral triangle and print the answer up to 2 decimal places after rounding off.

Sample Input :
20
Sample Output :
173.21

Answer:

import math
a=int(input())
area=round((math.sqrt(3)/4)*math.pow(a,2),2)
print(area)

---------------------------------------------------------------------------------------------------------------------------
9. You are provided with the radius of a circle "A". Find the length of its circumference.

Note: In case the output is coming in decimal, roundoff to 2nd decimal place. In case the input is a negative number, print "Error".

Input Description:
The Radius of a circle is provided as the input of the program.

Output Description:
Calculate and print the Circumference of the circle corresponding to the input radius up to two decimal places.

Sample Input :
2
Sample Output :
12.57

Answer:

radius=float(input())
import math
math.pi
circumference=2*math.pi*radius
print("{:.2f}".format(circumference))

-------------------------------------------------------------------------------------------------------------------------------

10. You are given A = Length of a rectangle & B = breadth of a rectangle. Find its area “C”.

(A and B are natural numbers)

Input Description:
The inputs are two natural numbers representing the length and the breadth of a rectangle.

Output Description:
Find the area of the rectangle formed by the provided input. Round off the answer to the first decimal place if required.

Sample Input :
2
3
Sample Output :
6

Answer:

A=int(input())
B=int(input())
C=A*B
print(C)

-----------------------------------------------------------------------------------------------------------------------------

11. Write a code to get the input and print it 5 times.

Input Description:
A single line contains an integer N.

Output Description:
Output contains 5 lines with each line having the value N.

Sample Input :
4
Sample Output :
4
4
4
4
4

Answer:

N=int(input())
for i in range(1,6):
  i=N*1
  print(i)

-----------------------------------------------------------------------------------------------------------------------

12. You will be provided with a number. Print the number of days in the month corresponding to that number.

Note: In case the input is February, print 28 days. If the Input is not in valid range print "Error".

Input Description:
The input is in the form of a number.

Output Description:
Find the days in the month corresponding to the input number. Print Error if the input is not in a valid range.

Sample Input :
8
Sample Output :
31

Answer:

N=int(input())
if(N==1 or N==3 or N==5 or  N==7 or  N==8 or N==10 or N==12):
  print(31)
elif(N==4 or  N==6 or  N==9 or  N==11):
  print(30)
elif(N==2):
  print(28)
else:
  print("Error")


---------------------------------------------------------------------------------------------------------------------

13.Using the method of looping, write a program to print the table of 9 till N in the format as follows:
(N is input by the user)

9 18 27...

Print NULL if 0 is input

Input Description:
A positive integer is provided as an input.

Output Description:
Print the table of nine with single space between the elements till the number that is input.

Sample Input :
3
Sample Output :
9 18 27

Answer:

N=int(input())
s=[]
for i in range(1, N+1):
    s.append(i*9)
print(*s)

-----------------------------------------------------------------------------------------------------------------
14.You are provided with two numbers. Find and print the smaller number.

Input Description:
You are provided with two numbers as input.

Output Description:
Print the small number out of the two numbers.

Sample Input :
23 1
Sample Output :
1

Answer:

b=list(map(int,input().split()))
print(min(b))

-----------------------------------------------------------------------------------------------------------------

15.Write a code to get 2 integers A and N. Print the integer A, N times in separate line.

Input Description:
First line contains an integer A. Second line contains an Integer N.

Output Description:
Print the integer A, N times in a separate line.

Sample Input :
2 3
Sample Output :
2
2
2

Answer:

A_N=input().split()
A=int(A_N[0])
N=int(A_N[1])

i=0
while i<N:
    print(A)
    i=i+1
-------------------------------------------------------------------------------------------------------------

16. You are given the coefficients of a quadratic equation in order A, B & C.

Where A is the coefficient of X2,  B is the coefficient of X and C is the constant term in the most simplified form.

Example: For  X2 + 5X + 6 = 0, you are given the input as: 1 5 6.

Write a program to find all of the roots of the quadratic.

Note: The output should be up to 2nd decimal place (round off if needed) and in case of a recurring decimal use braces i.e. for eg: 0.33333..... => 0.33.

Note: Use Shri Dharacharya's Method to solve i.e. X = {-b + √(b² - 4ac) } / 2a & {-b-√(b² -4ac)} / 2a

Input Description:
Three numbers corresponding to the coefficients of x(squared), x and constant are given as an input in that particular order

Output Description:
Print the two values of X after rounding off to 2 decimal places if required.

Sample Input :
1 5 6
Sample Output :
-2.00
-3.00

Answer:

n=input().split()
import math
math.sqrt

a=int(n[0])
b=int(n[1])
c=int(n[2])

alpha=(-b +math.sqrt(b**2-4*a*c))/(2*a)
beta=(-b-math.sqrt(b**2-4*a*c))/(2*a)

print("{:.2f}".format(alpha))
print("{:.2f}".format(beta))

--------------------------------------------------------------------------------------------------
17. You are given with Principle amount($), Interest Rate(%) and Time (years) in that order. Find Simple Interest.

Print the output up to two decimal places (Round-off if necessary).

(S.I. = P*T*R/100)

Input Description:
Three values are given to you as the input. these values correspond to Principle amount, Interest Rate and Time in that particular order.

Output Description:
Find the Simple interest and print it up to two decimal places. Round off if required.

Sample Input :
1000 2 5
Sample Output :
100.00

Answer:

a=list(input().split(" "))

Principle_amount = float(a[0])

Interest_Rate = float(a[1])

Time = float(a[2])

if Principle_amount > 0 and Interest_Rate > 0 and Time >0:

  SI = ( Principle_amount * Interest_Rate * Time) / 100

  print(round(SI,2))

-------------------------------------------------------------------------------------------------------

18. Write a code to get an integer N and print values from 1 till N in a separate line.

Input Description:
A single line contains an integer N.

Output Description:
Print the values from 1 to N in a separate line.

Sample Input :
5
Sample Output :
1
2
3
4
5

Answer:

N=int(input())
for i in range(1,N+1):
    print(i)

----------------------------------------------------------------------------------------------------

19. Let "A"  be a string. Remove all the whitespaces and find it's length.

Input Description:
A string is provide as an input

Output Description:
Remove all the whitespaces and then print the length of the remaining string.

Sample Input :
Lorem Ipsum
Sample Output :
10

Answer:

A = input()

b =A.replace(" ","")

print(len(b))

-----------------------------------------------------------------------------------------------------

20.Let "A" be a year, write a program to check whether this year is a leap year or not.

Print "Y" if its a leap year and "N" if its a common year.

Input Description:
A Year is the input in the form of a positive integer.

Output Description:
Print "Y" if its a leap year and "N" if its a common year.

Sample Input :
2020
Sample Output :
Y

Answer:

A=int(input())
if A%4==0:
  print("Y")
elif(A%4!=0):
  print("N")

------------------------------------------------------------------------------------------------------

21. Write a program to get a string as input and reverse the string without using temporary variable.

Input Description:
A single line containing a string.

Output Description:
Print the reversed string.

Sample Input :
GUVI
Sample Output :
IVUG

Answer:

A=input()
print(A[ : :-1])

----------------------------------------------------------------------------------------------------

22. Write a code to get 2 integers as input and find the HCF of the 2 integer without using recursion or Euclidean algorithm.

Input Description:
A single line containing 2 integers separated by space.

Output Description:
Print the HCF of the integers.

Sample Input :
2 3
Sample Output :
1

Answer:

num=input().split()
A=int(num[0])
N=int(num[1])
while A!=N:
  if A>N:
    A=A-N
  else:
    N=N-A
print(N)

--------------------------------------------------------------------------------------------------------

23. Write a code to get an integer N and print the values from N to 1.

Input Description:
A single line contains an integer N.

Output Description:
Print the values from N to 1 in a separate line.

Sample Input :
10
Sample Output :
10
9
8
7
6
5
4
3
2
1

Answer:

N=int(input())

for i in range(N,0,-1):
  
  print(i)

----------------------------------------------------------------------------------------------------

24.You are given with a number A i.e. the temperature in Celcius. Write a program to convert this into Fahrenheit. 

Note: In case of decimal values, round-off to two decimal places.

Input Description:
A number is provided in Celcius as the input of the program.

Output Description:
The output shall be the temperature converted into Fahrenheit corresponding to the input value print up to two decimal places and round off if required.

Sample Input :
12
Sample Output :
53.60

Answer:

celcius=int(input())
fahrenheit=(1.8*celcius)+32
print("{:.2f}".format(fahrenheit))

-----------------------------------------------------------------------------------------------------

25.Write a code to get an integer N and print the digits of the integer.

Input Description:
A single line contains an integer N.

Output Description:
Print the digits of the integer in a single line separated by space,

Sample Input :
348
Sample Output :
3 4 8

Answer:

N=input()
new=[int(x) for x in N]
print(*new)

------------------------------------------------------------------------------------------------------

26.Write a code get an integer number as input and print the odd and even digits of the number separately.

Input Description:
A single line containing an integer.

Output Description:
Print the even and odd integers of the integer in a separate line.

Sample Input :
1234
Sample Output :
2 4
1 3

Answer:

a=list(input())
odd=[]
even=[]
for i in a:
    i=int(i)
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(*sorted(even))
print(*sorted(odd))

----------------------------------------------------------------------------------------------------

27.Write a code to get an integer N and print the sum of  values from 1 to N.

Input Description:
A single line contains an integer N.

Output Description:
Print the sum of values from 1 to N.

Sample Input :
10
Sample Output :
55

Answer:

N=int(input())
sum=0
for i in range(N+1):
  sum=sum+i
print(sum)
---------------------------------------------------------------------------------------------------

28. You are provided with a number "N", Find the Nth term of the series: 1, 4, 9, 16, 25, 36, 49, 64, 81, .......

(Print "Error" if N = negative value and 0 if N = 0).

Input Description:
An integer N is provided to you as the input.

Output Description:
Find the Nth term in the provided series.

Sample Input :
18
Sample Output :
324

Answer:

N=int(input())

if N==0:
    print('0')
elif N<0:
    print('Error')
else:
    a=N**2
    print(a)

-------------------------------------------------------------------------------------------------

29. Write a code get an integer number as input and print the sum of the digits.

Input Description:
A single line containing an integer.

Output Description:
Print the sum of the digits of the integer.

Sample Input :
124
Sample Output :
7

Answer:

def getSum(n):
    
    sum = 0
    for i in str(n): 
      sum += int(i)      
    return sum
   
n = int(input())
print(getSum(n))

----------------------------------------------------------------------------------------------------
30. Write a code to get an integer N and print the even values from 1 till N in a separate line.

Input Description:
A single line contains an integer N.

Output Description:
Print the even values from 1 to N in a separate line.

Sample Input :
6
Sample Output :
2
4
6

Answer:

N=int(input())
for i in range(1,N+1):
  if i%2==0:
    print(i)

