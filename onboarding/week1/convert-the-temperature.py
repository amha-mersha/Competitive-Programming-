class Solution(object):
    def convertTemperature(self, celsius):
        Kelvin = celsius + 273.15
        Fahrenheit = celsius * 1.8 + 32.00
        return [Kelvin, Fahrenheit]