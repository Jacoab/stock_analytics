import pytest, re

from crypto_analytics.types.symbol import (Symbol, SymbolPair, SymbolStandard,
    KrakenSymbolPairConverter, SymbolPairConverterError)

# test kraken symbol pair converter

def test_kraken_symbol_pair_converter_map_bijection():
    # given
    pairs = list(KrakenSymbolPairConverter.from_pair_map.keys())
    # when
    values = [KrakenSymbolPairConverter.from_pair_map[pair] for pair in pairs]
    recovered_pairs = [KrakenSymbolPairConverter.to_pair_map[value] for value in values]
    # then
    assert pairs == recovered_pairs

def test_kraken_symbol_pair_converter_standard():
    # when
    standard = KrakenSymbolPairConverter.get_standard()
    # then
    expected = SymbolStandard.KRAKEN
    assert standard == expected


# test from_pair

def test_kraken_symbol_pair_converter_from_pair_success():
    # given
    pair = SymbolPair(Symbol.BITCOIN, Symbol.USD)
    # when
    converted = KrakenSymbolPairConverter.from_pair(pair)
    # then
    expected = 'XXBTZUSD'
    assert converted == expected

def test_kraken_symbol_pair_converter_from_pair_failure():
    # given
    pair = SymbolPair(None, None)
    # when
    with pytest.raises(SymbolPairConverterError):
        converted = KrakenSymbolPairConverter.from_pair(pair)


# test to_pair

def test_kraken_symbol_pair_converter_to_pair_success():
    # given
    value = 'XXBTZUSD'
    # when
    converted = KrakenSymbolPairConverter.to_pair(value)
    # then
    expected = SymbolPair(Symbol.BITCOIN, Symbol.USD)
    assert converted == expected

def test_kraken_symbol_pair_converter_to_pair_failure():
    # given
    value = None
    # when
    with pytest.raises(SymbolPairConverterError):
        converted = KrakenSymbolPairConverter.to_pair(value)
