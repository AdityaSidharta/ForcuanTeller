import yaml

from forcuanteller.main.utils.paths import config_path


class Config:
    def __init__(self):
        with open(config_path, "r") as f:
            value = yaml.safe_load(f)

        self.schedule = self.get_schedule(value)
        self.period = self.get_period(value)
        self.interval = self.get_interval(value)
        self.indicators = self.get_indicators(value)
        self.tickers = self.get_tickers(value)

    @staticmethod
    def get_schedule(value):
        return value["schedule"]

    @staticmethod
    def get_period(value):
        return value["period"]

    @staticmethod
    def get_interval(value):
        return value["interval"]

    @staticmethod
    def get_indicators(value):
        return value["indicators"]

    @staticmethod
    def get_tickers(value):
        return value["tickers"]


config = Config()
