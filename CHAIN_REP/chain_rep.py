# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 12:55:04 2015

@author: asier
"""

# -*- coding: utf-8 -*-
bases = ['T', 'C', 'A', 'G']
codons = [a+b+c for a in bases for b in bases for c in bases]
amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
codon_table = dict(zip(codons, amino_acids))
        
def chain_rep(seq,start):
    
    global codon_table
    
    codon=seq[start+9:start+12]
    if codon_table[codon] == 'A': #substitute for V
        codon = 'VVV'
    else: #substitute for A
        codon = 'AAA'
    seq = seq[:start+9] + codon + seq[:start+12]
    print seq
    return seq

def reverseComplement(seq):
  sequence = seq*1
  complement = {'A':'T','C':'G','G':'C','T':'A','N':'N'}
  return "".join([complement.get(nt, '') for nt in sequence[::-1]])

def format_chain(seq,start):
    seq = seq[0:start]+" "+ \
    " ".join(seq[i:i+3] for i in range(start, len(seq)-start, 3)) \
    +" "+ seq[-start:]
    return seq

# Main4

f =  open('chain.txt','r')
seq = f.read()

print 'Your chains first 20:\n', seq[0:20], '\n'

start_pos = input('Tell me the position you would like to start: \n')
start_pos -= 1
print 'You selected', seq[start_pos:start_pos+10], 'as your starting point'

seq=seq[start_pos:] #delete the rest of the chain

print 'Your chain now is', seq[:10], '...'


start_codon = input('Tell me the position the first codon starts: \n')
start_codon -= 1
print 'You selected', seq[start_codon:start_codon+3], 'as your starting codon'

#old_trip = raw_input('Tell me the triplet you would like to replace (old): \n')
#new_trip = raw_input('Tell me the triplet you would like to replace for (new): \n')
#check = input('Is that correct?: (Y/N) \n')
#if 

fname = "new_chain.txt"
file = open(fname, 'w')

length_chain = start_codon*2+7*3 #start_codon + 7 codon + start_codon

print 'Processing...'
for x_ in xrange(0, len(seq), 3):
    
    chain = seq[x_: x_+length_chain] 
    chain_rev = reverseComplement(chain)
    
    if len(chain) != length_chain: break
    
    chain = chain_rep(chain,start_codon)
    chain_rev = chain_rep(chain_rev,start_codon)
    
    chain = format_chain(chain,start_codon)
    chain_rev = format_chain(chain_rev,start_codon)
    
    file.write(chain+ '\n')
    file.write(chain_rev+ '\n \n')
    


file.close()
