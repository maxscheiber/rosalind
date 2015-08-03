import sys

def fib(n, k):
  l = [1, 1]
  for i in xrange(2, n):
    l.append(l[i-1] + k*l[i-2])
  return l[n-1]

n = int(sys.argv[1])
k = int(sys.argv[2])
print(fib(n, k))
