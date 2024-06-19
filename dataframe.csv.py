import pandas as pd

df = pd.read_csv('sample.csv')
df['Age in 5 Years'] = df['Age'] + 5
df.to_csv('modified_sample.csv', index=False)
