import polars as pl
import numpy as np

np.random.seed(42)
N = 500
EARS = ['black', 'white', 'pink', 'blue', 'green', 'red', 'neon', 'orange', 'chartreuse', 'indigo', 'peachpuff', 'piercing', None]

index = pl.Series("id", np.arange(N))

df = pl.DataFrame(
    {
        "id": np.arange(N),
        "blue_spots": np.random.randint(1, 20, size=N),
        "black_spots": np.random.randint(1, 20, size=N),
        "ears": np.random.choice(EARS, size=N)
    }
)

df.write_csv("crew.csv")


