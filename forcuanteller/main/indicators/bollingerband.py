import os
import uuid

import matplotlib.pyplot as plt
import seaborn as sns
from ta.volatility import BollingerBands

from forcuanteller.main.indicators.base import Indicator
from forcuanteller.main.utils.paths import transform_dir


class BollingerBandInd(Indicator):
    def get_name(self):
        return "BollingerBand"

    def get_param(self):
        return "Window : {}, Standard Deviation : {}".format(self.indicator["window"], self.indicator["window_dev"])

    def get_signal(self, input_df, ticker, run_id):
        df = input_df.copy()

        indicator_bb = BollingerBands(
            close=df["Close"],
            window=self.indicator["window"],
            window_dev=self.indicator["window_dev"],
            fillna=self.indicator["fillna"],
        )

        # Add Bollinger Bands features
        df["bb_bbm"] = indicator_bb.bollinger_mavg()
        df["bb_bbh"] = indicator_bb.bollinger_hband()
        df["bb_bbl"] = indicator_bb.bollinger_lband()

        df["bb_bbhi"] = indicator_bb.bollinger_hband_indicator()
        df["bb_bbli"] = indicator_bb.bollinger_lband_indicator()
        df["bb_bbp"] = indicator_bb.bollinger_pband()

        row = df.iloc[-1]

        if row.bb_bbhi.item():
            sell_signal = {
                "ticker": ticker,
                "datetime": row.index.item(),
                "indicator": self.name,
                "param": self.param,
                "reason": "High BollingerBand percentage - currently at {:2f}%".format(int(row.bb_bbp.item() * 100.0)),
                "image": self.draw_image(df, ticker, run_id),
            }
        else:
            sell_signal = None

        if row.bb_bbli.item():
            buy_signal = {
                "ticker": ticker,
                "datetime": row.index.item(),
                "indicator": self.name,
                "param": self.param,
                "reason": "Low BollingerBand percentage - currently at {:2f}%".format(int(row.bb_bbp.item() * 100.0)),
                "image": self.draw_image(df, ticker, run_id),
            }
        else:
            buy_signal = None

        return buy_signal, sell_signal

    def draw_image(self, input_df, ticker, run_id):
        sns.set()
        df = input_df.copy()

        fig, ax = plt.subplots(figsize=(20, 5))

        sns.lineplot(x=df.index, y=df["Close"], data=df, color="blue", linewidth=3)
        sns.lineplot(x=df.index, y=df["bb_bbm"], data=df, color="orange", linewidth=1)
        sns.lineplot(x=df.index, y=df["bb_bbh"], data=df, color="green", linewidth=1)
        sns.lineplot(x=df.index, y=df["bb_bbl"], data=df, color="red", linewidth=1)

        ax.set_ylabel("")
        ax.set_xlabel("")

        filename = "{}_{}_{}_{}.png".format(ticker, self.name, run_id, str(uuid.uuid4())[:6])
        filepath = os.path.join(transform_dir, filename)
        plt.savefig(filepath)
        return filepath
