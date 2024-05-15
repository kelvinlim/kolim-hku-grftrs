#! /usr/bin/env python

"""
Code for directed graph analysis of brain data

"""


class DGMetrics:
    
    def __init__(self):
        pass
    
    def read_label_file(self, fpath:str, replace=False):
        """read labels from file
        
        index 0 - even index lines contain the labels
        
        Sample file: https://github.com/yetianmed/subcortex/blob/master/Group-Parcellation/3T/Cortex-Subcortex/Schaefer2018_400Parcels_7Networks_order_Tian_Subcortex_S4_label.txt
        
        Args:
            fpath (str): filepath to the label file
            replace (dict): dictionary describing replacement string
        """
        
        labels = []
        with open(fpath) as fp:
            lines = fp.readlines()
        index = 0
        for line in lines:
            if index%2 == 0:
                if replace:
                    for key, value in replace.items():
                        line = line.replace(key, value)
                    pass
                labels.append(line.rstrip('\n'))
            index += 1
                 
        return labels
    

file = "Schaefer2018_400Parcels_17Networks_order_Tian_Subcortex_S4_label.txt"
dg = DGMetrics()
replace = {'17Networks': 'N17'}
labels = dg.read_label_file(file, replace=replace)

pass

