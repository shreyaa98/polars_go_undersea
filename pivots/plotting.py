import seaborn as sns
import polars as pl
from matplotlib import pyplot as plt


df = pl.from_pandas(sns.load_dataset("penguins"))


piv = df.drop_nulls("sex").pivot(
    values="bill_length_mm",
    index="island",
    columns="sex",
    aggregate_function="count"
)

piv_pd = piv.to_pandas().set_index("island")
piv_pd = piv_pd.reindex(["Biscoe", "Dream", "Torgersen"])
ax = piv_pd[["Female", "Male"]].plot.bar()


plt.xlabel("Island")
plt.ylabel("Count")
plt.xticks(rotation=45)
ax.legend(title="sex")
plt.tight_layout()
plt.savefig("penguin_barplot.png", dpi=300)

