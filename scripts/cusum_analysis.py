# cusum_analysis.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def calculate_cusum(df):
    """Calculate the CUSUM of the price deviations from the mean."""
    mean_price = df['Price'].mean()
    cusum = np.cumsum(df['Price'] - mean_price)
    return cusum

def plot_cusum(df, cusum):
    """Plot the original prices and CUSUM values."""
    plt.figure(figsize=(14, 7))
    plt.plot(df.index, cusum, label='CUSUM')
    plt.axhline(y=0, color='r', linestyle='--')
    plt.xlabel('Date')
    plt.ylabel('CUSUM Value')
    plt.title('CUSUM Analysis')
    plt.legend()
    plt.show()
