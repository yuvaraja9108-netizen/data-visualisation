import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# paths
data_path = Path(__file__).resolve().parents[1] / "data" / "amazon.csv"
out_dir = Path(__file__).resolve().parents[1] / "output"
out_dir.mkdir(parents=True, exist_ok=True)

# load & prep
df = pd.read_csv(data_path, parse_dates=["product_name"])
df = df.sort_values("product_name")

# plot
plt.figure(figsize=(10, 5))
plt.plot(df["product_name"], df["actual_price"], marker="o")
plt.title("Amazon")
plt.xlabel("Product_name")
plt.ylabel("Actual_price")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()

# save + show
png_path = out_dir / "amazon.png"
plt.savefig(png_path, dpi=200)
plt.show()
print(f"Saved figure to: {png_path}")
