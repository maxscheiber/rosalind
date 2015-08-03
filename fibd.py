import sys

def fibd(n, m, k):
  ms = []
  for i in xrange(m):
    ms.append([0])
  ms[0] = [1]
  for i in xrange(1, n):
    ms[0].append(sum(map(lambda x: k*x, map(lambda l: l[i-1], ms[1::]))))
    for j in xrange(m-1):
      ms[j+1].append(ms[j][i-1])
  return sum(map(lambda l: l[n-1], ms))
  
n = int(sys.argv[1])
m = int(sys.argv[2])
print(fibd(n, m, 1))
