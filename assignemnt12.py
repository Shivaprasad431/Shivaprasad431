x=123456
s=0
while(x>0):
    remainder=x%10
    s=(s*10)+remainder
    x=x//10
print(s)
x=int(input())
if x==1:
    print(f"yes {x} is prime")
# elif x==2:
#     print(f"yes {x} is prime")
# elif x==3:
#    print(f"yes {x} is prime")
elif x>1:
     
    for i in range(2,int(x/2)+1):

        if x%i==0:
            print(f"no {x} is not prime")
            break
    else:
            print(f"yes {x} is prime")
else:
    print(f"no {x} is not prime")

# def PrimeChecker(a):  
#     if a > 1:   
#         for j in range(2, int(a/2) + 1):  
#             if (a % j) == 0:  
#                 print(a, "is not a prime number")  
#                 break   
#         else:  
#             print(a, "is a prime number")   
#     else:  
#         print(a, "is not a prime number")  
# a = int(input("Enter an input number:"))  
# PrimeChecker(a)  
lst=[]
for i in range(100+1):
    if i==1:
       lst.append(1)
    elif i==2:
       lst.append(2)
    elif i>1:
     for j in range(2,i):
      if (i%j)==0:
        break
      else:
            lst.append(i)
            break
        
print(lst)
start=15
end=45
for i in range(start,end+1):
    if (i>1):
        for j in range(2,int(i/2)+1):
            if (i%j)==0:
                break
        else:
            print(i)
from itertools import count
# Give the number n as static input and store it in a variable.
gvnnumb = int(input())
# Loop from 1 to given number using the For loop and the count() function.
for m in count(gvnnumb+1):
        # Inside the For loop, Iterate from 2 to the iterator value
    # of the parent loop using another For loop and range() functions(Nested For loop).
    for n in range(2, m):
        # Check if the inner loop iterator value divides
        # the parent loop iterator value using the if conditional statement.
        if(m % n == 0):
            # If it is true then break the inner for loop using the break keyword.
            break
    else:
        # else print the iterator value of the parent For loop.
        print('The Next prime number of {', gvnnumb, '} is:', m)
        # Break the parent for loop using the break keyword.
        break
x=int(input())
lst=[]
for i in range(x+1):
    if i==1:
       lst.append(1)
    elif i==2:
       lst.append(2)
    elif i>1:
     for j in range(2,i):
      if (i%j)==0:
        break
      else:
            lst.append(i)
            break
        
print(lst)
lst=[]
for i in range(2):
 x=int(input())
 if x==1:
    print(f"yes {x} is prime")
# elif x==2:
#     print(f"yes {x} is prime")
# elif x==3:
#    print(f"yes {x} is prime")
 elif x>1:
     
    for i in range(2,int(x/2)+1):

        if x%i==0:
            lst.append(x)
            print(f"no {x} is not prime")
            break
    else:
            print(f"yes {x} is prime")
 else:
    print(f"no {x} is not prime")
if len(lst)>0:
    print("they are not co prime")
else:
    print("yes they are co prime")
n=int(input())
sum=0
for i in range(n+1):
    sum=sum+i
print(sum)
def compute_gcd(x, y):

   while(y):
       x, y = y, x % y
   return x

# This function computes LCM
def compute_lcm(x, y):
   lcm = (x*y)//compute_gcd(x,y)
   return lcm

num1 = int(input())
num2 = int(input())

print("The L.C.M. is", compute_lcm(num1, num2))
a=int(input())
b=int(input())
print("the hcf is", compute_gcd(a, b))