import pandas as pd
import scipy.stats as stats
import scipy

A = pd.Series([34, 23, 51, 47, 34])
B = pd.Series([48, 27, 33, 45, 41, 35])
C = pd.Series([34, 53, 54, 28, 52, 29])

#test all for normality
print(stats.shapiro(A))
print(stats.shapiro(B))
print(stats.shapiro(C))

#A and B are normal but not paired
print("A and B t-test:" ,scipy.stats.ttest_ind(A, B))

#B is normal but C is not. They can also be potentially paired
print("B and C Mann-Whitney U test:" ,scipy.stats.mannwhitneyu(B, C))
#Wilcoxon test in case data is paired
print("B and C Wilcoxon signed-rank test:" ,scipy.stats.wilcoxon(B, C))
      
#A is normal but C is not. They are not paired
print("A and C Mann-Whitney U test:" ,scipy.stats.mannwhitneyu(A, C))