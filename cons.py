import sys
import fasta

def matrix(m):
  n = len(m.values()[0])
  l = []
  for b in ['A', 'C', 'G', 'T']:
    c = []
    for i in xrange(n):
      c.append(sum(map(lambda x: 1 if x == b else 0, map(lambda x: x[i], m.values()))))
    l.append(c)
  return l

def cons(m):
  l = ''
  for i in xrange(len(m[0])):
    a = m[0][i]
    c = m[1][i]
    g = m[2][i]
    t = m[3][i]
    sup = max(a,c,g,t)
    l += 'A' if sup == a else 'C' if sup == c else 'G' if sup == g else 'T'
  return l

m = fasta.read(sys.stdin)
[a, c, g, t] = matrix(m)
print(cons([a, c, g, t]))
print("A: " + ' '.join(map(str, a)))
print("C: " + ' '.join(map(str, c)))
print("G: " + ' '.join(map(str, g)))
print("T: " + ' '.join(map(str, t)))
