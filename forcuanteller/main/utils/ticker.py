import os

import pandas as pd

from forcuanteller.main.utils.paths import load_dir


def load_ticker(ticker, run_id):
    filename = "{}_{}.csv".format(ticker, run_id)
    filepath = os.path.join(load_dir, filename)
    return pd.read_csv(filepath)


def get_available_tickers(input_run_id):
    available_tickers = []
    filenames = os.listdir(load_dir)
    for filename in filenames:
        try:
            ticker, run_id = filename.split('_')
            run_id, _ = run_id.split('.')
            if run_id == input_run_id:
                available_tickers.append(ticker)
        except ValueError:
            pass
    return available_tickers