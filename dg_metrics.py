#! /usr/bin/env python

"""
Code for directed graph analysis of brain data

"""


class DGMetrics:
    
    def __init__(self):
        pass
    
    def read_label_file(self, fpath:str):
        """read labels from file
        
        Sample file: https://github.com/yetianmed/subcortex/blob/master/Group-Parcellation/3T/Cortex-Subcortex/Schaefer2018_400Parcels_7Networks_order_Tian_Subcortex_S4_label.txt
        
        Args:
            fpath (str): filepath to the label file
        """
        
        pass
    

file = "https://github.com/yetianmed/subcortex/blob/master/Group-Parcellation/3T/Cortex-Subcortex/Schaefer2018_400Parcels_7Networks_order_Tian_Subcortex_S4_label.txt"

dg = DGMetrics()
dg.read_label_file(file)

