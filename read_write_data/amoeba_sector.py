import polars as pl
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

df = pl.read_csv(r"C:\Users\shrey\Polars_Go_Undersea\read_write_data\amoeba_sector.csv")

# Extract coordinates
x = df["x"].cast(pl.Float64).to_numpy()
y = df["y"].cast(pl.Float64).to_numpy()

# KDE density estimation
xy = np.vstack([x, y])
kde = gaussian_kde(xy)

# Create grid
xmin, xmax = x.min(), x.max()
ymin, ymax = y.min(), y.max()

xx, yy = np.meshgrid(
    np.linspace(xmin, xmax, 300),
    np.linspace(ymin, ymax, 300)
)

# Evaluate density
grid_coords = np.vstack([xx.ravel(), yy.ravel()])
density = kde(grid_coords).reshape(xx.shape)

# Create figure
plt.figure(figsize=(10, 8))

# Filled contours
plt.contourf( xx, yy, density, levels=10, cmap="magma", alpha=0.65 )

# Transparent contour lines
plt.contour(xx, yy, density, levels=10, colors="white", linewidths=0.8, alpha=0.65)

# Raw sector points
plt.scatter( x, y, s=8, color="cyan", alpha=0.85)

plt.xlabel("X Coordinate")
plt.ylabel("Y Coordinate")
plt.title("Sector Coordinate Density Map")
# plt.show()

plt.savefig(
    "C://Users//shrey//Polars_Go_Undersea//read_write_data//sector_coordinate_density_map.jpg",
    dpi=300,
    bbox_inches="tight"
)