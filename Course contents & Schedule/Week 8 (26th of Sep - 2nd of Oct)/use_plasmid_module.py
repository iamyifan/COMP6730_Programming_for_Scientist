#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 01:24:16 2022

@author: brianparker
"""

from seq_plasmid import Sequence
DNA_seq=Sequence('atgcaagtaggtcccaac')
print(DNA_seq.seqstring)
#DNA_seq

print(DNA_seq.transcribe())

print(len(DNA_seq.seqstring))

#print(len(DNA_seq))  # error without __len__ method

from seq_plasmid import Plasmid

plasmid_seq = Plasmid('acgaattcgtacagc')
print(plasmid_seq.seqstring)
print(plasmid_seq.restrict('EcoRI'))
print(plasmid_seq.restrict('EcoR1'))
print(plasmid_seq.pcs('EcoRI'))
print(plasmid_seq.re_in_pcs('EcoRI'))
print(plasmid_seq.re_in_pcs('EcoR1'))
plasmid_seq.pcs(['EcoRI','SalI'])
print(plasmid_seq.re_in_pcs('EcoR1'))
print(plasmid_seq.re_in_pcs('EcoRI'))

test2 = Sequence('acgaattcgtacagc')
print(test2.restrict('EcoRI'))
#test2.pcs('EcoRI')  # error- not defined for a Sequence

# polymorphic function call example
def reverse_DNA_seq(seq):
    seq.seqstring = seq.seqstring[::-1]

reverse_DNA_seq(DNA_seq)
print(DNA_seq.seqstring)

reverse_DNA_seq(plasmid_seq)
print(plasmid_seq.seqstring)


