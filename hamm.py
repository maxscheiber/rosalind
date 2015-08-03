import sys

def hamm(s, t):
  return sum(map(lambda i: 0 if s[i] == t[i] else 1, range(len(s))))

[s, t] = sys.stdin.read().strip().split('\n')
print(hamm(s, t))
