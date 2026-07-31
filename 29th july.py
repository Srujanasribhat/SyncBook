#(b) i=int(input("enter the number"))
#if i%2==0:
    #print("remainder is 0")
#else:
 #   print("remainder is not 0")
#(c)
#marks=int(input("enter the marks"))
#if marks>=75:
 #   print("eligible")
#else:
 #   print("not eligible")
#battery=int(input("enter battery percentage"))
#if battery<=20:
 #   print("low battery")
#else:
#    print("battery is ok")
# n=int(input("enter the number: "))
#for i in range(1,11):
 #   print(n,"*",i,"=",n*i)
#n=int(input("enter the number: "))
#sum=0
#for i in range(1,n+1):
 #   sum+=i
#print(sum)
#n=int(input("enter the number:"))
#sum=0
#for i in range(2,n+1,2):
#    sum+=i
#print(sum)
"""str=input("enter the string")
for ch in str:
    print(ch) """
"""num=int(input("enter the number"))
rev=""
for i in str(num):
    rev=i +rev
print(rev)"""
"""num=int(input("enter the number:"))
rev=0
temp=num
while temp>0:
    digit=temp%10
    rev=rev*10+digit
    temp//=10
if num==rev:
    print("palindrome")
else:
    print("not palindrome")"""
"""n=int(input("enter the number:"))
for i in range(2,n):
    if n%i==0:
        print("not prime")
        break
    else:
        print("prime")
        break"""
 #functions
"""def add(a, b):
    return a + b
print(add(6,4))
def square(n):
    return n*n
print(square(6))
def cube(n):
    return n*n*n
print(cube(8))
def check_even_odd(n):
    if n%2==0:
        return "even"
    else:
        return "odd"
print(check_even_odd(16))
def greater(a,b):
    if a>b:
        return a
    else:
        return b
print(greater(6,8))"""

"""def print_primes(a,b):
    for num in range(a,b+1):
        is_prime=True
        for i in range(2,num):
            if num%i==0:
                    is_prime=False
                    break
        if is_prime and num>1:
                    print(num,end="")
a=int(input("enter first number:"))
b=int(input("enter second number:"))
print_primes(a,b)"""
"""def sum_prime(n):
    sum=0
    for num in range(2,n+1):
        is_prime=True
        for i in range(2,num):
            if num%i==0:
                is_prime=False
                break
        if is_prime:
            sum+=num
    return sum
print(sum_prime(10))"""
"""def swap_first_last(n):
    s=str(n)
    if len(s)==1:
        return n
    else:
        swapped=s[-1]+s[1:-1]+s[0]
        return int(swapped)
n=int(input("enter a number:"))
print("after swapping:", swap_first_last(n))"""