#! /bin/bash

module load workbench/1.5.0

# add wb_extract to PATH
export PATH=/home/limko/kolim/Projects/wb_extract:$PATH
export CIFTI_parcs=/home/limko/public/CIFTI_parcs

# setup python environment
source /home/limko/public/Venvs/cdaema/bin/activate

# run the wb_extract command
wb_extract.py \
  --dlabel ${CIFTI_parcs}/Schaefer2018_400Parcels_17Networks_order_Tian_Subcortex_S4.dlabel.nii \
  --dtpath raw_dtseries

