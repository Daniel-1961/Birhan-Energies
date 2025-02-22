# scripts/change_point_detection.py

import ruptures as rpt
import matplotlib.pyplot as plt

def detect_change_points(data, penalty=20, model="rbf"):
    price_array = data['Price'].values
    algo = rpt.Pelt(model=model).fit(price_array)
    change_points = algo.predict(pen=penalty)
    return change_points

def plot_change_points(data, change_points):
    plt.figure(figsize=(14, 7))
    plt.plot(data.index, data['Price'], label='Brent Oil Price')
    for cp in change_points[:-1]:
        plt.axvline(x=data.index[cp], color='red', linestyle='--', label='Change Point' if cp == change_points[0] else "")
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.title('Brent Oil Prices with Detected Change Points')
    plt.legend()
    plt.show()
