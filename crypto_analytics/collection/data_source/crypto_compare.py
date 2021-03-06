import pandas as pd
import json
import requests
from typing import Dict, Union

from crypto_analytics.collection.data_source import OHLCVDataSource
from crypto_analytics.types  import Interval

class CryptoCompareOHLCV(OHLCVDataSource):
    endpoints = {
        Interval.MINUTE: 'data/histominute',
        Interval.HOURLY: 'data/histohour',
        Interval.DAILY: 'data/histoday',
    }

    def __init__(self, interval: Interval, fsym: str, tsym: str, limit: int):
        self.__prevalidate(interval, fsym, tsym, limit)

        self.fsym = fsym
        self.tsym = tsym
        self.limit = limit
        self.endpoint = CryptoCompareOHLCV.endpoints.get(interval)
        super().__init__(interval)

    def fetch(self) -> pd.DataFrame:
        url = 'https://min-api.cryptocompare.com/{}'.format(self.endpoint)

        parameters: Dict[str, Union[int, str]] = {
            'fsym': self.fsym,
            'tsym': self.tsym,
            'limit': self.limit
        }
        response = requests.get(url, params=parameters)
        response.raise_for_status()

        data = response.json()
        self.data = pd.DataFrame(data['Data'])
        return self.data

    def write(self, filepath: str):
        self.data.to_csv(filepath)

    def get_time(self):
        return self.data['time']

    def get_open(self):
        return self.data['open']

    def get_close(self):
        return self.data['close']

    def get_high(self):
        return self.data['high']

    def get_low(self):
        return self.data['low']

    def get_volume(self):
        return self.data['volumefrom']

    # private methods

    def __prevalidate(self, interval: Interval, fsym: str, tsym: str, limit: int):
        # validate interval
        if interval is None:
            raise ValueError('Interval must be specified')
        if CryptoCompareOHLCV.endpoints.get(interval) is None:
            raise ValueError('Interval must be daily, hourly or minute')
        # validate fsym
        if tsym is None:
            raise ValueError('From symbol (fsym) must be specified')
        # validate tsym
        if tsym is None:
            raise ValueError('To symbol (tsym) must be specified')
        # validate limit
        if limit is None:
            raise ValueError('Limit must be specified')
