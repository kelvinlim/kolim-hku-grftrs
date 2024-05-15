# kolim_hku_grftrs

1. On mriserver.psychiatry.hku.hk. In ~/team directory is where the fmriprep output was located.

2. Used the collect_dtseries.py program to collect all the *rest*dtseries*nii* files and place them into a single directory raw_dtseries.

3. The raw_dtseries were transfered into a folder: /scratch.global/kolim-hku-grftrs by using the rsync command called from msi.

    ```
    cd /scratch.global/kolim-hku-grftrs

    rsync -rav klim@mriserver.psychiatry.hku.hk:/mrihome/klim/team/raw_dtseries .

    ```
4. Time courses were then extracted using wb_extract with the process.sh script and stored in the data directory

    ```
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
    ```

5. Perform CDA  See example code used in kolim-cda-melbourne. 

    https://github.umn.edu/kolim/cda_tools2

    To run the cda

    ```
    # cd to the directory where the data directory is located
    # The config.yaml file and the data directory defined in 
    # the config.yaml are located in the directory
    cd /scratch.global/kolim-hku-grftrs

    # activate venv
    source /home/limko/public/Venvs/cdatools2/bin/activate

    # export path
    export PATH=/home/limko/public/cda_tools2:$PATH

    # make sure that there is a logs directory for slurm
    mkdir -p logs

    # determine the number of total cases, 
    run_causal2.py --list
    # got 172 cases

    # use sbatch to setup the jobs, assume total cases from above is 172
    # -J allows use to dynamically name the job
    sbatch --array=1-172 -J grftrs slurm_causal.sh

    # Check on queue
    squeue --user kolim

    # to cancel a job id
    scancel <jobid>


    ```

## s3cmd

```
# create bucket
s3cmd mb s3://kolim-hku-grftrs

# sync local directory to a bucket
cd /scratch.global/kolim-hku-grftrs
s3cmd sync . s3://kolim-hku-grftrs

```

# kolim-hku-grftrs
