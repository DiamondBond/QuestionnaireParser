import pandas as pd

# Filename definition
filename = "in.xlsx" #filename = sys.argv[1]

# Columns definition
columns = ['V','W','X','Y','Z','AA','AB','AC','AD','AE','AF','AG','AH','AI','AJ','AK','AL','AM','AN','AO','AP','AQ','AR','AS','AT','AU','AV','AW','AX','AY','AZ','BA','BR','BS','BT','BU','BV','BW','BX','BY','BZ','CA','CB']
#abis_columns = ['V','W','X','Y','Z','AA','AB','AC','AD','AE','AF','AG','AH']
#reverse_columns = ['V','W','Y','Z','AB','AF','AG','AH']
fc = ",".join(columns)

# Setup DataFrame
df = pd.read_excel(filename, sheet_name=0, usecols=fc, skiprows=[1]).fillna(0) #nans hack

# Reverse score [TODO: FIXME: THIS IS =HORRIBLY= HARDCODED]
#print(df.head)
df['Q6_1'] = df['Q6_1'].map({1.0:4.0, 2.0:3.0, 3.0:2.0, 4.0:1.0})
df['Q6_2'] = df['Q6_2'].map({1.0:4.0, 2.0:3.0, 3.0:2.0, 4.0:1.0})
df['Q6_4'] = df['Q6_4'].map({1.0:4.0, 2.0:3.0, 3.0:2.0, 4.0:1.0})
df['Q7_1'] = df['Q7_1'].map({1.0:4.0, 2.0:3.0, 3.0:2.0, 4.0:1.0})
df['Q7_3'] = df['Q7_3'].map({1.0:4.0, 2.0:3.0, 3.0:2.0, 4.0:1.0})
df['Q8_3'] = df['Q8_3'].map({1.0:4.0, 2.0:3.0, 3.0:2.0, 4.0:1.0})
df['Q8_4'] = df['Q8_4'].map({1.0:4.0, 2.0:3.0, 3.0:2.0, 4.0:1.0})
df['Q8_5'] = df['Q8_5'].map({1.0:4.0, 2.0:3.0, 3.0:2.0, 4.0:1.0})
#print(df.head)
#print(df.mean(axis=1))

# Average V - AH
#df['avg'] = df.mean(axis=1)
df['avg'] = df[['Q6_1', 'Q6_2','Q6_3','Q6_4','Q7_1','Q7_2','Q7_3','Q7_4','Q8_1','Q8_2','Q8_3','Q8_4','Q8_5']].mean(axis=1) #[HERESY]
#print(df['avg'])

print(df.head)
