import pandas as pd
import numpy as np
WS = pd.read_excel('a.xlsx')
WS_np = np.array(WS)

print(WS_np)
