# %%
import pandas as pd

df = pd.read_csv('workshops.csv')
df

# %%
null_mask = df.isna().any(axis=1)
df['Year'].fillna(method='ffill', inplace=True)
df['Month'].fillna(method='ffill', inplace=True)
df
non_null_rows = df[~null_mask]

# %%

non_null_rows

# %%
"""
Fix the data frame. At the end, row should have the following columns:
- start: pd.Timestemap
- end: pd.Timestamp
- name: str
- topic: str (python or go)
- earnings: np.float64
"""