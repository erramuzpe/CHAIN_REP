# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 12:55:04 2015

@author: asier
"""

# -*- coding: utf-8 -*-
import sys

bases = ['T', 'C', 'A', 'G']
codons = [a+b+c for a in bases for b in bases for c in bases]
amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
codon_table = dict(zip(codons, amino_acids))
codon_change_to_V = {
		"GCA" : "GTA",
		"GCC" : "GTC",
		"GCG" : "GTG",
		"GCT" : "GTT"
	}
codon_change_to_A = { #GCA GCC GCG GCT
    "TTT":"GCT", "TTC":"GCC", "TTA":"GCA", "TTG":"GCG",
    "TCT":"GCT", "TCC":"GCC", "TCA":"GCA", "TCG":"GCG",
    "TAT":"GCT", "TAC":"GCC", "TAA":"GCA", "TAG":"GCG",
    "TGT":"GCT", "TGC":"GCC", "TGA":"GCA", "TGG":"GCG",
    "CTT":"GCT", "CTC":"GCC", "CTA":"GCA", "CTG":"GCG",
    "CCT":"GCT", "CCC":"GCC", "CCA":"GCA", "CCG":"GCG",
    "CAT":"GCT", "CAC":"GCC", "CAA":"GCA", "CAG":"GCG",
    "CGT":"GCT", "CGC":"GCC", "CGA":"GCA", "CGG":"GCG",
    "ATT":"GCT", "ATC":"GCC", "ATA":"GCA", "ATG":"GCG",
    "ACT":"GCT", "ACC":"GCC", "ACA":"GCA", "ACG":"GCG",
    "AAT":"GCT", "AAC":"GCC", "AAA":"GCA", "AAG":"GCG",
    "AGT":"GCT", "AGC":"GCC", "AGA":"GCA", "AGG":"GCG",
    "GTT":"GCT", "GTC":"GCC", "GTA":"GCA", "GTG":"GCG",
    "GAT":"GCT", "GAC":"GCC", "GAA":"GCA", "GAG":"GCG",
    "GGT":"GCT", "GGC":"GCC", "GGA":"GCA", "GGG":"GCG"
	}
 

        
def chain_rep(seq,start):
    
    global codon_table
    
    codon=seq[start+12:start+15]
    if codon_table[codon] == 'A': #substitute for V
        codon = codon_change_to_V[codon]
    else: #substitute for A
        codon = codon_change_to_A[codon]
    seq = seq[:start+12] + codon + seq[start+15:]
    return seq

def reverseComplement(seq):
  sequence = seq*1
  complement = {'A':'T','C':'G','G':'C','T':'A','N':'N'}
  return "".join([complement.get(nt, '') for nt in sequence[::-1]])

def format_chain(seq,start):
    seq = seq[0:start]+" "+ \
    " ".join(seq[i:i+3] for i in range(start, len(seq)-start, 3)) \
    +" "+ seq[len(seq)-start:]
    return seq


#Main start

f =  open('chain.txt','r')
seq = f.read()

print 'Your chains first 20:\n', seq[0:20], '\n'

start_pos = input('Tell me the position you would like to start: \n')
start_pos -= 1
print 'You selected', seq[start_pos:start_pos+10], 'as your starting point'

seq=seq[start_pos:] #delete the rest of the chain

print 'Your chain now is', seq[:10], '...'


oligo_num = input('Tell me the length of oligos: \n')
side_num = 0

if (oligo_num-3)%2 != 0: 
    print 'Incorrect number of oligos, this will halt'
    sys.exit()
else:
    print 'Number of oligos accepted'
    if (oligo_num-3)%3 == 2:
        side_num = 1       
    else:
        side_num = 2
                
codon_num = (oligo_num - 3 - 2*side_num) / 2 / 3

line_num = input('Tell me the line you would like to print as the first one in \
your output file (1?): \n')

fname = "new_chain.txt"
file = open(fname, 'w')

print 'Processing...'
for x_ in xrange(0, len(seq), 3):
    
    chain = seq[x_: x_+oligo_num] 
      
    if len(chain) != oligo_num: break
    
    chain = chain_rep(chain,side_num)
    chain_rev = reverseComplement(chain)    
    
    file.write(str(line_num) + " " + chain + '\n')
    file.write(str(line_num+1) + " " + chain_rev + '\n \n')
    
    line_num += 2

file.close()
print 'Results in new_chain.txt'