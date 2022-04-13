#!/usr/bin/env python3
import sys
import json
import pandas as pd
import re
import numpy as np
from openpyxl import Workbook
from openpyxl import load_workbook

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

all_columns = ['V','W','X','Y','Z','AA','AB','AC','AD','AE','AF','AG','AH','AI','AJ','AK','AL','AM','AN','AO','AP','AQ','AR','AS','AT','AU','AV','AW','AX','AY','AZ','BA','BR','BS','BT','BU','BV','BW','BX','BY','BZ','CA','CB']
abis_columns = ['V','W','X','Y','Z','AA','AB','AC','AD','AE','AF','AG','AH']
reverse_columns = ['V','W','Y','Z','AB','AF','AG','AH']
columns = abis_columns

fc = ",".join(columns)

columns_df = pd.read_excel(filename, sheet_name=0, usecols=fc, skiprows=[1]).fillna(0)
#columns_df = columns_df['V','W','Y','Z','AB','AF','AG','AH'].map({1.0:4.0, 2.0:3.0, 3.0:2.0, 4.0:1.0 })
#output = columns_df['V'].map({1:4, 2:3, 3:2, 4:1})
list = columns_df.values.tolist()

# Strip [nan] entries
cleanedList = stripNAN(list)
#print(cleanedList)
dictList = eval(cleanedList)
# print(dictList)

# convert_dict = {abis_columns: int}
# dataframe = columns_df.astype(convert_dict)

# example = dictList
# for key in example:
#     s = example[key]
#     example[key] = [int(item) for item in s.split(',')]
# print(example)

# output columns
# jsonString = json.dumps(dictList)
# jsonFile = open("out.json", "w")
# jsonFile.write(jsonString)
# #print("\nList formatted and written to userinfo.json")



# file_path = "out.json"

# with open(file_path, 'r') as j:
#      contents = json.loads(j.read())
#      print(contents)

# # WRITING DATA OUT
# book = load_workbook(filename="output.xlsx")
# sheet = book.active

# # Data to write:
# output = [
#     [
#         data["V"],
#     ]
# ]

# for info in output:
#     # print(info)
#     sheet.append(info)

# # Save excel file
# book.save(filename="output.xlsx")
