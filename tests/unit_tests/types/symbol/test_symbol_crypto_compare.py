import pytest, re

from crypto_analytics.types.symbol import (Symbol, SymbolPair, SymbolStandard,
    CryptoCompareSymbolPairConverter, CryptoCompareSymbolPair, SymbolPairConverterError)

# test kraken symbol pair converter

def test_crypto_compare_symbol_pair_converter_map_bijection():
    # given
    symbols = list(CryptoCompareSymbolPairConverter.from_symbol_map.keys())
    # when
    values = [CryptoCompareSymbolPairConverter.from_symbol_map[symbol] for symbol in symbols]
    recovered_symbols = [CryptoCompareSymbolPairConverter.to_symbol_map[value] for value in values]
    # then
    assert symbols == recovered_symbols

def test_crypto_compare_symbol_pair_converter_standard():
    # when
    standard = CryptoCompareSymbolPairConverter.get_standard()
    # then
    expected = SymbolStandard.CRYPTO_COMPARE
    assert standard == expected


# test from_pair

def test_crypto_compare_symbol_pair_converter_from_pair_success():
    # given
    pair = SymbolPair(Symbol.BITCOIN, Symbol.USD)
    # when
    converted = CryptoCompareSymbolPairConverter.from_pair(pair)
    # then
    expected = CryptoCompareSymbolPair('BTC', 'USD')
    assert converted == expected

def test_crypto_compare_symbol_pair_converter_from_pair_failure():
    # given
    pair = SymbolPair(None, None)
    # when
    with pytest.raises(SymbolPairConverterError):
        converted = CryptoCompareSymbolPairConverter.from_pair(pair)


# test to_pair

def test_crypto_compare_symbol_pair_converter_to_pair_success():
    # given
    value = CryptoCompareSymbolPair('BTC', 'USD')
    # when
    converted = CryptoCompareSymbolPairConverter.to_pair(value)
    # then
    expected = SymbolPair(Symbol.BITCOIN, Symbol.USD)
    assert converted == expected

def test_crypto_compare_symbol_pair_converter_to_pair_failure():
    # given
    value = None
    # when
    with pytest.raises(SymbolPairConverterError):
        converted = CryptoCompareSymbolPairConverter.to_pair(value)
