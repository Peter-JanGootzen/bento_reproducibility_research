# Bento and the Art of Repeated Research

This repository contains all scripts, results and crashlogs from the [paper](https://github.com/Peter-JanGootzen/bento_reproducibility_research/blob/master/Bento_and_the_Art_of_Repeated_Research.pdf).
The crashlogs are numbered, and their descriptions can be found in the paper.

## Reproduction
To reproduce the results, clone the [Bento repository](https://github.com/smiller123/bento) (with it's submodules!) into the root of this repository and execute the 'run' script with the `DISK` environment variable as follows:
```bash
DISK=/dev/nvme0n1 ./run
```

The 'results.ipynb' Jupyter Notebook is used to process the results and create plots and tables that can be found in the paper.
