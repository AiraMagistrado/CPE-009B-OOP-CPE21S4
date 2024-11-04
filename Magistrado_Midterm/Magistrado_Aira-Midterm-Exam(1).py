
class TemperatureConversion:
    def __init__(self, temp=1):
      self._temp = temp

class CelsiusToFahrenheit(TemperatureConversion):
    def conversion(self):
      return (self._temp * 9) / 5 + 32

class FahrenheitToCelsius(TemperatureConversion):
    def conversion(self):
      return (self._temp * 5) / 9 - 32
class CelsiusToKelvin(TemperatureConversion):
    def conversion(self):
      return (self._temp) + 273.15

class KelvinToCelcius(TemperatureConversion):
    def conversion(self):
      return (self._temp) - 273.15

tempInCelsius = float(input("Enter the temperature in Celsius: "))
convert = CelsiusToKelvin(tempInCelsius)
print(str(convert.conversion()) + " Kelvin")
convert = FahrenheitToCelsius(tempInCelsius)
print(str(convert.conversion()) + " Celsius")
convert = CelsiusToFahrenheit(tempInCelsius)
print(str(convert.conversion()) + " Fahrenheit")
convert = KelvinToCelcius(tempInCelsius)
print(str(convert.conversion()) + " Celsius")