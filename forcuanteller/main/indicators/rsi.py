import os
import uuid
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.dates import WeekdayLocator
from ta.momentum import RSIIndicator
import mplfinance as fplt

from forcuanteller.main.indicators.base import Indicator
from forcuanteller.main.utils.paths import transform_dir


class RSIInd(Indicator):
    def get_name(self):
        return "RSI"

    def get_param(self):
        return "Window : {}, Low : {}, High : {}".format(
            self.indicator["window"], self.indicator["low"], self.indicator["high"]
        )

    def get_signal(self, input_df, ticker, run_id):
        df = input_df.copy()

        indicator_rsi = RSIIndicator(
            close=df["Close"],
            window=self.indicator["window"],
            fillna=self.indicator["fillna"],
        )

        # Add Bollinger Bands features
        df["rsi"] = indicator_rsi.rsi()

        previous_row = df.iloc[-2]
        row = df.iloc[-1]

        if row.rsi.item() > self.indicator["high"]:
            sell_signal = {
                "ticker": ticker,
                "datetime": row.Date,
                "indicator": self.name,
                "param": self.param,
                "reason": "High RSI Value - currently at {:2f}%".format(int(row.rsi.item())),
                "image": self.draw_image(df, ticker, run_id),
            }
        elif (row.rsi.item() < self.indicator["high"]) and (previous_row.rsi.item() > self.indicator["high"]):
            sell_signal = {
                "ticker": ticker,
                "datetime": row.Date,
                "indicator": self.name,
                "param": self.param,
                "reason": "RSI Crossover High - previous at {:2f}& and currently at {:2f}%".format(
                    int(previous_row.rsi.item()), int(row.rsi.item())
                ),
                "image": self.draw_image(df, ticker, run_id),
            }
        else:
            sell_signal = None

        if row.rsi.item() < self.indicator["low"]:
            buy_signal = {
                "ticker": ticker,
                "datetime": row.Date,
                "indicator": self.name,
                "param": self.param,
                "reason": "Low RSI Value - currently at {:2f}%".format(int(row.rsi.item())),
                "image": self.draw_image(df, ticker, run_id),
            }
        elif (row.rsi.item() > self.indicator["low"]) and (previous_row.rsi.item() < self.indicator["low"]):
            buy_signal = {
                "ticker": ticker,
                "datetime": row.Date,
                "indicator": self.name,
                "param": self.param,
                "reason": "RSI Crossover Low - previous at {:2f}& and currently at {:2f}%".format(
                    int(previous_row.rsi.item()), int(row.rsi.item())
                ),
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

        fig, ax = plt.subplots(figsize=(20, 8), nrows=2, sharex=True)

        fplt.plot(df, type="candle", style="charles", ax=ax[0])
        sns.lineplot(x=df.index.astype(str), y=df["rsi"], data=df, ax=ax[1], palette="blue")

        ax[1].axhline(self.indicator["high"], ls="--", linewidth=0.5, color="green", alpha=0.5)
        ax[1].axhline(self.indicator["low"], ls="--", linewidth=0.5, color="red", alpha=0.5)

        ax[0].set_ylabel("")
        ax[0].set_xlabel("")

        ax[1].set_ylabel("")
        ax[1].set_xlabel("")

        ax[1].set_ylim(bottom=0, top=100)
        ax[1].xaxis.set_major_locator(WeekdayLocator())

        fig.autofmt_xdate()

        filename = "{}_{}_{}.png".format(ticker, self.name, run_id)
        filepath = os.path.join(transform_dir, filename)
        plt.savefig(filepath)
        return filepath
