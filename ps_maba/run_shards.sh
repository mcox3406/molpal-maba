#!/bin/bash
#SBATCH --job-name=vina_dock
#SBATCH --partition=sched_mit_ccoley
#SBATCH --nodelist=node1238
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --time=06:00:00
#SBATCH --mem-per-cpu=4G
#SBATCH --output=slurm_out/job_output_%A_%a.log
#SBATCH --error=slurm_out/job_error_%A_%a.log
#SBATCH --array=1-12

cd /pool001/mcox340/molpal-maba/ps_maba

source /home/mcox340/miniconda3/etc/profile.d/conda.sh
conda activate molpal

/home/mcox340/miniconda3/envs/molpal/bin/python run_ps_vina_shard.py ${SLURM_ARRAY_TASK_ID}

