m,n=map(int,input().split())
for i in range(m+1,n):
  sum=0
  no=i
  while(no>0):
    x=no%10
    no=no//10
    y=x**3
    sum=sum+y
  if(i==sum):
    print(sum,end=' ')
  
