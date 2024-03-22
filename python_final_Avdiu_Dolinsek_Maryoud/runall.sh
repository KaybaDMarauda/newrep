#!/bin/bash

# Create directories
mkdir -p data results doc temp

mv README.txt doc

# Change to the 'data' directory
cd data

echo "Downloading taxid information..."
# Download taxid information
curl -o e5.taxid_info.tsv http://eggnog5.embl.de/download/eggnog_5.0/e5.taxid_info.tsv
echo "Download completed."

echo "Dowload annotation infromation..."
# Download annotations for tax level 33208
curl -o 33208_annotations.tsv.gz http://eggnog5.embl.de/download/eggnog_5.0/per_tax_level/33208/33208_annotations.tsv.gz
echo "Download completed."

echo "unpacking annotation information..."
gunzip 33208_annotations.tsv.gz
echo "unpacking complete"

echo "Downloading member infromation..."
# Download members for tax level 33208
curl -o 33208_members.tsv.gz http://eggnog5.embl.de/download/eggnog_5.0/per_tax_level/33208/33208_members.tsv.gz
echo "Download completed."

echo "unpacking member information..."
gunzip 33208_members.tsv.gz
echo "unpacking complete"

echo "Downloading functional categories..."
# Download functional categories from Eggnog 4.5
curl -o eggnog4.functional_categories.txt http://eggnog5.embl.de/download/eggnog_4.5/eggnog4.functional_categories.txt
echo "Download completed."


# Return to the parent directory
cd ..

echo "Starting Python File..."
# Run the Python script
python Project_GP.py
#if you dont need the __pycache__ folder also possible to use python -B
echo "Program End."

# Move __pycache__ to temp
mv __pycache__ temp


