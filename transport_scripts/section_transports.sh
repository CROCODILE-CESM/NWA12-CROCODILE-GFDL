#!/bin/bash
#PBS -N sec_transports
#PBS -A NCGD0011
#PBS -l select=1:ncpus=1:mem=80GB
#PBS -l walltime=02:00:00
#PBS -q casper
#PBS -j oe

source ~/.bashrc
module load conda
conda activate mom6-tools

python section_transports.py diag_config.yml section_transports.yml -nw 12
