import time

from crypto_analytics.collection.data_handler import ColumnMapper
from crypto_analytics.collection.data_source import CryptoCompareOHLCV, KrakenOHLCV
from crypto_analytics.types import Interval, MergeType

class PumpPredictionDataHandler(ColumnMapper):
    """ A data handler used to transdorm data for pump prediction models """

    def __init__(self, pair: str, fsym: str, tsym: str, rows: int):
        """ Creates the PumpPredictionDataHandler data handler object """
        interval = Interval.MINUTE
        merge_type = MergeType.INTERSECT
        limit = rows - 1
        interval_duration = interval.to_unix_time()
        # calculate time at rows intervals ago
        since = int(time.time() - rows*interval_duration)

        data_sources = {
            'crypto_compare_ohlcv': CryptoCompareOHLCV(interval, fsym, tsym, limit),
            'kraken_ohlcv': KrakenOHLCV(interval, pair, since),
        }
        column_map = {
            'crypto_compare_ohlcv': {
                'time': 'time',
                'open': 'cc_open',
                'high': 'cc_high',
                'low': 'cc_low',
                'close': 'cc_close',
                'volumefrom': 'cc_volumefrom',
                'volumeto': 'cc_volumeto',
            },
            'kraken_ohlcv': {
                'time': 'time',
                'open': 'k_open',
                'high': 'k_high',
                'low': 'k_low',
                'close': 'k_close',
                'vwap': 'k_vwap',
                'volume': 'k_volume',
                'count': 'k_count',
            },
        }
        super().__init__(data_sources, column_map, merge_type)
