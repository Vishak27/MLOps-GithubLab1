import pytest
from src import temperature_converter

def test_celsius_to_fahrenheit():
    assert temperature_converter.celsius_to_fahrenheit(0) == 32
    assert temperature_converter.celsius_to_fahrenheit(100) == 212
    assert temperature_converter.celsius_to_fahrenheit(-40) == -40
    assert temperature_converter.celsius_to_fahrenheit(37) == 98.6


def test_fahrenheit_to_celsius():
    assert temperature_converter.fahrenheit_to_celsius(32) == 0
    assert temperature_converter.fahrenheit_to_celsius(212) == 100
    assert temperature_converter.fahrenheit_to_celsius(-40) == -40
    assert round(temperature_converter.fahrenheit_to_celsius(98.6), 1) == 37.0


def test_celsius_to_kelvin():
    assert temperature_converter.celsius_to_kelvin(0) == 273.15
    assert temperature_converter.celsius_to_kelvin(100) == 373.15
    assert temperature_converter.celsius_to_kelvin(-273.15) == 0
    assert round(temperature_converter.celsius_to_kelvin(25), 2) == 298.15


def test_kelvin_to_celsius():
    assert temperature_converter.kelvin_to_celsius(273.15) == 0
    assert temperature_converter.kelvin_to_celsius(373.15) == 100
    assert temperature_converter.kelvin_to_celsius(0) == -273.15
    assert round(temperature_converter.kelvin_to_celsius(298.15), 2) == 25.0


# Test error cases
def test_celsius_to_kelvin_below_absolute_zero():
    with pytest.raises(ValueError, match="below absolute zero"):
        temperature_converter.celsius_to_kelvin(-274)


def test_kelvin_to_celsius_negative():
    with pytest.raises(ValueError, match="cannot be negative"):
        temperature_converter.kelvin_to_celsius(-1)


def test_invalid_input_types():
    with pytest.raises(ValueError, match="must be a number"):
        temperature_converter.celsius_to_fahrenheit("string")
    
    with pytest.raises(ValueError, match="must be a number"):
        temperature_converter.fahrenheit_to_celsius(None)
    
    with pytest.raises(ValueError, match="must be a number"):
        temperature_converter.celsius_to_kelvin([1, 2, 3])
    
    with pytest.raises(ValueError, match="must be a number"):
        temperature_converter.kelvin_to_celsius({"temp": 100})


# Parametrized tests for multiple values
@pytest.mark.parametrize("celsius,fahrenheit", [
    (0, 32),
    (100, 212),
    (-40, -40),
    (37, 98.6),
    (20, 68),
    (-273.15, -459.67)
])
def test_parametrized_conversions(celsius, fahrenheit):
    assert round(temperature_converter.celsius_to_fahrenheit(celsius), 2) == round(fahrenheit, 2)
    assert round(temperature_converter.fahrenheit_to_celsius(fahrenheit), 2) == round(celsius, 2)