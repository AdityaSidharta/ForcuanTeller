import json
import os

from forcuanteller.main.indicators.indicator import load_indicator
from forcuanteller.main.utils.config import config
from forcuanteller.main.utils.paths import transform_dir
from forcuanteller.main.utils.ticker import load_ticker, get_available_tickers


def main(run_id):
    available_tickers = get_available_tickers(run_id)
    indicators_info = config.indicators
    buy_signals = {}
    sell_signals = {}

    for ticker in available_tickers:
        df = load_ticker(ticker, run_id)
        ticker_buy_signals = []
        ticker_sell_signals = []
        for indicator_info in indicators_info:
            indicator = load_indicator(indicator_info)
            buy_signal, sell_signal = indicator.get_signal(df, ticker, run_id)
            if buy_signal is not None:
                ticker_buy_signals.append(buy_signal)
            elif sell_signal is not None:
                ticker_sell_signals.append(sell_signal)

        if ticker_buy_signals:
            buy_signals[ticker] = ticker_buy_signals
        if ticker_sell_signals:
            sell_signals[ticker] = ticker_sell_signals

    reports = {"buy_signals": buy_signals, "sell_signals": sell_signals, "run_id": run_id}
    filename = "report_{}.json".format(run_id)
    filepath = os.path.join(transform_dir, filename)

    with open(filepath, "w+") as f:
        json.dump(reports, f)
