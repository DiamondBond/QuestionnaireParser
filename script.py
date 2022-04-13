#!/usr/bin/env python3
import sys
import json
import pandas as pd
import re
import numpy as np

# [NOTES]
# column A to R useless
# column S to column U - age , gender & year (1, 2, or 3)

# column V to AH = impulsivity [ABIS]
# column AI to BR = difficulties in emotional regulation [DERS]
# column BS to CB = ordered questions [AUDIT]


def stripNAN(s):
    i = str(s).replace(", [nan, nan]", "")
    return i

def listToString(s):
    # initialize an empty string
    str1 = ""
    # traverse in the string
    for ele in s:
        str1 += ele
    # return string
    return str1


def stripContainer(s):
    a = str(s).replace("'", "")
    b = str(a).replace("[", "")
    c = str(b).replace("]", "")
    return c

#filename = sys.argv[1]
filename = "in.xlsx"

columns = ['V','W','X','Y','Z','AA','AB','AC','AD','AE','AF','AG','AH','AI','AJ','AK','AL','AM','AN','AO','AP','AQ','AR','AS','AT','AU','AV','AW','AX','AY','AZ','BA','BR','BS','BT','BU','BV','BW','BX','BY','BZ','CA','CB']

fc = ",".join(columns)

columns_df = pd.read_excel(filename, sheet_name=0, usecols=fc, skiprows=[1]).fillna(0)
#.map({1:5, 2:4, 3:3, 4:2, 5:1})
list = columns_df.values.tolist()

# Strip [nan] entries
cleanedList = stripNAN(list)
#print(cleanedList)
#cleanedList = 
dictList = eval(cleanedList)

# output columns
jsonString = json.dumps(dictList)
jsonFile = open("masterlist.json", "w")
jsonFile.write(jsonString)
#print("\nList formatted and written to userinfo.json")

# output template
# Participant ID (num) - Gender (text) - Age (num) - Year of study (text) - ABIS (num) - DERS (num) - AUDIT (num)
#ABIS = ['V','W','X','Y','Z','AA','AB','AC','AD','AE','AF','AG','AH']

# Deserializing JSON to dict
# with open("masterlist.json") as json_file:
#     data = json.load(json_file)
#     for i in range(len(data)):
#         our_list = data[i]
#         chunked_list = list()
#         chunk_size = 3
#         for i in range(0, len(our_list)):
#             chunked_list.append(our_list[i:i+chunk_size])
#             print(chunked_list)


