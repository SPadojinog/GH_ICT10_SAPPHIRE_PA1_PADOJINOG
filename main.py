# Practical Activity - Temperature Converter
from pyscript import document

def convert_temperature(e):
    result_element = document.getElementById('output')
    result_element.innerHTML = ""

    fahrenheit = float(document.getElementById('fahrenheit').value)

    # Convertion
    celsius = (fahrenheit - 32) * 5 / 9

    # Checking
    if celsius >= 37.8:
        status = "Fever detected"
    else:
        status = "No fever"

    # Display result
    result = f"""
    🌡️ <b>Temperature in Celsius:</b> {celsius:.2f} °C<br>
    🩺 <b>Status:</b> {status}
    """

    result_element.innerHTML = result

