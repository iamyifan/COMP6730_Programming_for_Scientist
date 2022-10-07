class Sequence:
    ObjectCount=0  # a class variable
    TranscriptionTable = {'A':'A', 'C':'C', 'G':'G', 'T':'U'}
    RETable = {'EcoRI':'GAATTC', 'SalI':'GTCGAC'}
    def __init__(self, seqstring): # self represents an instance of Sequence
        Sequence.ObjectCount = Sequence.ObjectCount + 1
        self.seqstring=seqstring.upper() #seqstring is an attribute of self

    def transcribe(self):
        RNA = ""
        for x in self.seqstring:
            if x in 'ACGT':
                RNA += self.TranscriptionTable[x]
        return RNA

    def restrict(self,enzyme):
        if enzyme in self.RETable: 
            if self.RETable[enzyme] in self.seqstring:
                return True
            else:
                return False
        else:
            return 'Unknown enzyme'
        
#    def __len__(self):
#        return len(self.seqstring)
            
class Plasmid(Sequence):
    def __init__(self, seqstring):
        Sequence.__init__(self,seqstring)

    def mcs(self, restr_list):  # multiple cloning site
        self.restr_list = restr_list
        return restr_list

    def re_in_mcs(self,enzyme):
        if self.restr_list:
            if enzyme in self.restr_list:
                return True
            else:
                return False
