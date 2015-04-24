# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 12:55:04 2015

@author: asier
"""

# -*- coding: utf-8 -*-

        
def chain_rep(seq,old,new):
    new_seq = ''
    
    for x_ in xrange(0, len(seq), 3):
        codon = seq[x_: x_+3]
        if codon == old:
            new_seq += new
        else: new_seq += codon
    return new_seq

def reverseComplement(sequence):
  complement = {'a':'t','c':'g','g':'c','t':'a','n':'n'}
  return "".join([complement.get(nt.lower(), '') for nt in sequence[::-1]])


# Main4

f =  open('chain.txt','r')
seq = f.read()

print 'Your chains first 20:\n', seq[0:20], '\n'

start_pos = input('Tell me the position you would like to start: \n')
start_pos -= 1
print 'You selected', seq[start_pos:start_pos+10], 'as your starting point'

seq=seq[start_pos:] #delete the rest of the chain

start_codon = input('Tell me the position the first codon starts: \n')
start_codon -= 1
print 'You selected', seq[start_codon:start_codon+3], 'as your starting codon'

#old_trip = raw_input('Tell me the triplet you would like to replace (old): \n')
#new_trip = raw_input('Tell me the triplet you would like to replace for (new): \n')
#check = input('Is that correct?: (Y/N) \n')
#if 

print 'Processing...'

    new_chain = chain_rep(seq[start_pos:],start_codon)
    new_chain_rev = 

print 'The new chain is: \n', new_chain

fname = "new_chain.txt"
file = open(fname, 'w')
file.write(new_chain)
file.close()


seq2=reverseComplement(seq)