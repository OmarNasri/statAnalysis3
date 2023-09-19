import pandas as pd
import scipy.stats as stats
import scipy

group_DT = pd.Series([5.6, 3.1, 8.7, 4.5, 6.7, 4.5])
group_DR = pd.Series([6.1, 5.8, 8.5, 5.3, 7.2, 5.1])

group_ET = pd.Series([4.5, 3.9, 7.1, 4.3, 6.9, 8.2, 7.6])
group_ER = pd.Series([4.9, 4.7, 7.8, 4.8, 7.5, 7.8, 8.1])

#test all for normality
print(stats.shapiro(group_DT))
print(stats.shapiro(group_DR))
print(stats.shapiro(group_ET))
print(stats.shapiro(group_ER))

#Data inside the groups are related
#DT,DR,ET are normal, ER is not

print("DT and DR t-test:" ,scipy.stats.ttest_rel(group_DT, group_DR))

print("ET and ER Wilcoxon signed-rank test:" ,scipy.stats.wilcoxon(group_ET, group_ER))

print("DT and ET t-test:" ,scipy.stats.ttest_ind(group_DT, group_ET))

print("DR and ER Mann-Whitney U test:" ,scipy.stats.mannwhitneyu(group_DR, group_ER))