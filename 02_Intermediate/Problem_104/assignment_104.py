'''
Write A Python Program To Get Temperature 
In Centigrade, To Convert Into Fahrenheit 
And Kelvin 
'''
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def celsius_to_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin


if __name__=="__main__":
    celsius = float(input("Enter temperature in Celsius: "))

    fahrenheit = celsius_to_fahrenheit(celsius)
    kelvin = celsius_to_kelvin(celsius)

    print("Temperature in Fahrenheit:", fahrenheit)
    print("Temperature in Kelvin:", kelvin)
