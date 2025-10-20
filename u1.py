import pandas as pd
data = {
    'X': [3, 4, 8, 10],
    'Y': [15, 25, 35, 45]
}
df = pd.DataFrame(data)
pearson_corr = df['X'].corr(df['Y'])
print("Pearson correlation coefficient (pandas): ",pearson_corr)