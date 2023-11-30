'''
NAME
    retrieve_strains.py
  
VERSION
    1.0  29/11/23


AUTHOR
    Valentina Arias & Ana Marisol 

DESCRIPTION
    The program receives the name or identifier of the strain/variant through the command line input and searches for the identifier in NCBI using Entrez. It displays the first result on the screen and requests user confirmation for downloading the GenBank file.


CATEGORY
   Database Search

USAGE

    % python retrieve_strains.py {strain_name_1} {strain_name_2} {strain_name_n}

ARGUMENTS
    STRAIN [Strain ...]: Name(s) of the strains or variants(s) to print identifier and file to download


'''
import sys
from Bio import Entrez
from xml.etree import ElementTree as ET

# NCBI's usage policies
Entrez.email = "vjarias@lcg.unam.mx"

# Function to search for SARS-CoV-2 sequences based on the provided strain
def search_sars_cov2(query):
    """
    Searches for SARS-CoV-2 sequences based on the provided query.

    Parameters:
    query (str): The query string used for searching.

    Returns:
    record: A dictionary containing the search results.
    """
    handle = Entrez.esearch(db="nucleotide", term=query)
    record = Entrez.read(handle)
    handle.close()
    return record
def fetch_genbank_record(id,strain):
    """
    Fetches the GenBank record for a given ID and saves it as a file.

    Parameters:
    id (str): The identifier of the record to be fetched.
    strain (str): The name or identifier of the strain/variant for file naming.

    Returns:
    filename (str): The filename of the saved GenBank record.
    """
    handle = Entrez.efetch(db="nucleotide", id=id, rettype="gb", retmode="text")
    record = handle.read()
    filename = f"../data/genbank_record_{strain_name}.gb"
    with open(filename, "w") as file:
        file.write(record)
    handle.close()
    return filename

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide at least one strain name as a command-line argument.")
        sys.exit(1)
    
    # Get all the strains from command-line arguments
    strains = sys.argv[1:]

    for strain_name in strains:
        # Construct the query
        query = f'"Severe acute respiratory syndrome coronavirus 2" AND "{strain_name}" NOT "genome"'

        # Print the strain being searched
        print(f"Searching for {strain_name}...")

        # Perform the search
        search_result = search_sars_cov2(query)
        ids = search_result['IdList']
        #retrieve sequence and accesion identifier
        if ids:
            handle = Entrez.efetch(db='nucleotide', id= ids, rettype='fasta', retmode='xml')
            resultXML = handle.read().decode()
    
            #Parse XML document to review info
            tree = ET.ElementTree(ET.fromstring(resultXML))
            root = tree.getroot()
    
            # Print the ID, and information in the xml file of the first match
            print(f"ID for {strain_name}: {ids[0]}")
            print((root.find('.//TSeq_defline')).text)
            print((root.find('.//TSeq_accver')).text, end='\n\n')
        else:
            print(f"No match found for {strain_name}")
        # Proceed with the file download?
        user_input = input("Proceed with the file download? (yes/no): ").lower()
        if user_input == "yes":
            genbank_records_files = fetch_genbank_record(ids[0],strain_name)
            print("\nGenBank records saved in the 'data' folder:", genbank_records_files)
        else:
            print("File download canceled.")

