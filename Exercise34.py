import pandas as pd
import scipy.stats as stats
import scipy

group_ET = pd.Series([4.5, 3.9, 7.1, 4.3, 6.9, 8.2, 7.6])
group_ER = pd.Series([4.9, 4.7, 7.8, 4.8, 7.5, 7.8, 8.1])

print("Pearson correlation:" ,scipy.stats.pearsonr(group_ET, group_ER))
print("Spearman correlation:" ,scipy.stats.spearmanr(group_ET, group_ER))

# Rank the two groups. (For same values use half. E.g. if there are two values with the smallest value, then rank them both 1.5.)
group_ET_rank = group_ET.rank()
group_ER_rank = group_ER.rank()

#pearson correlation on the ranks
print("Pearson correlation on the ranks:" ,scipy.stats.pearsonr(group_ET_rank, group_ER_rank))
