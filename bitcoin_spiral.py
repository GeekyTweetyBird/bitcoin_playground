import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

class BitcoinLogarithmicSpiral:
    DAYS_PER_HALVING = 210000 / 144
    DEGREES_PER_DAY = 360 / DAYS_PER_HALVING

    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self.bitcoin_history = self.get_bitcoin_history()

    def get_bitcoin_history(self):
        return yf.download('BTC-USD', start=self.start_date, end=self.end_date)

    @staticmethod
    def calculate_theta(degrees_per_day, data_length):
        return np.linspace(0, degrees_per_day * data_length, data_length) * np.pi / 180

    def plot_chart(self):
        r = np.log10(self.bitcoin_history['Close'].values)
        theta = self.calculate_theta(self.DEGREES_PER_DAY, len(self.bitcoin_history))
        
        plt.figure(figsize=(10, 10))
        ax = plt.subplot(111, polar=True)
        ax.plot(theta, r)
        ax.set_title("Bitcoin Price Logarithmic Spiral")
        ax.set_rlabel_position(0)
        ax.set_yticklabels([])
        ax.set_xticklabels([])
        ax.grid(True)

        self.set_y_axis(ax, r)
        
        plt.show()

    @staticmethod
    def set_y_axis(ax, r):
        y_ticks = np.arange(np.floor(np.min(r)), np.ceil(np.max(r)) + 1)
        ax.set_yticks(y_ticks)
        ax.set_yticklabels([f'${10 ** y_tick:.0f}' for y_tick in y_ticks])

if __name__ == "__main__":
    start_date = datetime(2010, 7, 17)
    end_date = datetime.now()
    bitcoin_chart = BitcoinLogarithmicSpiral(start_date, end_date)
    bitcoin_chart.plot_chart()
