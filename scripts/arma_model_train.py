import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.regime_switching.markov_regression import MarkovRegression

def fit_ms_arima(df, n_states=2, ar_order=1):
    """
    Fits a Markov-Switching AR model to Brent oil prices.

    Parameters:
    - df: DataFrame with 'Price' column
    - n_states: Number of hidden regimes (market conditions)
    - ar_order: Order of the autoregressive component

    Returns:
    - results: Fitted Markov-Switching model
    """
    model = MarkovRegression(df["Price"], k_regimes=n_states, trend="c", order=ar_order, switching_variance=True)
    results = model.fit()
    
    print(results.summary())
    
    # Plot the probabilities of each regime
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df["Price"], label="Brent Oil Price", color="blue", alpha=0.7)
    for i in range(n_states):
        plt.fill_between(df.index, df["Price"].min(), df["Price"].max(),
                         where=results.smoothed_marginal_probabilities[i] > 0.5, alpha=0.3,
                         label=f"Regime {i+1}")
    plt.xlabel("Year")
    plt.ylabel("Price (USD)")
    plt.title("Brent Oil Prices with Markov-Switching Regimes")
    plt.legend()
    plt.show()

    return results

