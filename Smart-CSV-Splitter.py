import pandas as pd
import numpy as np
import os
import re
# User Input
inputfile = input('What is the directory of your input file eg... D:/FILES/ALS_DRINKING-ALGAE_WATER_201807101206.xlsx: ')
seperator = input('what is the delimiter for cells output? eg: | or , : ' )
columntosplit = input('what is the heading for the column you want to split the data by?: ')
# Read File
df = pd.read_excel(inputfile, index=False)
df_column = df[columntosplit]
# The number of unique items in the column you chose
unique_values = df_column.unique()
numberofunique = len(unique_values)
print ('number of files to generate:', numberofunique)
# Create Files
for i in range(numberofunique):
    bools = df[columntosplit] == unique_values[i]
    df_temp = df[bools]
    filetag = re.sub('[^A-Za-z0-9]+', '-', unique_values[i])
    filename, file_extension = os.path.splitext(inputfile)
    filename = filename + "_" + filetag + ".csv"
    df_temp.to_csv(filename, sep=seperator, index=False)
