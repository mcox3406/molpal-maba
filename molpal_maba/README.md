The repo on the HPC has many more files (with variations/experiments/larger libraries/etc.), but this shows how to run a basic MolPAL calculation in an HPC environment. The key is in loading the appropriate conda environment in the SLURM submission script before running MolPAL. I run the submission script with
```bash
sbatch run_molpal.sh
```
