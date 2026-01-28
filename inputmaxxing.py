#inputmaxxing.py


#the problem was that the max input included the firs line which is n
#n is included as part of the input we need to compare max to it, if its bigger than the max than n is new max
#final working version:
#max(m,n) will find the max between the two
n=int(input())
m=int(input())
for _ in range(n-1):
  m = max(m, int(input()))

print(max(m,n))



#another way
i=int(0)
n=int(input())
number=int(input())
maxi=int(number)
while i< (n-1):
    number=int(input())
    if number>maxi:
        maxi=number
    i+=1
if(maxi<n):
    maxi=n

print(maxi)

#max(m,n) will find the max between the two

#m can be 0 because n has to be >= 1
# if the max is bellow 0 then n will be the max
n = int(input())
m = 0
for _ in range(n):
  m = max(m, int(input()))

print(max(m, n))