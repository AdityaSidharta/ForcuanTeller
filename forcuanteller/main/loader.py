import datetime
import os

import yfinance as yf

from forcuanteller.main.utils.config import config
from forcuanteller.main.utils.logger import logger
from forcuanteller.main.utils.paths import load_dir
from forcuanteller.main.utils.runner import runner
from forcuanteller.main.utils.timedate import get_interval, get_period

import fire


def main(run_id):
    tickers = config.tickers
    period = get_period(config.period)
    interval = get_interval(config.interval)

    for ticker in tickers:
        try:
            ticker_yf = yf.Ticker(ticker)
            df = ticker_yf.history(period=period, interval=interval)

            filename = "{}_{}.csv".format(ticker, run_id)
            filepath = os.path.join(load_dir, filename)
            df.to_csv(filepath)
        except Exception as e:
            logger.warning("ticker : {} is not available".format(ticker))


if __name__ == "__main__":
    logger.info("Running Loader...")
    main(runner.run_id)
    logger.info("Finishing Loader...")
