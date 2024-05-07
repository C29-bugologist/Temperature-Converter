# 0°C × 9/5) + 32 = 32°F Celsius to fehrenheit
#(32°F − 32) × 5/9 = 0°C fehrenheit to celsius
number = int(input("enter the number of either celsius or fehrenheit \n"))
C_F = int(input(" Enter 1 for Celsius \n Enter 2 for Fehrenhit \n"))
if C_F == 1:
    fehrenheit = (number * 9/5) + 32
    print(number, "in Fehrenheit is")
    print(fehrenheit)
else:
    celsius = (number - 32) * 5/9
    print(number, "in Celsius is")
    print(celsius)
