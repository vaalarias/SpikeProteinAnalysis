'''
NAME
    fasta_generator.py

VERSION 1.0 

AUTHOR
      Ana Marisol & Valentina Arias
DESCRIPTION
    This program iterates through the list of GenBank files using the Seq.IO library. It accesses the features (dictionaries) of each GenBank file, extracting the sequence of the S protein and the isolate (the strain). Then saves this information in FASTA format into a single file.

CATEGORY
    Data Processing
    
USAGE
    % python fasta_generator.py

ARGUMENTS
    None


'''
from Bio import SeqIO
import os

class FastaCreator:
    def __init__(self, folder_path):

        self.folder_path = folder_path

    def get_file_paths(self):
        """
    Retrieve the paths of GenBank files within the specified folder.

    Args:
    - self: The object instance.

    Returns:
    - file_paths (list of str): A list containing paths to GenBank files (ending with '.gb')
      within the specified folder_path.

    This method scans the folder specified by folder_path attribute, searches for files with the
    '.gb' extension, and constructs a list of paths for all the found GenBank files. It returns
    this list of file paths.
    """
        file_paths = []
        for file_name in os.listdir(self.folder_path):
            if file_name.endswith(".gb"):
                file_path = os.path.join(self.folder_path, file_name)
                file_paths.append(file_path)
        return file_paths

    def create_fasta(self, output_file):
        """
    Create a FASTA file from GenBank files.

    Args:
    - self: The object instance.
    - output_file (str): The name of the output FASTA file.

    The function retrieves file paths using `get_file_paths()`, reads GenBank files, and extracts
    relevant information to create a FASTA file containing protein sequences. It iterates through
    each GenBank file, extracts the isolate information and protein sequences for genes with the
    'S' gene marker. Then, it writes these sequences into the specified output_file in FASTA format.
    If the isolate information is available, it is used as the header for each protein sequence.
        """
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

# Path to access the data
folder = "../data"
output = "../data/s_protein.fasta"
# Use of the FastaCreator class
fasta_creator = FastaCreator(folder)
fasta_creator.create_fasta(output)
