import seaborn as sns
import matplotlib.pyplot as plt
from Bio import SeqIO
from collections import Counter
import re

# Obtener la frecuencia de cada aminoácido en una secuencia de proteínas
def count_amino_acids(sequence):
    return Counter(sequence)

# Ruta de tu archivo FASTA
fasta_file = "../data/s_protein.fasta"

# Crear un gráfico de barras por cada secuencia en el archivo FASTA
for record in SeqIO.parse(fasta_file, "fasta"):
    amino_acid_count = count_amino_acids(record.seq)
    plt.figure(figsize=(8, 4))
    sns.barplot(x=list(amino_acid_count.keys()), y=list(amino_acid_count.values()))
    plt.title(f'AA frequency - {record.id}')
    plt.xlabel('Aminoacids')
    plt.ylabel('Frequency')
    plt.xticks(rotation=90) 
    plt.tight_layout()
    plt.savefig(f'../results/aa_count_plot_{re.sub("[^a-zA-Z0-9]", "_", record.id)}.png')

