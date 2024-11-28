def percent(value:float) -> str:
    """
    Converts a decimal value to a percentage string
    
    Args:
        value: A float representing a percentage as a decimal 

    Returns:
        A string representing the percentage (e.g., "25%").

    Raises:
        ValueError: If the value is not a float, or if it is outside the range [0.0, 1.0].
    """
    if type(value) != float:
        raise ValueError("Input must be a float.")
    if not (0.0 <= value <= 1.0):
        raise ValueError("Value must be in the range 0.0 to 1.0.")
    percentage = round(value * 100)
    return (percentage)

if __name__ == "__main__":
    value = float(input("Please input a float from 0.0 to 1.0: "))
    print(f"{percent(value)}%")

