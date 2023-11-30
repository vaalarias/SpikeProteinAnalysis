'''
NAME
    fasta_generator.py

VERSION 1.0 

AUTHOR
      Ana Marisol García Mejía & Valentina Janet Arias Ojeda 

DESCRIPTION
    

CATEGORY
    
        
USAGE
    % py fasta_generator.py [-h] [file]

ARGUMENTS
    -f FILE, --file FILE 


EXAMPLE
    

'''
from Bio import SeqIO
import os

class FastaCreator:
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def get_file_paths(self):
        file_paths = []
        for file_name in os.listdir(self.folder_path):
            if file_name.endswith(".gb"):
                file_path = os.path.join(self.folder_path, file_name)
                file_paths.append(file_path)
        return file_paths

    def create_fasta(self, output_file):
        file_paths = self.get_file_paths()
        with open(output_file, "w") as fasta_file:  
            for path in file_paths:
                for record in SeqIO.parse(path, "genbank"):
                    isolate = None
                    for feature in record.features:
                        if feature.type == "source":
                            qualifiers = feature.qualifiers
                            isolate = qualifiers.get("isolate", [''])[0]
                        if feature.type == "CDS" and "S" in feature.qualifiers.get('gene', [''])[0]: 
                            protein_seq = feature.qualifiers.get('translation', [''])[0]
                            if isolate:
                                fasta_file.write(f">{isolate}\n")
                                fasta_file.write(f"{protein_seq}\n\n")

# Use the FastaCreator class
folder = "../data"
output = "../data/s_protein.fasta"

fasta_creator = FastaCreator(folder)
fasta_creator.create_fasta(output)
