import sys
import fasta

def gc(m):
  max_k = None
  max_p = 0.0
  for k in iter(m):
    v = m[k]
    p = len(filter(lambda x: x == 'C' or x == 'G', list(v))) / float(len(v))
    if p > max_p:
      max_k = k
      max_p = p
  return (max_k, 100 * max_p)

m = fasta.read(sys.stdin)
max_k, max_p = gc(m)
print(max_k)
print(max_p)
