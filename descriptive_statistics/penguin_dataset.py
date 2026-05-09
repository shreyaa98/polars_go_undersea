import seaborn as sns


df = sns.load_dataset("penguins")
df.to_csv("penguins.csv", index=False)
print("penguins.csv downloaded successfully")