import argparse
import os
from Bio import SeqIO
import re
import blast_101_search
import smith_waterman_search
import calc_bit_and_evalues

# Function to validate if input file exists and if it contains fasta format sequences
# File checking functionality adapted from - https://stackoverflow.com/questions/11540854/file-as-command-line-argument-for-argparse-error-message-if-argument-is-not-va
def file_exists(parser, filename):
    if not os.path.exists(filename):
        parser.error(f"Input file does not exist > {filename}")
    if not os.path.isfile(filename):
        parser.error(f"Input is not a file > {filename}")
    return(filename)


def fasta_file_validate(parser, filename):
    try:
        count = 0
        for _ in SeqIO.parse(filename, 'fasta'):
            count +=1
        if count < 1:
            parser.error(f"No FASTA format sequences found in file > {filename}")
        else:
            print(f"Found {count} Sequences in FASTA format in {filename}")
    except Exception:
        parser.error(f"Input is not a valid FASTA file > {filename}")
    return(filename)

# def csv_file_validate(parser, filename):


def validate_sequence(parser, seq):
    if not seq:
        parser.error("Looks like your Query String is empty")

    seq = seq.upper()
    # Check if input sequence is a nucelotide or protein sequence 
    # Adpated from https://docs.python.org/3/library/re.html#re.fullmatch
    if re.fullmatch(r"[ATGCN]+", seq):
        parser.error("Looks like your Query String is a Nucleotide sequence not a Protein sequence")
    else:
        return(seq)


def instantiate_parser():
    # Instantiate parser
    parser = argparse.ArgumentParser()
    # Add arg to define which mode we would like - the script that will be run
    # Control input by only allowing a selection of choices
    parser.add_argument('mode',
                        choices=['blast101', 'smith_waterman', 'stats', 'test'],
                        help='Which programme to run: blast101 (a custom blast implementation), smith_waterman (search using full SW algorithm), or stats (calculate statistics from a given CSV file)'
    )

    parser.add_argument(
        '-q', '--query',
        required=False,
        metavar='STRING',
        type=lambda x: validate_sequence(parser, x),
        help="Protein Sequence to Query"
    )

    # Add an argument to take a file as input
    parser.add_argument(
            '-i', '--input',
            required=False,
            metavar='FILE',
            type=lambda x: file_exists(parser, x),
            help='Input FASTA file containing query sequence(s), for stats programme a CSV containing simulation data'
        )

    return(parser)

print("""
##########################################################################################
#                                                                                        #
#                                 Blast 101                                              #
#                                                                                        #
##########################################################################################

Modes:
    - blast101          Run BLAST 101 search, a custom implementation of the SW algorith. Flags: -q <sequence> -i <database>
    - smith_waterman    Run a search with the full Smith-Waterman algorithm. Flags: -q <sequence> -i <database>
    - stats             Calculate statistics from a CSV file. Flags -i <csvfile>
    - test              Run test mode
      
Example:
    python3 entrypoint.py blast101 -q SOMEPROTEINSEQUENCE -i sequences.fasta")
""")


parser = instantiate_parser()
args = parser.parse_args()


# Validate required args are set
if args.mode == 'blast101' or args.mode == 'smith_waterman':
    if not args.query:
        args.query = validate_sequence(parser, input("Please enter your protein query sequence: ").strip())
    if not args.input:
        args.input = file_exists(parser, input("Please enter your database file name - this should be a file containing sequences in fasta format: ").strip())
    args.input = fasta_file_validate(parser, args.input)

    if args.mode == 'blast101':
        blast_101_search.blast101_run(args.query, args.input)
    elif args.mode == 'smith_waterman':
        smith_waterman_search.run_sw(args.query, args.input)


if args.mode == 'stats':
    if not args.input:
        args.input = file_exists(parser, input("Please enter the name of the CSV file containing your data: ").strip())
    calc_bit_and_evalues.build_fit(args.input)


