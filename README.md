# CHAIN_REP

## User Manual Chain_Rep.1

### Before using Chain_Rep.1:
- The program generates mutagenic oligonucleotide primers of pre-defined length for Ala-scanning mutagenesis (substitution to Ala of each residue of a given amino acid sequence) of a cDNA of known sequence.
- The forward and reverse mutagenic primers for each mutation are fully complementary, and all primers have the same length, which is defined by the user.
- The mutated Ala codon (3 nucleotides) is placed in the middle of the primer, with an equal number of nucleotides 5’ and 3’ to it. Therefore, the defined length of mutagenic primers has to be an odd number.
- Input: the program accepts as input .txt files containing the cDNA sequence of interest, and ignores numbers, non-letter characters, spaces, or line breaks. The first letter in the .txt file is considered the first position from the chain (sequence to be mutagenized). Therefore, letter characters other than the nucleotides should be avoided in the file. The user defines where to start the design of primers by defining the position to start in the chain. 
- Output: the program provides a list of consecutively numbered mutagenic primers, forward and reverse, written 5’ to 3’. The numbering of the first forward mutagenic primer can be previously defined by the user.

###  Using Chain_Rep.1:

1. Click the “Open” box and browse for the .txt file containing the cDNA of interest.
2. The 40 first positions of your chain are shown. 
3. Define the length of the mutagenic primers.
4. Define the position at which you would like to start the designing of mutagenic primers. This position indicates the first nucleotide in the first mutagenic primer, and it will depend on the position of the first codon to be mutagenized and on the defined length of the mutagenic primers.
5. Click “Run”.
6. The list of mutagenic primers is displayed in a new .txt file (xxx.txt) created in the folder where the Chain_Rep program was opened.   


---

# SAVER

Method to calculate an optimum experiment number
