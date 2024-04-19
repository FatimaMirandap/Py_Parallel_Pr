# Pi Approximation Scripts

This repository contains three different Python scripts that approximate the value of π (pi) using the method of numerical integration. The scripts represent different approaches: sequential calculation, multiprocessing, and distributed computing with MPI.

## Scripts

- `numerical_pi.py`: Implements the approximation of π without parallelization.
- `multiprocess_numerical_pi.py`: Uses Python's multiprocessing module to parallelize the computation.
- `mpi4py_numerical_pi.py`: Employs the `mpi4py` library to distribute the computation across multiple processes.

## Requirements

- Python 3.x
- NumPy (for `mpi4py_numerical_pi.py`)
- mpi4py (for `mpi4py_numerical_pi.py`)
- A system with MPI installed (for `mpi4py_numerical_pi.py`)

## Installation

To clone the repository, run:

git clone https://github.com/<your-username>/pi-approximation-scripts.git
# For the sequential approach
python numerical_pi.py

# For the multiprocessing approach
python multiprocess_numerical_pi.py

# For the distributed approach with MPI
mpirun -np <number_of_processes> python mpi4py_numerical_pi.py

# Profiling
Each script contains code for profiling its execution. Profiling results will be saved in text files within the same directory after running the scripts.

# Contributing
Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.
Please ensure to update tests as appropriate.

To use this README, you would need to:
1. Replace the `<FatimaMirandaP>` placeholder with your GitHub username.
2. Add any additional instructions or descriptions as necessary, depending on the specifics of your scripts or environment.
3. Save this text in a file named `README.md` in the root directory of your repository.

This README provides a basic structure that includes an overview of the repository, instructions for cloning and running the scripts, and sections for contributions and licensing. You can customize and expand each section to provide more detailed information as required.
