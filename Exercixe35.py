import pandas as pd
import scipy.stats as stats
import scipy

df = pd.read_csv("../Statistical Data Analysis 3/simulated_data_2_5.csv")

#Check all data rows for normality
print(stats.shapiro(df["F"]))
print(stats.shapiro(df["G"]))
print(stats.shapiro(df["H"]))
print(stats.shapiro(df["I"]))


#F, G, H are normal, I is not

#Perform pearson correlation on F and G
print("Pearson correlation on F and G:" ,scipy.stats.pearsonr(df["F"], df["G"]))

#perform pearson correlation on F and H
print("Pearson correlation on F and H:" ,scipy.stats.pearsonr(df["F"], df["H"]))

#perform spearman correlation on F and I
print("Spearman correlation on F and I:" ,scipy.stats.spearmanr(df["F"], df["I"]))