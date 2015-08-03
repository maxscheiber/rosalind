import sys
from collections import Counter

def dna(l):
  c = Counter(list(l))
  return str(c['A']) + ' ' + str(c['C']) + ' ' + str(c['G']) + ' ' + str(c['T'])

print(dna(sys.argv[1]))
