'''#1 str=input("enter a string: ")
len=0
for ch in str:
    len+=1
print("length=",len)'''
'''#2 str=input("enter a string:")
count=0
for ch in str:
    if ch in"aeiouuAEIOU":
        count+=1
print("count of vowel:",count)'''
'''#3 str=input("enter a string:")
vowel=0
consonant=0
for ch in str:
    if ch in "aeiouAEIOU":
        vowel+=1
    elif ch.isalpha():
        consonant+=1
print("count of vowel:",vowel)
print("count of consonant:",consonant)'''

#Medium 1 
# str=input("enter a string:")
'''freq_count={}
for ch in str:
    if ch in freq_count:
        freq_count[ch]+=1
    else:
        freq_count[ch]=1
print(freq_count)'''

#Medium 2
'''str=input("enter a string:")
result=""
for ch in str:
    if ch not in result:
        result+=ch
print("string without duplicate characters:", result)'''
#Medium 3
'''str=input("enter a string: ")
for ch in str:
    if str.count(ch)==1:
        print("first non repeating character:",ch)
        break
else:
    print("no non repeating character")'''
#LIST
from numpy import inf


n=[10,20,30,40,50,60,70,80,90,100]
#1 for i in n:
    #print(i)'''
'''#2 sum=0
for i in n:
    sum+=i
print("sum=",sum)'''
'''#3 largest=n[0]
for i in n:
    if i> largest:
        largest=i
print("largest=",largest)'''
'''#4 smallest=n[0]
for i in n:
    if i<smallest:
        smallest=i
print("smallest=",smallest)'''

#Medium
'''first=second=float(-inf)
for i in n:
    if i>first:
        second=first
        first=i
    elif i>second and i!=first:
        second=first
print("second largest number: ",second)'''
#Tuple
'''t=[10,20,30,40,50]
print(t)
print(len(t))
print(t[0])
print(t[-1])
print(t[2])
print("largest=",max(t))
print("smallest=",min(t))''' 
'''def common_elements(lst1,lst2):
    set1=set(lst1)
    set2=set(lst2)
    return(set1&set2)
arr1=[10,20,30]
arr2=[90,70,30]
print("common elements=",common_elements(arr1,arr2))'''
'''a={10,20,30}
b={90,70,30}
print(a.difference(b))
print(a.issubset(b))
print(a.issuperset(b))
print(a.isdisjoint(b))'''
#DICTIONARY
marks={"Rahul":78,"Aman":92,"Priya":85}
print(max(marks.values()))