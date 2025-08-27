import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# paths
data_path = Path(__file__).resolve().parents[1] / "data" / "amazon.csv"
out_dir = Path(__file__).resolve().parents[1] / "output"
out_dir.mkdir(parents=True, exist_ok=True)

# load & prep
df = pd.read_csv(data_path)
df = df.sort_values("product_name")  # sort for cleaner bars

# plot - column chart (bar)
plt.figure(figsize=(10, 5))
plt.bar(df["product_name"], df["actual_price"], color="skyblue", edgecolor="black")

plt.title("Amazon")
plt.xlabel("Product Name")
plt.ylabel("Actual Price")
plt.xticks(rotation=45, ha="right")  # rotate labels for readability
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()

# save + show
png_path = out_dir / "amazon_bar.png"
plt.savefig(png_path, dpi=200)
plt.show()
print(f"Saved column chart to: {png_path}")
