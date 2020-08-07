# # MIT License

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
# Salinity.py is command-line Python program written in Python 3 that calculates fluid inclusion salinities 
# for several fluid inclusions simultaneously.
# This software calculate salinities using ice-melting temperatures for aqueous-electrolitic fluids 
# in the system NaCl-H2O, for salinities up to 23 % in mass.

# References:

# Bodnar, R.J., 1993. Revised equation and table for determining the freezing point depression of H2O-Nacl solutions.
# Geochimica et Cosmochimica Acta 57, 683–684. doi:10.1016/0016-7037(93)90378-A

# Bodnar, R.J., Vityk, M.O., 1994. Interpretation of microthermometric data for H2O-NaCl fluid inclusions, in: 
# De Vivo, B., Frezzotti, M.L. (Eds.), Fluid Inclusions in Minerals, Methods and Applications. 
#Virginia Tech Blackburg, pp. 117–130.

# USAGE:

# Access the the directory where isochore.py is stored
# In the terminal prompt, execute: 'python isochore.py filename'
# files must be saved in the CSV file format, with data structured in three columns: 'id, Th, TmIce'
# The results are saved as a CSV file in the same directory

from sys import argv, exit

import csv

def salty1(TmIce):
    '''
    Function that takes ice melting temperatures (in Celsius) and calculates salinities (Bodnar & Vytik, 1994).
    '''

    Salinity = (1.78 * (TmIce * -1) + 0.0442 * (TmIce * -1) ** 2
            + 0.000557 * (TmIce * -1) ** 3)
    
    return Salinity

def main():
    '''
    Salinity.py is command-line Python program that calculates fluid inclusion salinities 
    for several fluid inclusions simultaneously. References: Bodnar (1993) and Bodnar & Vytik (1994).
    '''

    if not len(argv) == 2:
        print('Usage: python salinity.py filename.csv')
        exit(1)

    with open(argv[1], 'r') as file:
        reader = csv.reader(file)

        header = next(reader)

        reader = list(reader)

        for row in reader:

            row[1] = float(row[1])
            row[2] = float(row[2])

        Salinity = []
        for row in reader:

            values = salty1(row[2])
            Salinity.append(values)
        
        for i, row in enumerate(reader):
            
            row.append(Salinity[i])  

        data = reader 

        header.append('Salinity')

        data.insert(0, header)

        print(data)

        while True:
            newName = input("File Name:")
            if not newName:
                continue
            else:
                break

        with open(newName + '.csv', 'w', newline='') as newFile:
            writer = csv.writer(newFile)

            writer.writerows(data)

    file.close()
    newFile.close()
    exit(0)
    
if __name__ == '__main__':
    main()