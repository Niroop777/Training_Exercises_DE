#EX 6

# Pandas Series Creation and Indexing

import pandas as pd 

celsius = pd.Series([21,22,23,24,25,26,17,18,19,20,35])

Farenheit = celsius * 1.8 + 32

print("celsius: \n", celsius)
print("Farenheit: \n", Farenheit) 


"""

This program creates a Pandas Series of temperatures in Celsius.

It then converts them to Fahrenheit using the same index.

"""