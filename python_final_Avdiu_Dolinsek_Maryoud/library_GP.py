# %%
"""Library for working with eggNOG files (eggNOG v5.0)"""

import gzip
import logging
from collections import defaultdict, Counter
from typing import Iterable
import sys
import csv
import os


csv.field_size_limit(sys.maxsize)
member_dict = {}

log_file_name = "logger_GP.log"
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(message)s")

file_handler = logging.FileHandler("doc/logger_GP.log")  # for log file
file_handler.setLevel(logging.ERROR)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter) 

stream_handler = logging.StreamHandler()  # for output in Console
stream_handler.setFormatter(formatter)  # Optional: Setting formatter for stream handler

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def make_member_dict(file_name):
    """Loads information in of colomn 2 in the keys and makes a list for the values with column 5 and 6 of the file"""

    path = "data/" + file_name.rsplit(".", 1)[0]
    with open(
        file_name, "rt", newline="", encoding="utf-8"
    ) as tsvfile:  # Open the TSV file for reading
        reader = csv.reader(
            tsvfile, delimiter="\t"
        )  # Create a CSV reader object to read the TSV file. The delimiter '\t' indicates that the file is tab-separated

        # Iterate over each row in the TSV file
        for row in reader:
            # For each row, use the value in the second column as a key in the dictionary.
            # Assign a list containing values from the fifth and sixth columns as the value for this key.
            member_dict[row[1]] = [row[4], row[5]]
    # Return the populated dictionary

    return member_dict



def find_taxid(sciname: str, file_name="e5.taxid_info.tsv", directory="data"):
    """Looks up the right taxid in the e5.taxid_info.tsv file"""

    # Define path to the file
    path = f"{directory}/{file_name}"

    # Open the file and handle FileNotFoundError exceptions
    try:
        with open(path, "r", newline="", encoding="utf-8") as tsvfile:
            reader = csv.reader(tsvfile, delimiter="\t")

            # Iterate through the rows in the TSV file
            for row in reader:
                # If the sciname matches, return the corresponding taxid
                if row[1] == sciname:
                    return str(row[0])

    except FileNotFoundError:
        logger.error(f"Error: {path} does not exist.")
        return None
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        return None


def OGs_dict(species1: str, species2: str, species3: str, file_path=None):
    """Find OGs present in species1 and species2 but not in species3."""
    com_OGs = {}  # create an empty dictionary to store the data

    # If file_path is not provided, use the global variable member_dict
    if file_path is None:
        file_path = member_dict

    # get taxids for the given species
    taxid1 = find_taxid(species1)
    taxid2 = find_taxid(species2)
    taxid3 = find_taxid(species3)

    # iterate over file_path (either the provided dictionary or the global member_dict)
    for keys, values in file_path.items():
        # check if taxids of species1 and species2 are present and taxid of species3 is not present
        if taxid1 in values[1] and taxid2 in values[1] and taxid3 not in values[1]:
            com_OGs[keys] = values  # store the key-value pair in the result dictionary

    # return the result dictionary
    return com_OGs


def find_annotation(annotation_file: str):  # Function to find annotations
    path = "data/" + annotation_file.rsplit(".", 1)[0]

    try:
        with open(
            annotation_file, "r", newline="", encoding="utf-8"
        ) as tsvfile:  # Open annotation file
            reader = csv.reader(tsvfile, delimiter="\t")  # Create a CSV reader

            ortho_dict = {}  # Initialize an empty dictionary

            for row in reader:  # Iterate through each row
                ortho_dict[row[1]] = row[2]  # Add gene and ortholog to dictionary

        return ortho_dict  # Return the dictionary

    except FileNotFoundError:
        logger.error(f"Error: {path} does not exist.")
        return None
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        return None
