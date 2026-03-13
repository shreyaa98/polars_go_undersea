### Pandas Version

import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

df = pd.read_csv('C:\\Users\\shrey\\polars_go_to_space\\read_write_data\\panda_sector.csv', index_col=0)
sns.scatterplot(data=df, x='x', y='y', hue='class', size='size')

### Polars Version