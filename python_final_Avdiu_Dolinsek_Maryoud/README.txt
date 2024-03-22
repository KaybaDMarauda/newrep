# Final project: A man or a mouse? Studying metazoan genes in different lineages. 
## Group members: Omar Maryoud, Besard Avdiu, Jan Dolin�ek (all M.BDSC.B.23)

## Description

This project includes a pipeline that uses a shell script (`run.sh`) to prepare the environment and data for a Python script (`Project_GP.py`). The Python script utilizes a library (`library_GP.py`) to process the data.

The `runall.sh` script creates necessary directories, downloads and unpacks data from the Eggnog database, and then runs the Python script for further processing.

`Project_GP.py` is the main Python script that extracts human genes from the Eggnog database and compares them to homologues from chimpanzee, mouse, rat, chicken, zebrafish, and takifugu. It also identifies homologues common to primates and animals. It uses functions defined in `library_GP.py` to perform its tasks.

`library_GP.py` is a Python library that contains a collection of functions used by `Project_GP.py`. This library encapsulates the core logic for data processing, making the main script cleaner and easier to maintain. It handles logging, looks up species in the Eggnog database, searches for homologues in their genomes, and retrieves gene annotations.

## Installation

1. Clone this repository to your local machine.
2. Ensure you have `bash`, `curl`, `gunzip`, and `python` installed on your system.

## Usage

To run the pipeline, navigate to the project directory and execute the following command in your terminal:

$ bash run.sh

This will create the directories `data`, `results`, `doc`, and `temp`. It will then download several data files from the Eggnog database into the `data` directory and unpack them. After the data is prepared, it will run the `Project_GP.py` Python script.

The `Project_GP.py` script uses the `library_GP.py` library to process the data. The results of the script are logged in `results.log`, which is then moved to the `doc` directory. Temporary files and caches are moved to the `temp` directory.

## Findings

In this project, we learned how to handle relatively simple databases, extract specific data, and compare resulting datasets. We also gained insights into project and code documentation, logging, code style, and code readability. The project taught us about group work and collaboration in collaborative projects.
Clearly, contributors proposed different solutions resulting in the same findings. In general, we decided for solutions with best time performance, even though that sometimes sacrificed memory efficiency.
More specifically, we identified 1073 genes shared between human and chimpanzee that have no homologue in mouse. Furthermore, we could identify protein IDs of those genes, bin them into functional categories, identify their homologues in other animals, and identify 167 homologues specific to primates. 
When we compared genes present in selected vertebrates, we found 9861 genes shared between selected primates, birds, and fish, 108 of those were lost in mice and rats, 63 were lost in mice but not in rats, and 138 were lost in rats but not in mice. 
Finally, we identified 694 orthologous groups that are shared between most animals.     

## Contributions

This project is the result of the collaborative efforts of Omar Maryoud, Besard Avdiu, and Jan Dolin�ek. Each contributor wrote their own version of the code independently, but also handled some minor specific tasks. The results were then compared to ensure correctness, and the best performing code was then chosen for this project.

The code itself was written by the contributors without AI assistance. The comments and this README were generated using a generative AI as an assistant in documenting the project (see Exercise sheet 8, 04.11.2023).


























