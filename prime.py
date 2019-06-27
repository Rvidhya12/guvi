d=int(input())
for i in range(2,d):
  if(d%i==0):
    print("no")
    break
else:
  print("yes")
