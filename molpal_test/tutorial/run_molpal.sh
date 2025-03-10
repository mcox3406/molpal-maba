#!/bin/bash
#SBATCH --job-name=molpal_1k
#SBATCH --partition=sched_mit_ccoley
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=12
#SBATCH --time=24:00:00
#SBATCH --mem-per-cpu=4G
#SBATCH --output=job_output.log
#SBATCH --error=job_error.log

cd /pool001/mcox340/molpal-maba/molpal_test/tutorial

source /home/mcox340/miniconda3/etc/profile.d/conda.sh
conda activate molpal

molpal run --config config.yaml
