#!/bin/bash
#SBATCH --job-name=molpal_1k_maba
#SBATCH --partition=sched_mit_ccoley
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=12
#SBATCH --time=48:00:00
#SBATCH --mem-per-cpu=4G
#SBATCH --output=slurm/out.log
#SBATCH --error=slurm/err.log

cd /nobackup1/mcox340/molpal-maba/molpal_maba

source /home/mcox340/miniconda3/etc/profile.d/conda.sh
conda activate molpal-env

molpal run --config configs/config.yaml
