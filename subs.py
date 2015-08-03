import sys

def subs(s, t):
  a = []
  for i in xrange(1 + len(s) - len(t)):
    if t == s[i:i+len(t)]:
      a.append(1+i)
  return a

[s, t] = sys.stdin.read().strip().split('\n')
print(' '.join(map(str, subs(s, t))))
