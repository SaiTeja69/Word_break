from itertools import permutations 
list=[]
n=int(input("enter the number of words"))
for i in range(n):
  a=input("Enter! : ")
  list.append(a)
str=input("Enter target string to broken : ")
perm = permutations(range(n)) 
for i in perm: 
  xstr=""
  for j in i:
	  xstr+=list[j]
	  if(xstr==str):
	    l=i
for j in l:
  print(list[j],end=" ") 
