#! /usr/bin/env python

import pandas as pd
import networkx as nx 
import glob 
import os

directory = 'output_gfci'

# get the matching files
fileList = glob.glob(os.path.join(directory,'*semopy.csv'))

# create list to hold results
results = []

for file in fileList:
    print(file)
    # read in the file into a df
    df = pd.read_csv(file)
    
    info = {}  # dict to hold file results
    # create a directed graph
    DG = nx.DiGraph() 
    # loop through all edges in file
    for index, row in df.iterrows():
        #print(row.keys())
        DG.add_edge(row['rval'], row['lval'], weight=row['Estimate'])
        pass
    
    # compute graphmetrics
    # Degree Centrality
    deg_centrality = nx.degree_centrality(DG)

    # In-Degree Centrality
    in_deg_centrality = nx.in_degree_centrality(DG)

    # Out-Degree Centrality
    out_deg_centrality = nx.out_degree_centrality(DG)

    # Closeness Centrality
    close_centrality = nx.closeness_centrality(DG)

    # Betweenness Centrality
    btwn_centrality = nx.betweenness_centrality(DG)
   
    # load the info
    info['id'] = file
    info['deg_centrality'] = deg_centrality
    info['in_deg_centrality'] = in_deg_centrality
    info ['out_deg_centrality'] = out_deg_centrality
    info ['close_centrality'] = close_centrality
    info ['btwn_centrality'] = btwn_centrality
    
    # append to list
    results.append(info)
    
    pass
# create a new dataframe for results 
df_results = pd.DataFrame(results)
# write out to file
df_results.to_csv('gm_results.csv', index=False)
pass
