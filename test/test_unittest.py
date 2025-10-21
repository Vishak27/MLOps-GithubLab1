import sys
import os
import unittest

# Get the path to the project's root directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

from src import temperature_converter


class TestTemperatureConverter(unittest.TestCase):

    def test_celsius_to_fahrenheit(self):
        self.assertEqual(temperature_converter.celsius_to_fahrenheit(0), 32)
        self.assertEqual(temperature_converter.celsius_to_fahrenheit(100), 212)
        self.assertEqual(temperature_converter.celsius_to_fahrenheit(-40), -40)
        self.assertEqual(temperature_converter.celsius_to_fahrenheit(37), 98.6)

    def test_fahrenheit_to_celsius(self):
        self.assertEqual(temperature_converter.fahrenheit_to_celsius(32), 0)
        self.assertEqual(temperature_converter.fahrenheit_to_celsius(212), 100)
        self.assertEqual(temperature_converter.fahrenheit_to_celsius(-40), -40)
        self.assertAlmostEqual(temperature_converter.fahrenheit_to_celsius(98.6), 37.0, places=1)

    def test_celsius_to_kelvin(self):
        self.assertEqual(temperature_converter.celsius_to_kelvin(0), 273.15)
        self.assertEqual(temperature_converter.celsius_to_kelvin(100), 373.15)
        self.assertEqual(temperature_converter.celsius_to_kelvin(-273.15), 0)
        self.assertAlmostEqual(temperature_converter.celsius_to_kelvin(25), 298.15, places=2)

    def test_kelvin_to_celsius(self):
        self.assertEqual(temperature_converter.kelvin_to_celsius(273.15), 0)
        self.assertEqual(temperature_converter.kelvin_to_celsius(373.15), 100)
        self.assertEqual(temperature_converter.kelvin_to_celsius(0), -273.15)
        self.assertAlmostEqual(temperature_converter.kelvin_to_celsius(298.15), 25.0, places=2)

    def test_celsius_to_kelvin_below_absolute_zero(self):
        with self.assertRaises(ValueError) as context:
            temperature_converter.celsius_to_kelvin(-274)
        self.assertIn("below absolute zero", str(context.exception))

    def test_kelvin_to_celsius_negative(self):
        with self.assertRaises(ValueError) as context:
            temperature_converter.kelvin_to_celsius(-1)
        self.assertIn("cannot be negative", str(context.exception))

    def test_invalid_input_celsius_to_fahrenheit(self):
        with self.assertRaises(ValueError) as context:
            temperature_converter.celsius_to_fahrenheit("string")
        self.assertIn("must be a number", str(context.exception))

    def test_invalid_input_fahrenheit_to_celsius(self):
        with self.assertRaises(ValueError) as context:
            temperature_converter.fahrenheit_to_celsius(None)
        self.assertIn("must be a number", str(context.exception))

    def test_invalid_input_celsius_to_kelvin(self):
        with self.assertRaises(ValueError) as context:
            temperature_converter.celsius_to_kelvin([1, 2, 3])
        self.assertIn("must be a number", str(context.exception))

    def test_invalid_input_kelvin_to_celsius(self):
        with self.assertRaises(ValueError) as context:
            temperature_converter.kelvin_to_celsius({"temp": 100})
        self.assertIn("must be a number", str(context.exception))


if __name__ == '__main__':
    unittest.main()