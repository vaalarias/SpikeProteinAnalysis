'''
NAME
   histogram.py

VERSION 1.0 

AUTHOR
      Ana Marisol & Valentina Arias 

DESCRIPTION
    This program obtains the length of the sequences by iterating through each sequence in the FASTA format, storing it, and generating a plot using the Matplotlib library.

CATEGORY
    Sequence Analysis
        
USAGE
    % python histogram.py

ARGUMENTS
    None

    

'''
from Bio import SeqIO
import matplotlib.pyplot as plt

# Path to your FASTA file
fasta_file = "../data/s_protein.fasta"

# List to store sequence lengths
sequence_lengths = []

# Get sequence lengths from the FASTA file
for record in SeqIO.parse(fasta_file, "fasta"):
    sequence_lengths.append(len(record.seq))

# Create a histogram of sequence lengths
plt.figure(figsize=(8, 6))
plt.hist(sequence_lengths, bins=20, color='skyblue', edgecolor='black')
plt.title('Histogram of Amino Acid Sequence Lengths')
plt.xlabel('Sequence Length')
plt.ylabel('Frequency')
plt.grid(True)
plt.tight_layout()
plt.savefig("../results/histogram.png")