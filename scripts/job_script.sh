#!/bin/bash -l
#SBATCH --account=lp_h_ds_students
#SBATCH --cluster=wice
#SBATCH --job-name=bloom_benchmark
#SBATCH --time=02:00:00
#SBATCH --mem=8GB
#SBATCH --output=results/benchmark_%j.log

module load Miniconda3
source activate bloom_filter

python scripts/download_words.py
python scripts/benchmark.py