import library_GP


# %%
# Excercise 1A
try:
    library_GP.logger.info(
        "Starting Exercise 1A: Creating member dictionary"
    )
    # Define the file names for member info and annotations and unpack them
    members_file = "data/33208_members.tsv"
    annotation_file = "data/33208_annotations.tsv"

    member_dict = library_GP.make_member_dict(members_file)

    # Load the annotation data using the annotation_file
    annotation = library_GP.find_annotation(annotation_file)

    # Define the species to include and exclude
    spec_includ1 = "Homo sapiens"
    spec_includ2 = "Pan troglodytes"
    spec_exclud = "Mus musculus"

    total_genes = library_GP.OGs_dict(
        spec_includ1, spec_includ2, spec_exclud, member_dict
    )

    tot_genes_path = "results/Ex_1A-Gene_comparison_in_three_species.txt"
    with open(tot_genes_path, "w", encoding="utf-8") as tot_genes:
        tot_genes.write(
            f"{spec_includ1} and {spec_includ2} share {len(total_genes)} OGs that are missing in {spec_exclud}."
        )
    library_GP.logger.info(
        "Completed Exercise 1A: Successfully created member dictionary from file: %s", members_file
    )
except Exception as e:
    library_GP.logger.error(
        "Error creating member dictionary from file %s: %s", members_file, str(e)
    )


# %%
# Excercise 1B


# Empty lists to store human and chimp protein IDs
human_protIDs = []
chimp_protIDs = []

# Iterate through the total_genes dictionary
try:
    library_GP.logger.info("Starting Exercise 1B: processing of human (and chimp) protein IDs.")
    # Processing human and chimp protein IDs
    for keys, values in total_genes.items():
        # Split the first value (gene list) by ',' to get individual gene IDs
        for item in values[0].split(","):
            # Check if the gene ID belongs to human and append it to the human_protIDs list
            if library_GP.find_taxid(spec_includ1) in item.split(".")[0]:
                human_protIDs.append(item)

            # Check if the gene ID belongs to chimp and append it to the chimp_protIDs list

            # elif library_GP.find_taxid(spec_includ2) in item.split(".")[0]:
            #     chimp_protIDs.append(item)
                
    

    # Define the path for the output file containing human protein IDs
    prot_IDs_path = "results/Ex_1B-Human_protIDs.txt"

    # Open the output file in write mode with utf-8 encoding
    with open(prot_IDs_path, "w", encoding="utf-8") as protein_IDs:
        # Write a header line to the output file
        protein_IDs.write(
            f"############### List of human protein IDs (Total number: {len(human_protIDs)}): ###############\n"
        )
        # Iterate through the human_protIDs list
        for line in human_protIDs:
            # Write each protein ID to a new line in the output file
            protein_IDs.write(f"{line}\n")
        # protein_IDs.write(f"###############List of chimp protein IDs (Total number: {len(chimp_protIDs)}):###############\n")
        # for line in chimp_protIDs:
        # protein_IDs.write(f"{line}\n")
            
    library_GP.logger.info("Completed Exercise 1B: processing human (and chimp) protein IDs.")
except Exception as e:
    library_GP.logger.error(
        "Error in processing human (and chimp) protein IDs: %s", str(e)
    )

# %%
# Excercise 1C #


# Initialize a Counter object to count the occurrences of functional categories
func_counts = library_GP.Counter()

# Iterate through the keys in the total_genes dictionary
try:
    library_GP.logger.info("Starting Exercise 1C: processing of functional categories.")
    for line in total_genes.keys():
        # Update the func_counts Counter object with the functional category of the current gene
        func_counts.update([annotation.get(line, "unknown")])

    # Sort the func_counts dictionary by value in descending order
    sorted_func = dict(
        sorted(func_counts.items(), key=lambda item: item[1], reverse=True)
    )

    # Define the path for the output file containing functional categories
    func_path = "results/Ex_1C-Functional_categories_score.txt"

    library_GP.logger.info("Completed processing functional categories.")

    # Open the output file in write mode with utf-8 encoding
    with open(func_path, "w", encoding="utf-8") as functions:
        # Write a header line to the output file
        functions.write(
            "################## List of functional categories ##################\n"
        )
        functions.write("Func. categories: Number of proteins\n")
        functions.write("\n")
        # Iterate through the sorted_func dictionary
        for function, count in sorted_func.items():
            # If the function is 'S', skip it
            if function == "S":
                pass
            # Otherwise write the function and its count to the output file
            else:
                functions.write(f"{function}: {count}\n")
        functions.write("\n")

        # Write a summary line for the functional category 'S' to the output file
        functions.write(
            f"For the functional category 'S' where the functions are unknown\n"
        )
        functions.write(
            f"Among the {len(total_genes)}, {sorted_func['S']} were poorly discribed.\n"
        )

    library_GP.logger.info("Completd Exercise 1C: processing functional categories.")
except Exception as e:
    library_GP.logger.error("Error in processing functional categories: %s", str(e))


# %%
# Excercise 1D

# Initialize an empty set to store genes that are present in only two species
only_two_species = set()

# Initialize an empty dictionary to store genes that are present in other species
other_species = {}

# Iterate through the key-value pairs in the total_genes dictionary
try:
    library_GP.logger.info(
        "Starting Exercise 1D: processing of genes in only two species and other species."
    )
    for keys, values in total_genes.items():
        # Check if the values[1] (taxonomy string) contains only the taxids of the two specified species
        if (
            values[1]
            .replace(library_GP.find_taxid(spec_includ1), "")
            .replace(library_GP.find_taxid(spec_includ2), "")
            == ","
        ):
            # If so, add the key (gene id) to the only_two_species set
            only_two_species.add(keys)
        else:
            # Otherwise, add the key-value pair to the other_species dictionary
            other_species[keys] = values[1]

    # Define the path for the output file containing genes in other species and genes in only two species
    spec_path = "results/Ex_1D-Query_genes_in_other_species.txt"

    library_GP.logger.info(
        "Completed processing genes in only two species and other species."
    )

    # Open the output file in write mode with utf-8 encoding
    with open(spec_path, "w", encoding="utf-8") as spec:
        # Write a header line to the output file
        spec.write(
            f"#################### List of {len(other_species)} genes in other species ####################\n"
        )

        # Iterate through the key-value pairs in the other_species dictionary
        for keys, values in other_species.items():
            # Write the key and value to the output file
            spec.write(f"{keys}: {values}\n")
        spec.write("\n")
        # Write a header line to the output file
        spec.write(
            f"#################### List of {len(only_two_species)} genes only in {spec_includ1} and {spec_includ2}:#################### \n"
        )
        # Iterate through the genes in the only_two_species set
        for line in only_two_species:
            # Write the gene to the output file
            spec.write(f"{line}\n")
    library_GP.logger.info("Completed Exercise 1D")
except Exception as e:
    library_GP.logger.error(
        "Error in processing genes in only two species and other species: %s", str(e)
    )


# %%
# Excercise 1E


# Create a set of primate species
try:
    library_GP.logger.info(
        "Starting Exercise 1E: processing of primate-specific genes.(Excercise 1E)"
    )
    primates = {
        "Homo sapiens",
        "Tarsius syrichta",
        "Callithrix jacchus",
        "Macaca fascicularis",
        "Papio anubis",
        "Gorilla gorilla",
        "Pan paniscus",
        "Pan troglodytes",
        "Pongo abelii",
        "Saimiri boliviensis",
        "Chlorocebus sabaeus",
        "Rhinopithecus roxellana",
        "Nomascus leucogenys",
        "Otolemur garnettii",
        "Macaca mulatta",
    }

    # Create an empty set for primate IDs
    prim_IDs = set()

    # Create an empty set for primate-specific genes
    only_prim = set()

    # Iterate over each primate species and find the ID for each one
    for item in primates:
        prim_IDs.add(library_GP.find_taxid(item))

    library_GP.logger.info("Found ID's for each species")

    # Iterate over other species and their values
    for keys, values in other_species.items():
        # Remove primate IDs from the values
        for item in prim_IDs:
            values = values.replace(str(item), "")

        # Replace any remaining commas with an empty string
        values = values.replace(",", "")

        # Add the key to the primate-specific genes set if no IDs are found
        if values == "":
            only_prim.add(keys)

    # Combine the primate-specific genes with the `only_two_species` set
    all_prim = only_prim | only_two_species

    prim_path = "results/Ex_1E-Query_genes_in_primates.txt"

    with open(prim_path, "w", encoding="utf-8") as prim:
        prim.write(
            f"#################### List of {len(all_prim)} genes found only in primates: ####################\n"
        )

        for items in all_prim:
            prim.write(items)
            prim.write("\n")

    library_GP.logger.info("Completed Exercise 1E: processing of primate-specific genes.")

except Exception as e:
    library_GP.logger.error(f"Error in Exercise 1E: {str(e)}")


# %%
# Excercise 2

try:
    library_GP.logger.info(
        "Starting Exercise 2: Gene comparison across different species."
    )

    # Find the tax IDs for various species
    human = library_GP.find_taxid("Homo sapiens")
    chicken = library_GP.find_taxid("Gallus gallus")
    fish1 = library_GP.find_taxid("Danio rerio")
    fish2 = library_GP.find_taxid("Takifugu rubripes")
    chimp = library_GP.find_taxid("Pan troglodytes")
    mouse = library_GP.find_taxid("Mus musculus")
    rat = library_GP.find_taxid("Rattus norvegicus")

    # Initialize counters for genes
    genes_counter = 0
    genes_counter2 = 0
    genes_counter3 = 0
    genes_counter4 = 0

    # Iterate over the member dictionary
    for keys, values in member_dict.items():
        # Check if the values contain chicken, and either human or chimpanzee (or both),
        # and either fish1 or fish2 (or both)
        if (
            chicken in values[1]
            and (
                (human in values[1] or chimp in values[1])
                or (human in values[1] and chimp in values[1])
            )
            and (
                (fish1 in values[1] or fish2 in values[1])
                or (fish1 in values[1] and fish2 in values[1])
            )
        ):
            # If so, increment the genes_counter
            genes_counter += 1
            # Check if the values do not contain mouse or rat
            if mouse not in values[1] and rat not in values[1]:
                # If so, increment the genes_counter2
                genes_counter2 += 1
            # Check if the values do not contain mouse
            if mouse not in values[1] and rat in values[1]:
                # If so, increment the genes_counter3
                genes_counter3 += 1
            # Check if the values do not contain rat
            if rat not in values[1] and mouse in values[1]:
                # If so, increment the genes_counter4
                genes_counter4 += 1

    mezo_path = "results/Ex_2-Gene_comparison_in_diff_species.txt"

    # ... existing code ...
    with open(mezo_path, "w", encoding="utf-8") as mezo:
        mezo.write(
            f"#################### Comparison of gene found in differant species: ####################\n"
        )
        mezo.write("\n")
        mezo.write(f"Genes found in primates, chicken, and fish: {genes_counter}\n")
        mezo.write("\n")
        mezo.write(
            f"Genes found in primates, chicken, and fish but not in mouse and rat: {genes_counter2}\n"
        )
        mezo.write("\n")
        mezo.write(
            f"Genes found in primates, chicken, and fish but not in mouse: {genes_counter3}\n"
        )
        mezo.write("\n")
        mezo.write(
            f"Genes found in primates, chicken, and fish but not in rat: {genes_counter4}\n"
        )

    library_GP.logger.info(
        "Completed Exercise 2: Gene comparison results written to file."
    )
except Exception as e:
    library_GP.logger.error(f"Error in Exercise 2: {str(e)}")

# %%
# Excercise 3

try:
    library_GP.logger.info(
        "Starting Exercise 3: Identifying OGs in 99% or more of all animal species."
    )

    # Create an empty set to store all metazoan species
    all_member = set()

    # Iterate over the member dictionary
    for keys, values in member_dict.items():
        # Split the values[1] by commas and add each item to the set
        for item in values[1].split(","):
            all_member.add(item)

    # Calculate the number of all metazoan species
    all_member_count = len(all_member)

    # Create an empty set to store OGs that occur in 99% or more of all animal species
    OGs_99p_animals = set()

    # Iterate over the member dictionary
    for keys, values in member_dict.items():
        # Check if the number of members in values[1] divided by the number of all metazoan species is greater than or equal to 0.99
        if len(values[1].split(",")) / all_member_count >= 0.99:
            # If so, add keys to the OGs_99p_animals set
            OGs_99p_animals.add(keys)

    OGs_in_all_path = "results/Ex_3-Genes_in_all_animals.txt"
    with open(OGs_in_all_path, "w", encoding="utf-8") as OGs_in_all:
        OGs_in_all.write(
            f"#################### Following {len(OGs_99p_animals)} OGs occur in more then 99% of all animal species: ####################\n"
        )
        for items in OGs_99p_animals:
            OGs_in_all.write(items)
            OGs_in_all.write("\n")

    library_GP.logger.info(
        f"Completed Exercise 3. Identified {len(OGs_99p_animals)} OGs in 99% or more of all animal species."
    )
except Exception as e:
    library_GP.logger.error(f"Error in Exercise 3: {str(e)}")
