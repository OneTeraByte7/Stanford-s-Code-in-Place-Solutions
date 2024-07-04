"""Question : Given two equal length strings, return the number of indices
              where the two strings have different characters.
"""

def find_snps(string_1, string_2):
    num_snps = 0
    for i in range(len(dna_1)):
       ch_1 = dna_1[i]
       ch_2 = dna_2[i]
       if ch_1 != ch_2:
          num_snps += 1
    return num_snps
