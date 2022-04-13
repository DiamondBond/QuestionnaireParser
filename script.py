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

columns = []
UserInfo = ['S','T','U']
ABIS = ['V','W','X','Y','Z','AA','AB','AC','AD','AE','AF','AG','AH']
DERS = ['AI','AJ','AK','AL','AM','AN','AO','AP','AQ','AR','AS','AT','AU','AV','AW','AX','AY','AZ','BA','BR']
AUDIT = ['BS','BT','BU','BV','BW','BX','BY','BZ','CA','CB']


fc = ",".join(columns)

columns_df = pd.read_excel(filename, sheet_name=0, usecols=fc, skiprows=[1])
#.map({1:5, 2:4, 3:3, 4:2, 5:1})
list = columns_df.values.tolist()

# Strip [nan] entries
cleanedList = stripNAN(list)
dictList = eval(cleanedList)

# output columns
jsonString = json.dumps(dictList)
jsonFile = open("userinfo.json", "w")
jsonFile.write(jsonString)
#print("\nList formatted and written to userinfo.json")

# output template
# Participant ID (num) - Gender (text) - Age (num) - Year of study (text) - ABIS (num) - DERS (num) - AUDIT (num)
