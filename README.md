# Satellite_Imagery_Merge_Mask
Batch process merging multiple satellite images and masking them within a geographic region of focus.

##


Input table is expected to have four columns and be in '.csv' format. Column 1 must contain paths to the satellite imagery, and be titled'path'. Column 2 must contain an id number (e.g. 1, 2, 3). Satellite imagery sharing an id number will be merged together, and then masked within the shapefile. Column 2 must be titled 'id'. Column 3 must contain a directory path to deposit the merged output (titled 'merge_out'), and Column 4 must contain a directory to deposit the masked output (titled 'mask_out'). I wrote this script assuming the user will want both merged and masked outputs, but this script can be edited to only have the masked product as the final result.
