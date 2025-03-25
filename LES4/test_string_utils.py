import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("neva", "Neva"),
    ("hello mentor", "Hello mentor"),
    ("samsung", "Samsung"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("92351dfg", "92351dfg"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected",
[
    (" neva", "neva"),
    (" Neva", "Neva"),
    (" My_Neva", "My_Neva"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected",
[
    ("   ", ""),
    ("", ""),
])

def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.posititive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Saint-Petersburg", "-", "SaintPetersburg"),
    ("Saint-Petersburg", "sburg", "Saint-Peter"),
    ("Saint-Petersburg", "t", "Sain-Peersburg")
])

@pytest.mark.posititive
@pytest.mark.parametrize("string, symbol, expected",
[
    ("Saint-Petersburg", "P", True),
    ("Saint-Petersburg", "g", True),
])

def test_contains_positive(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected

@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected",
[
    ("Saint-Petersburg", "W", False),
    ("Saint-Petersburg", "q", False),
])

def test_contains_negative(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected

def  test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected_exception",
[
    ("", "a", ""),
    ("SkyPro", "z", "SkyPro"),
])

def test_delete_symbol_negative(input_str, symbol, expected_exception):
    assert string_utils.delete_symbol(input_str, symbol) ==  expected_exception






