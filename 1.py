roh=int(input())
kr=list(map(int,input().split()[: roh]))
kr.sort()
for i in kr:
  print(i,end=" ")
