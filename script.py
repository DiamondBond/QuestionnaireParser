#!/usr/bin/env python3
import sys
import json
import pandas as pd
# WS = pd.read_excel('in.xlsx')
# WS_np = np.array(WS)

# print(WS_np)



def stripNAN(s):
    i = str(s).replace(", [nan, nan]", "")
    return i


filename = sys.argv[1]
columns = []
dc = sys.argv[2]
nc = sys.argv[3]
columns.append(dc)
columns.append(nc)


fc = ",".join(columns)

columns_df = pd.read_excel(filename, sheet_name=0, usecols=fc)
list = columns_df.values.tolist()

# Strip [nan] entries
cleanedList = stripNAN(list)
dictList = eval(cleanedList)

# output columns
# jsonString = json.dumps(dictList)
# jsonFile = open("masterlist.json", "w")
# jsonFile.write(jsonString)
# print("\nList formatted and written to masterlist.json")
