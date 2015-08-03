import sys

def rna(l):
  return l.replace('T', 'U')

print(rna(sys.argv[1]))
