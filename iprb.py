import sys
from math import factorial as f

def C(n, r):
  return f(n) / f(r) / f(n-r)

def iprb(k, m, n):
  N = C(k + m + n, 2)
  # dom-dom + hetero-hetero + dom-hetero + dom-rec + hetero-rec
  return 1.0*C(k,2)/N + 0.75*C(m,2)/N + 1.0*k*m/N + 1.0*k*n/N + 0.5*m*n/N

k = float(sys.argv[1]) # homozygous dominant
m = float(sys.argv[2]) # heterozygous
n = float(sys.argv[3]) # homozygous recessive
print(iprb(k, m, n))
