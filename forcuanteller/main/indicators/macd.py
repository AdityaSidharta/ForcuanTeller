import os
import uuid
import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as fplt
import numpy as np
import seaborn as sns
from ta.trend import MACD

from matplotlib.dates import WeekdayLocator
from forcuanteller.main.indicators.base import Indicator
from forcuanteller.main.utils.paths import transform_dir


class MACDInd(Indicator):
    def get_name(self):
        return "MACD"

    def get_param(self):
        return "Window Slow : {}, Window Fast : {}, Window Sign : {}".format(
            self.indicator["window_slow"], self.indicator["window_fast"], self.indicator["window_sign"]
        )

    def get_signal(self, input_df, ticker, run_id):
        df = input_df.copy()

        indicator_macd = MACD(
            close=df["Close"],
            window_slow=self.indicator["window_slow"],
            window_fast=self.indicator["window_fast"],
            window_sign=self.indicator["window_sign"],
            fillna=self.indicator["fillna"],
        )

        # Add Bollinger Bands features
        df["macd"] = indicator_macd.macd()
        df["macd_signal"] = indicator_macd.macd_signal()
        df["macd_diff"] = indicator_macd.macd_diff()

        previous_row = df.iloc[-2]
        row = df.iloc[-1]

        if (row.macd_diff.item() < 0) and (previous_row.macd_diff.item() > 0):
            sell_signal = {
                "ticker": ticker,
                "datetime": row.Date,
                "indicator": self.name,
                "param": self.param,
                "reason": "MACD Downward Crossover",
                "image": self.draw_image(df, ticker, run_id),
            }
        else:
            sell_signal = None

        if (previous_row.macd_diff.item() < 0) and (row.macd_diff.item() > 0):
            buy_signal = {
                "ticker": ticker,
                "datetime": row.Date,
                "indicator": self.name,
                "param": self.param,
                "reason": "MACD Upward Crossover",
                "image": self.draw_image(df, ticker, run_id),
            }
        else:
            buy_signal = None

        return buy_signal, sell_signal

    def draw_image(self, input_df, ticker, run_id):
        sns.set()
        df = input_df.copy()
        df['Date'] = pd.to_datetime(df['Date'])
        df.index = pd.DatetimeIndex(df['Date'])

        colormat = np.where(df["macd_diff"] > 0, "g", "r")
        fig, ax = plt.subplots(figsize=(20, 8), nrows=2, sharex=True)

        fplt.plot(df, type="candle", style="charles", ax=ax[0])
        sns.barplot(x=df.index.astype(str), y=df["macd_diff"], data=df, ax=ax[1], palette=colormat)
        sns.lineplot(x=df.index.astype(str), y=df["macd"], data=df, color="blue", ax=ax[1], label="macd")
        sns.lineplot(
            x=df.index.astype(str), y=df["macd_signal"], data=df, color="orange", ax=ax[1], label="macd_signal"
        )

        ax[0].set_ylabel("")
        ax[0].set_xlabel("")

        ax[1].set_ylabel("")
        ax[1].set_xlabel("")

        ax[1].legend()

        ax[1].xaxis.set_major_locator(WeekdayLocator())

        fig.autofmt_xdate()

        filename = "{}_{}_{}.png".format(ticker, self.name, run_id)
        filepath = os.path.join(transform_dir, filename)
        plt.savefig(filepath)
        return filepath
