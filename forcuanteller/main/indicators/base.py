class Indicator:
    def __init__(self, indicator):
        self.indicator = indicator
        self.name = self.get_name()
        self.param = self.get_param()

    def get_name(self):
        raise NotImplementedError()

    def get_param(self):
        raise NotImplementedError()

    def get_signal(self, input_df, ticker, run_id):
        raise NotImplementedError()
