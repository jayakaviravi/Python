1.Write a code to get the input in the given format and print the output in the given format

Input Description:
To take an integer value

Output Description:
Print the integer value

Sample Input :
2
Sample Output :
2

Answer:

a=input()
print(a)


2.Write a code to get the input in the given format and print the output in the given format

Input Description:
A single line contains integers separated by space

Output Description:
Print the integer list of integers separated by space

Sample Input :
2 3 4 5 6 7 8
Sample Output :
2 3 4 5 6 7 8

Answer

a=list(map(int,input().split()))
print(*a)


3. Write a code to get the input in the given format and print the output in the given format.

Input Description:
First-line indicates two integers which are the size of array and 'K' value. Second-line indicates an integer contains elements of an array.

Output Description:
Print the taken input in the same format.

Sample Input :
5 3
1 2 3 4 5
Sample Output :
5 3
1 2 3 4 5

Answer

a=list(map(int,input().split()))
b=list(map(int,input().split()))

print(*a)
print(*b)

4. Write a code to get the input in the given format and print the output in the given format

Input Description:
First-line indicates two integers separated by space. Second-line indicates two integers separated by space. Third-line indicates two integers separated by space.

Output Description:
Print the input in the same format.

Sample Input :
2 4
2 4
2 4
Sample Output :
2 4
2 4
2 4

Answer

a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))

print(*a)
print(*b)
print(*c)

5.Write a code to get the input in the given format and print the output in the given format

Input Description:
Three integers are given in line by line.

Output Description:
Print the integers in a single line separate by space.

Sample Input :
2
4
5
Sample Output :
2 4 5

Answer

a=int(input())
b=int(input())
c=int(input())
print(a,b,c)

6. Write a code to get the input in the given format and print the output in the given format

Input Description:
First-line indicates two integers separated by space. Second-line indicates three integers separated by space. Third-line indicates three integers separated by space

Output Description:
Print the input in the same format.

Sample Input :
2 5
2 5 6
2 4 5
Sample Output :
2 5
2 5 6
2 4 5

Answer

a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
print(*a)
print(*b)
print(*c)

7.Write a code to get the input in the given format and print the output in the given format

Input Description:
A single line contains a string.

Output Description:
Print the characters in a string separated by space.

Sample Input :
guvi
Sample Output :
g u v i

Answer

string = input()
print(*string)

8.Write a code to get the input in the given format and print the output in the given format.

Input Description:
A single line contains three float values separated by space.

Output Description:
Print the float value separated by line.

Sample Input :
2.3 4.5 7.8
Sample Output :
2.3
4.5
7.8

Answer

a = input().split()
for i in a:
    print(i)

9. Write a code to get the input in the given format and print the output in the given format.

Input Description:
A single line contains a string.

Output Description:
Print the characters in a string separated by line.

Sample Input :
guvigeek
Sample Output :
g
u
v
i
g
e
e
k

Answer

s=input()
for i in s:
    print(i)


10.Write a code to get the input in the given format and print the output in the given format.

Input Description:
A single line contains a string.

Output Description:
Print the characters in a string separated by comma.

Sample Input :
guvi
Sample Output :
g,u,v,i

Answer

s=input()
a=len(s)
for i in range(0,a-1):
    print(s[i]+',',end='')
print(s[a-1])