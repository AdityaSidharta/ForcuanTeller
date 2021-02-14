from forcuanteller.main.indicators.bollingerband import BollingerBandInd
from forcuanteller.main.indicators.macd import MACDInd
from forcuanteller.main.indicators.rsi import RSIInd


def load_indicator(indicator_info):
    if indicator_info['name'] == 'BollingerBandInd':
        return BollingerBandInd(indicator_info)
    elif indicator_info['name'] == 'RSIInd':
        return RSIInd(indicator_info)
    elif indicator_info['name'] == 'MACDInd':
        return MACDInd(indicator_info)
    else:
        raise ValueError("Invalid indicator_info_name : {}".format(indicator_info['name']))