
'''
Author: David Jensen
Date Created: 29 Mar 2020
Date Modified: 29 Mar 2020
User Inputs: path to table (tb1), and path to masking shapefile (mask_string)

Purpose: Batch process merging multiple satellite images and masking them within a region of focus. For use in QGIS python console. SEE README FOR REQUIRED INPUTS.



'''


#import packages
import os
import pandas as pd
import processing

#create paths
mask_string = 'USER INPUT REQUIRED'
tb1 = pd.read_csv('USER INPUT REQUIRED')
counter = tb1['id']

for a in counter:
    tb2 = tb1.loc[tb1['id'] == a]
    input_list0 = (tb2['path'])
    input_list = list(input_list0)
    tb2 = tb2.reset_index()
    merge_out = tb2['merge_out'][0]
    mask_out = tb2['mask_out'][0]
    processing.run("gdal:merge", { 'DATA_TYPE' : 5, 'EXTRA' : '', 'INPUT' : input_list, 'NODATA_INPUT' : 0, 'NODATA_OUTPUT' : None, 'OPTIONS' : '', 'OUTPUT' : merge_out, 'PCT' : False, 'SEPARATE' : False })
    processing.run("gdal:cliprasterbymasklayer", { 'ALPHA_BAND' : False, 'CROP_TO_CUTLINE' : True, 'DATA_TYPE' : 0, 
    'EXTRA' : '', 'INPUT' : merge_out, 'KEEP_RESOLUTION' : False, 'MASK' : mask_string, 'MULTITHREADING' : False, 
    'NODATA' : None, 'OPTIONS' : '', 'OUTPUT' : mask_out, 'SET_RESOLUTION' : False, 'SOURCE_CRS' : None, 'TARGET_CRS' : None, 
    'X_RESOLUTION' : None, 'Y_RESOLUTION' : None })
    os.remove(merge_out)
