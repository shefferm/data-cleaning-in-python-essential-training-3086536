# %%
import pandas as pd

df = pd.read_csv('rides.csv')
df

# %%

# - Missing values are not allowed
null_mask = df.isnull().any(axis=1)
df[null_mask]

# %%

# - A plate must be a combination of at least 3 upper case letters or digits
plate_mask = ~df['plate'].str.match(r'^[0-9A-Z]{3,}', na=False)
df[plate_mask]

# %%

# - Distance much be bigger than 0
distance_mask = df['distance'] <= 0
df[distance_mask]


# %%
# Find out all the rows that have bad values
# - Missing values are not allowed
# - A plate must be a combination of at least 3 upper case letters or digits
# - Distance much be bigger than 0
mask = null_mask | plate_mask | distance_mask
df[mask]
# %%
