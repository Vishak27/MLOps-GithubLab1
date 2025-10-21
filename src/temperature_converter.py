def celsius_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.
    
    Args:
        celsius (float): Temperature in Celsius
        
    Returns:
        float: Temperature in Fahrenheit
        
    Raises:
        ValueError: If celsius is not a number
    """
    if not isinstance(celsius, (int, float)):
        raise ValueError("Temperature must be a number.")
    
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit):
    """
    Convert temperature from Fahrenheit to Celsius.
    
    Args:
        fahrenheit (float): Temperature in Fahrenheit
        
    Returns:
        float: Temperature in Celsius
        
    Raises:
        ValueError: If fahrenheit is not a number
    """
    if not isinstance(fahrenheit, (int, float)):
        raise ValueError("Temperature must be a number.")
    
    return (fahrenheit - 32) * 5/9


def celsius_to_kelvin(celsius):
    """
    Convert temperature from Celsius to Kelvin.
    
    Args:
        celsius (float): Temperature in Celsius
        
    Returns:
        float: Temperature in Kelvin
        
    Raises:
        ValueError: If celsius is not a number or if result would be below absolute zero
    """
    if not isinstance(celsius, (int, float)):
        raise ValueError("Temperature must be a number.")
    
    kelvin = celsius + 273.15
    if kelvin < 0:
        raise ValueError(f"Temperature {celsius}°C is below absolute zero")
    
    return kelvin


def kelvin_to_celsius(kelvin):
    """
    Convert temperature from Kelvin to Celsius.
    
    Args:
        kelvin (float): Temperature in Kelvin
        
    Returns:
        float: Temperature in Celsius
        
    Raises:
        ValueError: If kelvin is not a number or is negative
    """
    if not isinstance(kelvin, (int, float)):
        raise ValueError("Temperature must be a number.")
    
    if kelvin < 0:
        raise ValueError(f"Temperature cannot be negative in Kelvin: {kelvin}")
    
    return kelvin - 273.15