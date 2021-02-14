import datetime


class Runner:
    def __init__(self):
        self.run_id = self.get_run_id()

    @staticmethod
    def get_run_id():
        return datetime.datetime.now().strftime("%Y%m%d%H%M%S")


runner = Runner()
