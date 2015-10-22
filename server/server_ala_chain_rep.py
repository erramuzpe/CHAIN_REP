# A very simple alachainrep app to get started with...
from bottle import default_app, route, post, get, request

import re


BASES = ['T', 'C', 'A', 'G']
CODONS = [a+b+c for a in BASES for b in BASES for c in BASES]
AMINO_ACIDS = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
CODON_TABLE = dict(zip(CODONS, AMINO_ACIDS))
CODON_CHANGE_TO_V = {
    "GCA" : "GTA",
    "GCC" : "GTC",
    "GCG" : "GTG",
    "GCT" : "GTT"
}
CODON_CHANGE_TO_A = { #GCA GCC GCG GCT
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
COMPLEMENT = {'A':'T', 'C':'G', 'G':'C', 'T':'A', 'N':'N'}

def chain_rep(chain, start):
    """
    chain_rep
    """
    codon = chain[start:start+3]
    if CODON_TABLE[codon] == 'A': #substitute for V
        codon = CODON_CHANGE_TO_V[codon]
    else: #substitute for A
        codon = CODON_CHANGE_TO_A[codon]
    chain = chain[:start] + codon + chain[start+3:]
    return chain

def reverse_complement(chain):
    """
    reverse_complement
    """
    return "".join([COMPLEMENT.get(nt, '') for nt in chain[::-1]])


@route('/')
@get('/')
def index():
    return '''

        <form action="/run" method="post" enctype="multipart/form-data">
            <p>Start <input name="start" type="text" value="1" /></p>
            <p>Primer len <input name="primer" type="text" value="27" /></p>
            <p>Output line <input name="output_line" type="text" value="1" /></p>


          <input type="file" name="data" />
          <input name="RUN" type="submit" value="RUN" /></p>
        </form>

    '''




@post('/run')
def do_upload():

    try:
        start_pos = int(request.forms.get('start'))
        oligo_num = int(request.forms.get('primer'))
        line_num = int(request.forms.get('output_line'))
    except:
        return "Problem loading variables. Not numbers?"

    try:
        data = request.files.get('data')
    except:
        return "Problem loading data. File corrupt or not adecuate?"

    seq = data.file.read() # small files =.=

    seq = re.sub(r'\W', '', seq)
    #remove all non LETTER char
    seq = re.sub('[^a-zA-Z]', '', seq)
    seq = seq.upper()

    start_pos -= 1
    try:
        side_num = 0

        if (oligo_num-3)%2 != 0 or (oligo_num-3) <= 0:
            return "Incorrect number of oligos insert a correct one"
        else:
            #self.logger.AppendText('Length of primers accepted \n')
            side_num = (oligo_num-3) / 2
    except:
        return "Insert a number"


    try:
        dum_file = ""
        for i in xrange(0, len(seq), 3):

            chain = seq[i: i+oligo_num]

            if len(chain) != oligo_num:
                break

            chain = chain_rep(chain, side_num)
            chain_rev = reverse_complement(chain)

            dum_file += (str(line_num) + " " + chain + ' <br> ')
            dum_file += (str(line_num+1) + " " + chain_rev + ' <br>  <br> ')

            line_num += 2
    except:
        return "Insert a number"


    return '''<p>%s''' % (dum_file)


application = default_app()

