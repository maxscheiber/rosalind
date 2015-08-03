def read(f):
  m = {}
  k = None
  v = ''
  for l in f:
    l = l.strip()
    if l[0] == '>':
      if k != None:
        m[k] = v
        v = ''
      k = l[1::]
    else:
      v += l
  m[k] = v # for the last one
  return m
