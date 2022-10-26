
################################################
# Example of bottom-up and top down design

# problem: Write a function valid_DNA_fasta_file(filename) that returns True if 
# all sequences are valid DNA sequences (consist of A,C,G or T bases)

#----------------------------------
# bottom-up functional abstraction
#----------------------------------

def valid_DNA_seq(s):
    '''
    Parameters
    ----------
    s : str
        input sequence.

    Returns
    -------
    True if valid DNA sequence.
    '''
    s = s.lower() # put in canonical form to handle upper case
    return set(s).issubset(set("acgt"))

# unit tests
def test_valid_DNA_seq():
    assert(valid_DNA_seq("GTGGCGCGA"))  # check valid uppercase
    assert(valid_DNA_seq("gtggcgcga"))  # check valid lowercase
    assert(not valid_DNA_seq("ygtggcgcga"))  # check invalid lowercase
    assert(not valid_DNA_seq("y kz"))  # check only invalid lowercase
    assert(valid_DNA_seq("g")) # check boundary case- 1 element
    assert(valid_DNA_seq("")) # check boundary case- 0 element (what should happen here?)
    
test_valid_DNA_seq()

# Note: In this example we represent a DNA sequence with a python str, but 
# we could also consider defining a user-defined data type for a DNA sequence 
# relevant to this domain,
# or we could use such a type already available in a library such as biopython

# The question asked us to validate multiple sequences, so a function taking
# a list of sequences will be useful

def valid_DNA_seqs(seqs):
    '''
    Parameters
    ----------
    seqs : list of str
        input sequences.

    Returns
    -------
    True if all valid DNA sequence.
    '''
    is_valid = True
    for seq in seqs:
        if not valid_DNA_seq(seq):
            is_valid = False
    return is_valid
        
# unit tests
def test_valid_DNA_seqs():
    assert(valid_DNA_seqs(["GTGGCGCGA", "GTGGCGCGA"]))  # check valid uppercase
    assert(not valid_DNA_seqs(["SSGGCGCGA", "GTGGCGCGA"]))  # check valid uppercase


#----------------------------------
# top-down refinement
#----------------------------------

def valid_DNA_fasta_file(filename):
    '''
    Parameters
    ----------
    s : str
        fasta file filename.

    Returns
    -------
    True if all valid DNA sequence.
    '''

    # what to put here?
    # if we can compute a list of DNA sequences (seq_list) from the file 
    # we can use valid_DNA_seqs()
    seq_list = get_seq_list_from_file(filename) # todo: need to write this function
    return valid_DNA_seqs(seq_list)

def get_seq_list_from_file(filename):
    '''
    Parameters
    ----------
    filename: str
        fasta file filename.

    Returns
    -------
    List of DNA sequences.
    '''
    
    with open(filename, mode="r") as f:
        s = f.read()    # read entire file as string (not memory-efficient)
    s2 = s.split('>')[1:]
    # s2 has each DNA sequence as a separate list element,
    # but there are line feeds ('\n') throughout sequence, 
    # and it includes unneeded sequence description
  #  print(s2)
    
    # So go through each element and remove unneeded "\n" and description
    rl = []
    for pre_seq in s2:
        # todo: need to write a function to clean the pre_seq
        l3 = clean_sequence_data(pre_seq)
        rl.append(l3)
    return rl


def clean_sequence_data(pre_seq):
    '''
    Parameters
    ----------
    pre_seq: str
        DNA seq with embedded newlines and starting description.

    Returns
    -------
    clean DNA sequence.
    '''
    
    l1 = pre_seq.split("\n")  # split at '\n'
    l2 = "".join(l1[1:])      # and reassemble with no character separating 
                                  # subsequences
                                  # and excluding first element (seq description)
    return l2


def test_clean_sequence_data():
    pre_seq = 'gi|119395733|ref|NM_000059.3| Homo sapiens breast cancer 2, early onset (BRCA2), mRNA\nGTGGCGCGAGCTTCTGAAACTAGGCGGCAGAGGCGGAGCCGCTGTGGCACTGCTGCGCCTCTGCTGCGCC\nTCGGGTGTCTTTTGCGGCGGTGGGTCGCCGCCGGGAGAAGCGTGAGGGGACAGATTTGTGACCGGCGCGG\nTTTTTGTCAGCTTACTCCGGCCAAAAAAGAACTGCACCTCTGGAGCGGACTTATTTACCAAGCATTGGAG\n'
    expected_output_seq = 'GTGGCGCGAGCTTCTGAAACTAGGCGGCAGAGGCGGAGCCGCTGTGGCACTGCTGCGCCTCTGCTGCGCCTCGGGTGTCTTTTGCGGCGGTGGGTCGCCGCCGGGAGAAGCGTGAGGGGACAGATTTGTGACCGGCGCGGTTTTTGTCAGCTTACTCCGGCCAAAAAAGAACTGCACCTCTGGAGCGGACTTATTTACCAAGCATTGGAG'
    assert(clean_sequence_data(pre_seq) == expected_output_seq)
    # todo: should add other test cases
    
test_clean_sequence_data()   



# test final function
def test_valid_DNA_fasta_file():
    assert(valid_DNA_fasta_file("multiple_seq_fasta_test.fa"))
    assert(not valid_DNA_fasta_file("invalid_multiple_seq_fasta_test.fa"))

test_valid_DNA_fasta_file()













