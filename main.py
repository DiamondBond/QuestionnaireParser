import pandas as pd

# Filename definition
filename = "in.xlsx" #filename = sys.argv[1]

# Columns definition
columns = ['V','W','X','Y','Z','AA','AB','AC','AD','AE','AF','AG','AH','AI','AJ','AK','AL','AM','AN','AO','AP','AQ','AR','AS','AT','AU','AV','AW','AX','AY','AZ','BA','BB','BC','BD','BE','BF','BG','BH','BI','BJ','BK','BL','BM','BN','BO','BP','BQ','BR','BS','BT','BU','BV','BW','BX','BY','BZ','CA','CB']
#abis_columns = ['V','W','X','Y','Z','AA','AB','AC','AD','AE','AF','AG','AH']
#reverse_columns = ['V','W','Y','Z','AB','AF','AG','AH']
fc = ",".join(columns)

# Setup DataFrame
df = pd.read_excel(filename, sheet_name=0, usecols=fc, skiprows=[1]).fillna(0) #nans hack

# Reverse score [TODO: FIXME: THIS IS =HORRIBLY= HARDCODED]
df['Q6_1'] = df['Q6_1'].map({1.0:4.0, 2.0:3.0, 3.0:2.0, 4.0:1.0})
df['Q6_2'] = df['Q6_2'].map({1.0:4.0, 2.0:3.0, 3.0:2.0, 4.0:1.0})
df['Q6_4'] = df['Q6_4'].map({1.0:4.0, 2.0:3.0, 3.0:2.0, 4.0:1.0})
df['Q7_1'] = df['Q7_1'].map({1.0:4.0, 2.0:3.0, 3.0:2.0, 4.0:1.0})
df['Q7_3'] = df['Q7_3'].map({1.0:4.0, 2.0:3.0, 3.0:2.0, 4.0:1.0})
df['Q8_3'] = df['Q8_3'].map({1.0:4.0, 2.0:3.0, 3.0:2.0, 4.0:1.0})
df['Q8_4'] = df['Q8_4'].map({1.0:4.0, 2.0:3.0, 3.0:2.0, 4.0:1.0})
df['Q8_5'] = df['Q8_5'].map({1.0:4.0, 2.0:3.0, 3.0:2.0, 4.0:1.0})

# AVG(V - AH)
df['attention'] = df[['Q6_1', 'Q6_4', 'Q7_3', 'Q8_1', 'Q8_4']].mean(axis=1)
df['motor'] = df[['Q6_3','Q7_2','Q7_4','Q8_2']].mean(axis=1)
df['non-planning'] = df[['Q6_2','Q7_1','Q8_3','Q8_5']].mean(axis=1)
df['abis-total'] = df[['attention', 'motor','non-planning']].mean(axis=1)
df['abis-total'] = round(df['abis-total'],2)

# Reverse score [TODO: FIXME: THIS IS =HORRIBLY= HARDCODED]
df['Q9_1'] = df['Q9_1'].map({1.0:5.0, 2.0:4.0, 3.0:3.0, 4.0:2.0, 5.0:1.0})
df['Q9_2'] = df['Q9_2'].map({1.0:5.0, 2.0:4.0, 3.0:3.0, 4.0:2.0, 5.0:1.0})
df['Q9_6'] = df['Q9_6'].map({1.0:5.0, 2.0:4.0, 3.0:3.0, 4.0:2.0, 5.0:1.0})
df['Q9_7'] = df['Q9_7'].map({1.0:5.0, 2.0:4.0, 3.0:3.0, 4.0:2.0, 5.0:1.0})
df['Q10_1'] = df['Q10_1'].map({1.0:5.0, 2.0:4.0, 3.0:3.0, 4.0:2.0, 5.0:1.0})
df['Q10_3'] = df['Q10_3'].map({1.0:5.0, 2.0:4.0, 3.0:3.0, 4.0:2.0, 5.0:1.0})
df['Q11_3'] = df['Q11_3'].map({1.0:5.0, 2.0:4.0, 3.0:3.0, 4.0:2.0, 5.0:1.0})
df['Q11_6'] = df['Q11_6'].map({1.0:5.0, 2.0:4.0, 3.0:3.0, 4.0:2.0, 5.0:1.0})
df['Q12_1'] = df['Q12_1'].map({1.0:5.0, 2.0:4.0, 3.0:3.0, 4.0:2.0, 5.0:1.0})
df['Q12_3'] = df['Q12_3'].map({1.0:5.0, 2.0:4.0, 3.0:3.0, 4.0:2.0, 5.0:1.0})
df['Q13_6'] = df['Q13_6'].map({1.0:5.0, 2.0:4.0, 3.0:3.0, 4.0:2.0, 5.0:1.0})

# SUM(AI - BR)
df['ders'] = df[['Q9_1','Q9_2','Q9_3','Q9_4','Q9_5','Q9_6','Q9_7','Q10_1','Q10_2','Q10_3','Q10_4','Q10_5','Q10_6','Q10_7','Q11_1','Q11_2','Q11_3','Q11_4','Q11_5','Q11_6','Q11_7','Q12_1','Q12_2','Q12_3','Q12_4','Q12_5','Q12_6','Q12_7','Q13_1','Q13_2','Q13_3','Q13_4','Q13_5','Q13_6','Q13_7','Q13_8']].sum(axis=1)

# Reverse score [TODO: FIXME: THIS IS =HORRIBLY= HARDCODED]
df['Q22'] = df['Q22'].map({1.0:0.0, 2.0:2.0, 3.0:4.0})
df['Q23'] = df['Q23'].map({1.0:0.0, 2.0:2.0, 3.0:4.0})

# SUB(-1)
df['Q14'] = (df['Q14'] - 1).apply(lambda x : x if x > 0 else 0)
df['Q15'] = (df['Q15'] - 1).apply(lambda x : x if x > 0 else 0)
df['Q16'] = (df['Q16'] - 1).apply(lambda x : x if x > 0 else 0)
df['Q17'] = (df['Q17'] - 1).apply(lambda x : x if x > 0 else 0)
df['Q18'] = (df['Q18'] - 1).apply(lambda x : x if x > 0 else 0)
df['Q19'] = (df['Q19'] - 1).apply(lambda x : x if x > 0 else 0)
df['Q20'] = (df['Q20'] - 1).apply(lambda x : x if x > 0 else 0)
df['Q21'] = (df['Q21'] - 1).apply(lambda x : x if x > 0 else 0)

# SUM(BS to CB)
df['audit'] = df[['Q14','Q15','Q16','Q17','Q18','Q19','Q20','Q21','Q22','Q23']].sum(axis=1)

# Output
print(df.head)

df.to_excel(r'out.xlsx')
