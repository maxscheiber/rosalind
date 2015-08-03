import sys

m = {}
m["UUU"] = 'F'
m["UUC"] = 'F'
m["UUA"] = 'L'
m["UUG"] = 'L'
m["UCU"] = 'S'
m["UCC"] = 'S'
m["UCA"] = 'S'
m["UCG"] = 'S'
m["UAU"] = 'Y'
m["UAC"] = 'Y'
m["UAA"] = "Stop"
m["UAG"] = "Stop"
m["UGU"] = 'C'
m["UGC"] = 'C'
m["UGA"] = "Stop"
m["UGG"] = 'W'
m["CUU"] = 'L'
m["CUC"] = 'L'
m["CUA"] = 'L'
m["CUG"] = 'L'
m["CCU"] = 'P'
m["CCC"] = 'P'
m["CCA"] = 'P'
m["CCG"] = 'P'
m["CAU"] = 'H'
m["CAC"] = 'H'
m["CAA"] = 'Q'
m["CAG"] = 'Q'
m["CGU"] = 'R'
m["CGC"] = 'R'
m["CGA"] = 'R'
m["CGG"] = 'R'
m["AUU"] = 'I'
m["AUC"] = 'I'
m["AUA"] = 'I'
m["AUG"] = 'M'
m["ACU"] = 'T'
m["ACC"] = 'T'
m["ACA"] = 'T'
m["ACG"] = 'T'
m["AAU"] = 'N'
m["AAC"] = 'N'
m["AAA"] = 'K'
m["AAG"] = 'K'
m["AGU"] = 'S'
m["AGC"] = 'S'
m["AGA"] = 'R'
m["AGG"] = 'R'
m["GUU"] = 'V'
m["GUC"] = 'V'
m["GUA"] = 'V'
m["GUG"] = 'V'
m["GCU"] = 'A'
m["GCC"] = 'A'
m["GCA"] = 'A'
m["GCG"] = 'A'
m["GAU"] = 'D'
m["GAC"] = 'D'
m["GAA"] = 'E'
m["GAG"] = 'E'
m["GGU"] = 'G'
m["GGC"] = 'G'
m["GGA"] = 'G'
m["GGG"] = 'G'

def prot(l):
  r = ""
  for i in xrange(0, len(l)/3):
    p = m[l[3*i] + l[3*i + 1] + l[3*i + 2]]
    if p == "Stop":
      break
    else:
      r += p
  return r

print(prot(sys.argv[1]))
