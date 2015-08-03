import sys
import fasta

def overlap(m, k):
  l = []
  n = len(m)
  ks = m.keys()
  for i in xrange(n):
    for j in xrange(i+1, n):
      s = m[ks[i]]
      t = m[ks[j]]
      if s[-k:] == t[:k]:
        l.append((ks[i], ks[j]))
      if s[:k] == t[-k:]:
        l.append((ks[j], ks[i]))
  return l

l = overlap(fasta.read(sys.stdin), 3)
for (s, t) in l:
  print(s + ' ' + t)
