

# 1        2         3        4          5        6         7        8         9         10          1
 
# alpha     CL        CD       CDp       Cm      Top Xtr   Bot Xtr   Cpmin    Chinge     XCp         Re
# ------- -------- --------- --------- -------- -------   -------  --------  --------- ---------   ---------














import glob
from io import StringIO
import numpy as np
import pandas as pd

RE0 = 100000;
del_RE = 10000;

files = glob.glob("*.txt")
data_len = 0
data_array = np.zeros([0,11])
temp_array = np.zeros([1,11])
files_count = len(files)
for fl in range(0,files_count - 1):
    file  = open(files[fl],"r")
    last_data_len = data_len
    lines = file.readlines()

    file.close()
    data  = lines[11:]
    data_len = len(data)
    


    for i in range(0,len(data)-2):
        df = np.array(pd.read_csv(StringIO(data[i]), sep='  ',header =None,index_col=None, usecols=None, squeeze=False, prefix=None))
        for j in range(0,9):
            #data_array[i + last_data_len][j] = df[0][j] 
            temp_array[0][j] = df[0][j]
        temp_array[0][10] = RE0 + fl*del_RE;
        data_array = np.append(data_array,temp_array,axis = 0)
        
        
pd.DataFrame(data_array).to_csv("data_analysis.csv", header=None, index=None)
