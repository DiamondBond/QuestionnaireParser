#!/usr/bin/env python3

# QuestionnaireParser v1.0
# Parser designed for qualtrics questionnaires.
#
# Dependencies:
# $ pip install pandas
#
# Running:
# $ python3 main.py
#
# Input file: in.xlsx
# Output file: out.xlsx

import pandas as pd

# ====================
# INPUT
# ====================

filename = "in.xlsx"

# Columns
columns = ['S','T','U','V','W','X','Y','Z','AA','AB','AC','AD','AE','AF','AG','AH','AI','AJ','AK','AL','AM','AN','AO','AP','AQ','AR','AS','AT','AU','AV','AW','AX','AY','AZ','BA','BB','BC','BD','BE','BF','BG','BH','BI','BJ','BK','BL','BM','BN','BO','BP','BQ','BR','BS','BT','BU','BV','BW','BX','BY','BZ','CA','CB']
fc = ",".join(columns)

# Initialize DataFrame
df = pd.read_excel(filename, sheet_name=0, usecols=fc, skiprows=[1]).fillna(0)

# ====================
# ABIS
# ====================

# Reverse score [ABIS]
rs_abis =['Q6_1','Q6_2','Q6_4','Q7_1','Q7_3','Q8_3','Q8_4','Q8_5']
for i in range(len(rs_abis)):
    df[rs_abis[i]] = df[rs_abis[i]].map({1.0:4.0, 2.0:3.0, 3.0:2.0, 4.0:1.0})

# Calculate Average for [ABIS]
df['attention'] = df[['Q6_1', 'Q6_4', 'Q7_3', 'Q8_1', 'Q8_4']].mean(axis=1)
df['motor'] = df[['Q6_3','Q7_2','Q7_4','Q8_2']].mean(axis=1)
df['non-planning'] = df[['Q6_2','Q7_1','Q8_3','Q8_5']].mean(axis=1)
df['abis-total'] = df[['attention', 'motor','non-planning']].mean(axis=1)
df['abis-total'] = round(df['abis-total'],2)

# ====================
# DERS
# ====================

# Reverse score [DERS]
rs_ders = ['Q9_1','Q9_2','Q9_6','Q9_7','Q10_1','Q10_3','Q11_3','Q11_6','Q12_1','Q12_3','Q13_6']
for i in range(len(rs_ders)):
    df[rs_ders[i]] = df[rs_ders[i]].map({1.0:5.0, 2.0:4.0, 3.0:3.0, 4.0:2.0, 5.0:1.0})

# Calculate Sum for [DERS]
df['ders'] = df[['Q9_1','Q9_2','Q9_3','Q9_4','Q9_5','Q9_6','Q9_7','Q10_1','Q10_2','Q10_3','Q10_4','Q10_5','Q10_6','Q10_7','Q11_1','Q11_2','Q11_3','Q11_4','Q11_5','Q11_6','Q11_7','Q12_1','Q12_2','Q12_3','Q12_4','Q12_5','Q12_6','Q12_7','Q13_1','Q13_2','Q13_3','Q13_4','Q13_5','Q13_6','Q13_7','Q13_8']].sum(axis=1)

# ====================
# AUDIT
# ====================

# Reverse score [AUDIT]
rs_audit = ['Q22', 'Q23']
for i in range(len(rs_audit)):
    df[rs_audit[i]] = df[rs_audit[i]].map({1.0:0.0, 2.0:2.0, 3.0:4.0})

# Calculate fn(x - 1) for [AUDIT]
sub1 = ['Q14', 'Q15', 'Q16', 'Q17', 'Q18', 'Q19', 'Q20', 'Q21']
for i in range(len(sub1)):
    df[sub1[i]] = (df[sub1[i]] - 1).apply(lambda x : x if x > 0 else 0)

# Calculate Sum for [AUDIT]
df['audit'] = df[['Q14','Q15','Q16','Q17','Q18','Q19','Q20','Q21','Q22','Q23']].sum(axis=1)

# ====================
# OUPUT
# ====================

df.to_excel(r'out.xlsx')
