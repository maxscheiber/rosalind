import sys

def iev(AA_AA, AA_Aa, AA_aa, Aa_Aa, Aa_aa, aa_aa):
  return 2 * (AA_AA + AA_Aa + AA_aa + 0.75*Aa_Aa + 0.5*Aa_aa)

if len(sys.argv) != 7:
  print('Usage: python iev.py AA-AA AA-Aa AA-aa Aa-Aa Aa-aa aa-aa')
  sys.exit()

AA_AA = int(sys.argv[1])
AA_Aa = int(sys.argv[2])
AA_aa = int(sys.argv[3])
Aa_Aa = int(sys.argv[4])
Aa_aa = int(sys.argv[5])
aa_aa = int(sys.argv[6])

print(iev(AA_AA, AA_Aa, AA_aa, Aa_Aa, Aa_aa, aa_aa))
