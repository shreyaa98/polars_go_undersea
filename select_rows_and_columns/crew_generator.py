import polars as pl
import numpy as np

np.random.seed(42)
N = 100
HEADSCARF = ['black', 'white', 'pink', 'blue', 'green', 'orange', 'indigo', None] * 6 + ['red']

index = pl.Series("id", np.arange(N))

df = pl.DataFrame(
    {
        "id": np.arange(N),
        "headscarf": np.random.choice(HEADSCARF, size=N),
        "earrings": np.roll(np.random.randint(0, 12, size=N), -1),
        "tattoos": np.random.randint(0, 25, size=N),
    }
)

df.write_csv("bar.csv")
