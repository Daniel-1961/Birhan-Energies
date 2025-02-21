import matplotlib.pyplot as plt

def plot_prices(df):
    """Plots oil prices over time."""
    plt.figure(figsize=(12,6))
    plt.plot(df.index, df['Price'], label="Brent Oil Price", color="blue")
    plt.xlabel("Year")
    plt.ylabel("Price (USD)")
    plt.title("Brent Oil Prices Over Time")
    plt.legend()
    plt.show()


