# Fluid Inclusions Programs

1.ISOCHORE.PY:
Isochore.py is a command-line Python program written in Python 3 that calculates fluid inclusion isochores for a
fluid inclusion in the system NaCl-H2O.
Homogenization temperature (Th) values up to 700 °C
Salinity range: 0 to 40 mass %. equivalent in NaCl

1.1.USAGE:
I.Access the the directory where isochore.py is stored
II.In the terminal prompt, execute: 'python isochore.py'
III.The results are saved as a CSV file in the same directory

1.1.REFERENCES:
Atkinson, A.B.J., 2002. A Model for the PTX Properties of H2O-NaCl [Master Thesis]. 
  Virginia Polytechnic Institute and State University, Blacksburg, Virginia, USA.
Bodnar, R.J., Vityk, M.O., 1994. Interpretation of microthermometric data for H2O-NaCl fluid inclusions, in: 
  De Vivo, B., Frezzotti, M.L. (Eds.), Fluid Inclusions in Minerals, Methods and Applications. 
  Virginia Tech Blackburg, pp. 117–130.

2.ISOPLETH.py v 0.1.1
Isopleth.py is a command-line Python program written in Python 3 that calculates fluid inclusion isopleth for a
fluid inclusion in the system NaCl-H2O.
Temperature range: -21.2 to 1500 °C
Salinity range: 0 to 100 mass %. equivalent in NaCl

2.1.USAGE:
I.Access the the directory where isochore.py is stored
II.In the terminal prompt, execute: 'python isopleth.py' 
III.The results are saved as a CSV file in the same directory

2.2.REFERENCES:
Atkinson, A.B.J., 2002. A Model for the PTX Properties of H2O-NaCl [Master Thesis]. 
  Virginia Polytechnic Institute and State University, Blacksburg, Virginia, USA.
Bodnar, R.J., Vityk, M.O., 1994. Interpretation of microthermometric data for H2O-NaCl fluid inclusions, in: 
  De Vivo, B., Frezzotti, M.L. (Eds.), Fluid Inclusions in Minerals, Methods and Applications. 
  Virginia Tech Blackburg, pp. 117–130.
Knight, C.L., Bodnar, R.J., 1989. Synthetic fluid inclusions: IX. Critical PVTX properties of NaCl-H2O solutions. 
  Geochimica et Cosmochimica Acta 53, 3–8. doi:10.1016/0016-7037(89)90267-6

3. SALINITY.PY
Salinity.py is command-line Python program written in Python 3 that calculates fluid inclusion salinities 
for several fluid inclusions simultaneously.
This software calculate salinities using ice-melting temperatures for aqueous-electrolytic fluids 
in the system NaCl-H2O, for salinities up to 23 % in mass.

3.1.USAGE:
I.Access the the directory where isochore.py is stored
II.In the terminal prompt, execute: 'python isochore.py filename'
files must be saved in the CSV file format, with data structured in three columns: 'id, Th, TmIce'
III.The results are saved as a CSV file in the same directory

3.2.REFERENCES
Bodnar, R.J., 1993. Revised equation and table for determining the freezing point depression of H2O-Nacl solutions.
  Geochimica et Cosmochimica Acta 57, 683–684. doi:10.1016/0016-7037(93)90378-A
Bodnar, R.J., Vityk, M.O., 1994. Interpretation of microthermometric data for H2O-NaCl fluid inclusions, in: 
  De Vivo, B., Frezzotti, M.L. (Eds.), Fluid Inclusions in Minerals, Methods and Applications. 
  Virginia Tech Blackburg, pp. 117–130.
