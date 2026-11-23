def check_temperature(temperature: str) -> str:
        try:
            temp = int(temperature)
        except ValueError as e:
            raise ValueError(f"Invalid temperature value: {temperature}. Please provide a valid integer.") from e

        if temp < 0:
             raise ValueError(f"Temperature {temp} is below freezing point. Please provide a temperature above 0°C.")
        elif temp > 40:
            raise ValueError(f"Temperature {temp} is too high for this application. Please provide a temperature below 40°C.")
        else:
            return f"The temperature is {temp} degrees Celsius."

def test_check_temperature():
    test_cases = [
        ("25", "The temperature is 25 degrees Celsius."),
        ("-5", "Temperature -5 is below freezing point. Please provide a temperature above 0°C."),
        ("45", "Temperature 45 is too high for this application. Please provide a temperature below 40°C."),
        ("abc", "Invalid temperature value: abc. Please provide a valid integer."),
    ]

    for input_value, expected_output in test_cases:
        try:
            result = check_temperature(input_value)
            assert result == expected_output, f"Test failed for input {input_value}. Expected: {expected_output}, Got: {result}"
            print(f"Test passed for input {input_value}.")
        except ValueError as e:
            assert str(e) == expected_output, f"Test failed for input {input_value}. Expected: {expected_output}, Got: {str(e)}"
            print(f"Test passed for input {input_value} with exception: {str(e)}")
if __name__ == "__main__":
    test_check_temperature()