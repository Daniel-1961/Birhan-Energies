import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.regime_switching.markov_regression import MarkovRegression

def model_arima(df, n_states_list=[2, 3, 4], ar_order=1):
    """
    Fits multiple Markov-Switching AR models to Brent oil prices and selects the best one.

    Parameters:
    - df: DataFrame with 'Price' column
    - n_states_list: List of different numbers of regimes to test
    - ar_order: Order of the autoregressive component

    Returns:
    - best_model: The selected Markov-Switching model
    """
    best_model = None
    best_aic = float("inf")

    for n_states in n_states_list:
        print(f"\n🔹 Fitting MS-AR({ar_order}) model with {n_states} regimes...")
        try:
            model = MarkovRegression(df["Price"], k_regimes=n_states, trend="c", order=ar_order, switching_variance=True)
            results = model.fit()
            print(f"✅ Model with {n_states} regimes: AIC = {results.aic}")

            if results.aic < best_aic:
                best_aic = results.aic
                best_model = results

        except Exception as e:
            print(f"❌ Model with {n_states} regimes failed: {e}")

    print("\n🏆 Best Model Selected:")
    print(best_model.summary())

    # Plot regime probabilities
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df["Price"], label="Brent Oil Price", color="blue", alpha=0.7)
    
    for i in range(best_model.k_regimes):
        plt.fill_between(df.index, df["Price"].min(), df["Price"].max(),
                         where=best_model.smoothed_marginal_probabilities[i] > 0.5, alpha=0.3,
                         label=f"Regime {i+1}")
    
    plt.xlabel("Year")
    plt.ylabel("Price (USD)")
    plt.title("Brent Oil Prices with Markov-Switching Regimes")
    plt.legend()
    plt.show()

    return best_model


