import numpy as np
import pandas as pd
observed = np.array([
    [4, 3],
    [3, 4]
])
row_sums = observed.sum(axis=1)
col_sums = observed.sum(axis=0)
total = observed.sum()
expected = np.outer(row_sums, col_sums) / total
chi_square_stat = ((observed - expected) ** 2 / expected).sum()
dof = (observed.shape[0] - 1) * (observed.shape[1] - 1)
print(f"Chi-square statistic (manual):",chi_square_stat)
print(f"Degrees of freedom: ",dof)