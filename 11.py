roh=int(input())
kr=list(map(int,input().split()[: roh]))
kr.sort()
for v in kr:
  print(v,end=" ")

