import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.random.random((1000)), columns = ['values'])
df2 = pd.DataFrame(np.random.random((1000)), columns = ['values'])

df1['band1'] = pd.qcut(df1['values'], 5, duplicates = 'drop')
temp_df = df1[['band1', 'values']].groupby('band1')['values'].mean().sort_index().reset_index()
print(temp_df)


def assign_cat(x, cat_df):
    #this method assigns categorical related values to a pandas series
    idx_bool = [x in interval for interval in cat_df['band1']]
    if sum(idx_bool) > 0:
        idx = idx_bool.index(True)
        return idx, cat_df['values'].loc[idx]
    else:
        #print(x)
        return np.nan, np.nan
    

df2[['band1', 'band2']] = df2['values'].apply(assign_cat, cat_df = temp_df).apply(pd.Series)


