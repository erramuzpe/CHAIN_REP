#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 12:55:04 2015

@author: asier
"""

# -*- coding: utf-8 -*-
import re
import wx
import os



#mystr = "I want to Remove all white \t spaces, new lines \n and tabs \t"
#print re.sub(r"\W", "", mystr)

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
 

        
def chain_rep(chain,start):
    
    global codon_table
    
    codon=chain[start:start+3]
    if codon_table[codon] == 'A': #substitute for V
        codon = codon_change_to_V[codon]
    else: #substitute for A
        codon = codon_change_to_A[codon]
    chain = chain[:start] + codon + chain[start+3:]
    return chain

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
class ExamplePanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.quote = wx.StaticText(self, label="Your quote :", pos=(20, 30))

        # A multiline TextCtrl - This is here to show how the events work in this program, don't pay too much attention to it
        self.logger = wx.TextCtrl(self, pos=(300,20), size=(200,300), style=wx.TE_MULTILINE | wx.TE_READONLY)

        # Open button
        self.buttonopen =wx.Button(self, label="Open", pos=(200, 300))
        self.Bind(wx.EVT_BUTTON, self.OnClickOpen,self.buttonopen)
        
        # Run button
        self.buttonrun =wx.Button(self, label="Run", pos=(200, 400))
        self.Bind(wx.EVT_BUTTON, self.OnClickRun,self.buttonrun)


        # the position control 
        self.lblpos = wx.StaticText(self, label="Tell me the position you would like to start", pos=(20,60))
        self.editpos = wx.TextCtrl(self, value="1", pos=(150, 60), size=(140,-1))
        self.Bind(wx.EVT_TEXT, self.EvtTextpos, self.editpos)

        # the oligo num control
        self.lbloligo = wx.StaticText(self, label="Tell me the length of oligos:", pos=(20, 90))
        self.editoligo = wx.TextCtrl(self, value="7", pos=(150, 90), size=(140,-1))
        self.Bind(wx.EVT_TEXT, self.EvtTextoligo, self.editoligo)
        
        # the oligo num control
        self.lblline = wx.StaticText(self, label="Tell me the line to start in the output:", pos=(20, 120))
        self.editline = wx.TextCtrl(self, value="1", pos=(150, 120), size=(140,-1))
        self.Bind(wx.EVT_TEXT, self.EvtTextline, self.editline)




    def OnClickOpen(self,event):
        global seq
        
        try:
             """ Open a file"""
             dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.OPEN)
             if dlg.ShowModal() == wx.ID_OK:
                 self.filename = dlg.GetFilename()
                 self.dirname = dlg.GetDirectory()
                 f = open(os.path.join(self.dirname, self.filename), 'r')
                 #self.control.SetValue(f.read())
                 seq = f.read()
                 f.close()
             dlg.Destroy()
             
        except: self.logger.AppendText("There was some problem opening the file" %event.GetId())
    def EvtTextpos(self, event):
        self.logger.AppendText('EvtText: %s\n' % event.GetString())
    def EvtTextoligo(self, event):
        self.logger.AppendText('EvtText: %s\n' % event.GetString())
    def EvtTextline(self, event):
        self.logger.AppendText('fuvlk %s\n' % event.GetString())
    def OnClickRun(self,event):
        global seq
        
        
        self.logger.AppendText(" Click on object with Id %d\n" %event.GetId())



app = wx.App(False)
frame = wx.Frame(None)
panel = ExamplePanel(frame)
frame.Show()
app.MainLoop()



class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        self.dirname=''

        # A "-1" in the size parameter instructs wxWidgets to use the default size.
        # In this case, we select 200px width and the default height.
        wx.Frame.__init__(self, parent, title=title, size=(200,-1))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.CreateStatusBar() # A Statusbar in the bottom of the window

        # Setting up the menu.
        filemenu= wx.Menu()
        menuOpen = filemenu.Append(wx.ID_OPEN, "&Open"," Open a file to edit")
        menuAbout= filemenu.Append(wx.ID_ABOUT, "&About"," Information about this program")
        menuExit = filemenu.Append(wx.ID_EXIT,"E&xit"," Terminate the program")

        # Creating the menubar.
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"&File") # Adding the "filemenu" to the MenuBar
        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.

        # Events.
        self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)

        self.sizer2 = wx.BoxSizer(wx.HORIZONTAL)
        self.buttons = []
        for i in range(0, 6):
            self.buttons.append(wx.Button(self, -1, "Button &"+str(i)))
            self.sizer2.Add(self.buttons[i], 1, wx.EXPAND)

        # Use some sizers to see layout options
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.control, 1, wx.EXPAND)
        self.sizer.Add(self.sizer2, 0, wx.EXPAND)

        #Layout sizers
        self.SetSizer(self.sizer)
        self.SetAutoLayout(1)
        self.sizer.Fit(self)
        self.Show()

    def OnAbout(self,e):
        # Create a message dialog box
        dlg = wx.MessageDialog(self, " A sample editor \n in wxPython", "About Sample Editor", wx.OK)
        dlg.ShowModal() # Shows it
        dlg.Destroy() # finally destroy it when finished.

    def OnExit(self,e):
        self.Close(True)  # Close the frame.

    def OnOpen(self,e):
        """ Open a file"""
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            f = open(os.path.join(self.dirname, self.filename), 'r')
            self.control.SetValue(f.read())
            f.close()
        dlg.Destroy()

app = wx.App(False)
frame = MainWindow(None, "Sample editor")
app.MainLoop()









f =  open('chain.txt','r')
seq = f.read()
f.close()

# seq treatment
seq = re.sub(r'\W', '', seq) #remove all spaces/blanks/newlines
seq = re.sub('[^a-zA-Z]', '', seq)  #remove all non LETTER char
seq = seq.upper()


print 'Your chains first 20:\n', seq[0:20], '\n'

try:
    start_pos = input('Tell me the position you would like to start (1 by default): \n')
except:
    start_pos = 1
    
start_pos -= 1
print 'You selected', seq[start_pos:start_pos+10], 'as your starting point'

seq=seq[start_pos:] #delete the rest of the chain

print 'Your chain now is', seq[:10], '...'





oligo_assert = False
while oligo_assert == False:
    try:
        oligo_num = input('Tell me the length of oligos: \n')
        side_num = 0
        
        if (oligo_num-3)%2 != 0 or (oligo_num-3) <= 0: 
            print 'Incorrect number of oligos, insert a correct one'
        else:
            print 'Number of oligos accepted'
            oligo_assert = True
        
            if (oligo_num-3)%3 == 2:
                side_num = 1       
            else:
                side_num = 2
    except:
        print 'Insert a number, please'
        
        
        
                
codon_num = (oligo_num - 3 - 2*side_num) / 2 / 3




try:
    line_num = input('Tell me the line you would like to print as the first one in \
your output file (1 by default): \n')
except: line_num = 1

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







