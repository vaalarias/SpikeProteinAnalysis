'''
NAME
    aminoacid_count.py
  
VERSION
    1.0  29/11/23


AUTHOR
    Valentina Arias & Ana García

DESCRIPTION
    El programa realiza un conteo de los aminoácidos presentes en cada secuencia del formato fasta recibido y genera un plot con las librerías Seaborn.

CATEGORY
   Sequence Analysis    

USAGE

    % python aminoacid_count.py 

ARGUMENTS
    None


'''

import seaborn as sns
import matplotlib.pyplot as plt
from Bio import SeqIO
from collections import Counter
import re

def count_amino_acids(sequence):
    """
    Counts the occurrences of each amino acid in a given protein sequence.

    Parameters:
    sequence (str): A string representing the protein sequence.

    Returns:
    collections.Counter: A Counter object containing the count of each amino acid in the sequence.
    """
    return Counter(sequence)

# fasta path
fasta_file = "../data/s_protein.fasta"

# Histogram for each file
for record in SeqIO.parse(fasta_file, "fasta"):
    amino_acid_count = count_amino_acids(record.seq)
    plt.figure(figsize=(8, 4))
    sns.barplot(x=list(amino_acid_count.keys()), y=list(amino_acid_count.values()), palette="Pastel1")
    plt.title(f'AA frequency - {record.id}')
    plt.xlabel('Aminoacids')
    plt.ylabel('Frequency')
    plt.xticks(rotation=90) 
    plt.tight_layout()
    plt.savefig(f'../results/aa_count_plot_{re.sub("[^a-zA-Z0-9]", "_", record.id)}.png')

