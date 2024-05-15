#! /usr/bin/env python


import glob
import os
import pandas as pd
import shutil

src_dir = "GRFTRS_process/derivatives/fmriprep" #"fmriprep_VS"
dest_dir = "raw_dtseries"

os.makedirs(dest_dir, exist_ok=True)

# get the list of files
stub = "*rest*dtseries*nii" 
#filelist = glob.glob(os.path.join(src_dir,"**", stub), recursive=True)
path = f"{src_dir}/**/{stub}"
filelist = glob.glob(path, recursive=True)

# files_info structure
files_info = []

# get the basename
basename_list = []
for fp in filelist:
    info = {}
    info['raw'] = fp
    info['base'] = os.path.basename(fp)
    info['sub'] = info['base'].split("_")[0].split("-")[1]
    info['ses'] = info['base'].split("_")[1].split("-")[1]
    info['task'] = info['base'].split("_")[2].split("-")[1]

    tmpignore, info['ext'] = os.path.splitext(info['base'])
    
    
    # append info to files_info only for nii
    if info['ext'] == '.nii':
        files_info.append(info)


# write out data to csv
df = pd.DataFrame(files_info) # first create a dataframe
df.to_csv("dtseries.csv", header=True, index=False)
df.to_excel("dtseries.xlsx", header=True, index=False)


for file in files_info:
    
    # copy file to despath
    
    srcpath = file['raw']
    despath = os.path.join(dest_dir, file['base'])    
    
    shutil.copy(srcpath, despath)
    print(f"copied {despath}")
        
pass
