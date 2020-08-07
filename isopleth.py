# MIT License

# Copyright (c) 2020 Andre Luiz Silva Pestilho

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# ABOUT:
# Isopleth.py is a command-line Python program written in Python 3 that calculates fluid inclusion isopleth for a
# fluid inclusion in the system NaCl-H2O. References: Atkinson (2002)
# Temperature range: -21.2 to 484 °C
# Salinity range: 0 to 100 mass %. equivalent in NaCl

# REFERENCES:

# Atkinson, A.B.J., 2002. A Model for the PTX Properties of H2O-NaCl [Master Thesis]. 
# Virginia Polytechnic Institute and State University, Blacksburg, Virginia, USA.

# USAGE:

# Access the the directory where isochore.py is stored
# In the terminal prompt, execute: 'python isopleth.py' 
# The results are saved as a CSV file in the same directory

from sys import exit

import csv

def getPh(Temperature, Salinity):
    '''
    Function that takes salinity and homogenization temperature (Th, in Celsius) and calculates 
    the pressure (in bars) at liquid-vapor line (Atkinson, 2002).
    '''

    T = (Temperature + 273.15) / 100

    X = (Salinity) / 100

    W = (1.0001 - X / 1.0001) * (2.5 / T)
    
    if Temperature < 300:

        logPh = (-27.2444260945047 - (3.43823854919821 * X) + 49.6470810423974 * (X ** 3) + 284.920532084465 * (X ** 4)
            - 671.468924936888 * (X ** 5) - 306.420824097701 * (X ** 6) - 476.3912831617690 * (X ** 7) 
            + (19.6752698743832 * T) - 6.03987279418686 * (T ** 2) + 1.05318996126294 * (T ** 3) 
            - 0.107523830798341 * (T ** 4) + 0.0063216048751384 * (T ** 5) - 0.000201391014431089 * (T ** 6) 
            + 0.0000029370853393422 * (T ** 7) + 2.94599944070388 * T * X - 5.05959726370657 * T * (X ** 2) 
            - 78.057932502234 * T * (X ** 3) + (272.541674619991 * T * (X ** 5)) + (191.281847960897 * T * (X ** 6)) 
            - 1.02712250242286 * (T ** 2) * X + (5.3605248349362 * (T ** 2) * (X ** 2)) 
            + 18.9371135629599 * (T ** 2) * (X ** 3) - 27.5731923399911 * (T ** 2) * (X ** 4) 
            - 43.6261697756668 * (T ** 2) * (X ** 5) + 0.132241696257544 * (T ** 3) * (X ** 1) 
            - 1.43460393380215 * (T ** 3) * (X ** 2) - 0.517812895404053 * (T ** 3) * (X ** 3) 
            + 4.28981312806579 * (T ** 3) * (X ** 4) + 0.115824432759682 * (T ** 4) * (X ** 2) 
            - 0.147543794540513 * (T ** 4) * (X ** 3) - 0.000792743415349166 * (T ** 5) * X + W)

    else:

        logPh = (-7.250911394178014 + 52.7356253268118 * X - 95.139589091999 * (X ** 2) 
            + 237.001333358832 * (X ** 3) - 270.853923550159 * (X ** 4) - 645.843502315573 * (X ** 6) 
            + 411.125432162485 * (X ** 7) + 2.91847163119225 * T - 0.282727704099067 * (T ** 2) 
            + 0.00898343968706551 * (T ** 3) + 0.0000015228510009732 * (T ** 6) 
            - 30.0742277771278 * T * X + 41.0055099275695 * T * (X ** 2) 
            - 82.6121950337547 * T * (X **3) + 86.8864476861164 * T * (X ** 4) 
            + 85.0303689746524 * T * (X ** 5) - 24.1431916305905 * T * (X ** 6) 
            + 5.98143068258883 * (T ** 2) * X - 5.87588111777108 * (T ** 2) * (X ** 2) 
            + 7.89995198785004 * (T ** 2) * (X ** 3) - 10.886118260654 * (T ** 2) * (X ** 4) 
            - 0.436696998416016 * (T ** 3) * (X ** 1) + 0.27654361988714 * (T ** 3) * (X ** 2) 
            - 0.0074586977134027 * (T ** 4) * (X ** 3) + 0.000828114542697018 * (T ** 5) * X 
            + 0 * (T ** 6) * X + W)

    Ph = 10 ** logPh

    return Ph

def main():
    '''
    Isopleth.py is a command-line Python program that calculates fluid inclusion isopleth for a
    fluid inclusion in the system NaCl-H2O. References: Bodnar & Vytik (1994) and Atkinson (2002)
    '''

    print('Isopleth.py: Command-line program to calculate fluid inclusion isopleths in the system NaCl-H2O')
    print('Reference: Bodnar & Vytik (1994) and Atkinson (2002)')
    print('Temperature range: -21.2 to 484 °C')
    print('Salinity range: 0 to 100 mass %. equivalent in NaCl')
    print('Type the paramters to calculate isopleths in the system H2O-NaCl bellow:') 

    while True:
        Salinity = input('Salinity (mass %. eq. in NaCl: ')
        if not Salinity:
            continue
        elif Salinity.isalpha():
            continue
        elif Salinity == '-' or Salinity == '+' or Salinity == ',' or Salinity == '.':
            continue
        elif float(Salinity) < 0:
            continue
        else:
            break

    while True:
        minT = input('Minimum temperature (°C): ')
        if not minT:
            continue
        elif minT.isalpha():
            continue
        elif minT == '-' or minT == '+' or minT == ',' or minT == '.':
            continue
        elif int(minT) < 0:
            continue
        else:
            break

    while True:
        maxT = input('Maximum temperature (°C): ')
        if not maxT:
            continue
        elif maxT.isalpha():
            continue
        elif maxT == '-' or maxT == '+' or maxT == ',' or maxT == '.':
            continue
        elif int(maxT) < 0:
            continue
        elif int(maxT) < int(minT):
            continue
        else:
            break

    while True:
        stepT = input('Temperature step (°C): ')
        if not stepT:
            continue
        elif stepT.isalpha():
            continue
        elif stepT == '-' or stepT == '+' or stepT == ',' or stepT == '.':
            continue
        elif int(stepT) < 0:
            continue
        elif int(stepT) > (int(maxT) - int(minT)):
            continue
        else:
            break

    while True:
        Precision = input('Digits after decimal point (0-5): ')
        if not Precision:
            continue
        elif Precision.isalpha():
            continue
        elif Precision == '-' or Precision == '+' or Precision == ',' or Precision == '.':
            continue
        elif int(Precision) < 0:
            continue
        elif int(Precision) > 5:
            continue
        else:
            break

    Salinity = float(Salinity)
    minT = int(minT)
    maxT = int(maxT)
    stepT = int(stepT)
    Precision = int(Precision)

    Temperature,  Pressure, data = [], [], []

    for i in range(minT, (maxT+stepT), stepT):
        Temperature.append(i)

    for i,T in enumerate(Temperature):
        Pressure.append(i)
        Pressure[i] = round(getPh(T, Salinity), Precision)

    for rows in zip(Temperature, Pressure):
        data.append(rows)

    header = ('Temperature (Celsius)', 'Pressure (bar)')

    data.insert(0, header)

    while True:
        newName = input("File Name:")
        if not newName:
            continue
        else:
            break

    with open(newName + '.csv', 'w', newline='') as outFile:
        writer = csv.writer(outFile)
        writer.writerows(data)

    outFile.close()
    exit(0)
    
if __name__ == '__main__':
    main()