#!/bin/bash
#SBATCH --job-name=vina_dock_full_100k
#SBATCH --partition=sched_mit_ccoley
#SBATCH --nodelist=node1236
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=16
#SBATCH --time=96:00:00
#SBATCH --mem=64G         
#SBATCH --output=slurm_100k/out.log
#SBATCH --error=slurm_100k/err.log


cd /nobackup1/mcox340/molpal-maba/ps_maba

source /home/mcox340/miniconda3/etc/profile.d/conda.sh
conda activate molpal-env

/home/mcox340/miniconda3/envs/molpal-env/bin/python ps_vina.py
