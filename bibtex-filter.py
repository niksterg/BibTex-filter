# BibTex filter
#
# This script filters a BibTeX file by a list of keys

# Usage: python bibtex-filter.py -i input.bib -o output.bib -k key1,key2,key3
#
# Requirements: bibtexparser (https://bibtexparser.readthedocs.io/en/main/)
# Install with: pip install bibtexparser or conda install -c conda-forge bibtexparser
#
# Author: Nikolaos Stergioulas, Aristotle University of Thessaloniki
#
# Content provided under a Creative Commons Attribution license, CC BY-NC-SA 4.0; 
# code under GNU GPLv3 License. (c)2024 Nikolaos Stergioulas

import bibtexparser
from bibtexparser.bparser import BibTexParser
import argparse

# Create a command-line parser
parser = argparse.ArgumentParser(description='BibTeX Filter')

# Add arguments for input file, output file, and keys string
parser.add_argument('-i', '--input', dest='input_file', nargs='?', default='input.bib', help='Input BibTeX file')
parser.add_argument('-o', '--output', dest='output_file', nargs='?', default='output.bib', help='Output BibTeX file')
parser.add_argument('-k', '--keys', dest='keys_string', default=' ', nargs='?', help='Comma-separated list of keys')

# Parse the command-line arguments
args = parser.parse_args()

# Call the filter_bibtex_file function with the parsed arguments
#filter_bibtex_file(args.input_file, args.output_file, args.keys_string)

def filter_bibtex_file(input_file, output_file, keys_string):
    # Parse keys_string into a list of keys
    keys = [key.strip() for key in keys_string.split(',')]

    # Create a parser that recognizes non-standard entry types
    parser = BibTexParser(common_strings=True)
    parser.customization = bibtexparser.customization.convert_to_unicode
    parser.ignore_nonstandard_types = False

    # Load BibTeX data from input_file
    with open(input_file, 'r') as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file, parser=parser)

    # Filter entries by keys
    filtered_entries = [entry for entry in bib_database.entries if entry.get('ID') in keys]

    # Create a new BibDatabase with the filtered entries
    filtered_bib_database = bibtexparser.bibdatabase.BibDatabase()
    filtered_bib_database.entries = filtered_entries

    # Write the filtered BibDatabase to output_file
    with open(output_file, 'w') as bibtex_file:
        bibtex_file.write(bibtexparser.dumps(filtered_bib_database))

# Usage
filter_bibtex_file(args.input_file, args.output_file, args.keys_string)