from crypto_analytics.types import Interval
from crypto_analytics.collection.data_handler import PumpPredictionDataHandler
from crypto_analytics.collection.data_source import CryptoCompareOHLCV, KrakenOHLCV
from crypto_analytics.controller import CollectionController
from crypto_analytics.types.symbol import Symbol, SymbolPair

from crypto_analytics.controller import Controller
from crypto_analytics.types import Interval, MergeType
from crypto_analytics.types.symbol import SymbolPair
from typing import Mapping, List, Tuple, Optional
from crypto_analytics.utils.typing import RealNumber

pair = SymbolPair(Symbol.BITCOIN, Symbol.USD)
interval = Interval.MINUTE
redundancy = 3

data_sources = {
    # 'crypto_compare_ohlcv': CryptoCompareOHLCV(interval, pair, 2000),
    # 'kraken_ohlcv': KrakenOHLCV(interval, pair, 719),
    'crypto_compare_ohlcv': CryptoCompareOHLCV(interval, pair, 5),
    'kraken_ohlcv': KrakenOHLCV(interval, pair, 3),
}

collection_controller = CollectionController(pair, data_sources, redundancy)
collection_controller.run()
