import pandas as pd
data = {
    'X': [10, 20, 30],
    'Y': [15, 25, 35],
    'Z': [5, 7, 9]
}

df = pd.DataFrame(data)

cov_matrix = df.cov()
print("Covariance matrix:")
print(cov_matrix)