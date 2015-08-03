import sys
from collections import Counter

def complement(b):
  return 'A' if b == 'T' else 'T' if b == 'A' else 'C' if b == 'G' else 'G' if b == 'C' else b

def revc(l):
  return ''.join(map(lambda b: complement(b), l)[::-1])

print(revc(sys.argv[1]))
