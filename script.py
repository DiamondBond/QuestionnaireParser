#!/usr/bin/env python3
import sys
import json
import pandas as pd

# [NOTES]
# column A to R useless
# column S to column U - age , gender & year (1, 2, or 3)

# column V to AH = impulsivity [ABIS]
# column AI to BR = difficulties in emotional regulation [DERS]
# column BS to CB = ordered questions [AUDIT]


def stripNAN(s):
    i = str(s).replace(", [nan, nan]", "")
    return i

#filename = sys.argv[1]
filename = "in.xlsx"
columns = []
columns.append('S') # Age
columns.append('T') # Gender
columns.append('U') # Year


fc = ",".join(columns)

columns_df = pd.read_excel(filename, sheet_name=0, usecols=fc)
list = columns_df.values.tolist()

# Strip [nan] entries
cleanedList = stripNAN(list)
dictList = eval(cleanedList)

# output columns
jsonString = json.dumps(dictList)
jsonFile = open("masterlist.json", "w")
jsonFile.write(jsonString)
print("\nList formatted and written to masterlist.json")
