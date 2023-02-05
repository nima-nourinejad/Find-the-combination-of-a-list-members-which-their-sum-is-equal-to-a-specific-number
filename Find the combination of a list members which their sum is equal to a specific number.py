def jam(a,x):
  n=len(a)
  out=[]
  for i in range(n):
    for j in range (n):
      if a[i]+a[j]==x and j>i:
        out.append([i,j])
  return out
