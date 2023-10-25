import pandas as pd
import numpy as np
df = pd.read_csv('coeff_dataa.csv')
type = df['type']  # Replace 'ColumnName' with the actual column name
const = df['const']
lin1 = df['linear_1']
lin2 = df['linear_2']
lin3 = df['linear_3']
L = [[l1, l2, l3] for l1 in lin1 for l2 in lin2 for l3 in lin3]
L_2d = np.reshape(L, (11, 11))

print(L_2d)