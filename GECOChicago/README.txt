Sepideh Mosaferi, June 3, 2017

This folder contains:
1. lookup-files folder
2. 4 modules
3. generate-data.py

1. look-up files folder:
The folder contains different csv files
related to the frequency tables of attributes and errors.
They have collected from web sources, wikipedia, census bureau
website and DBGEN ZIP Code source.

Link for the raw source of DBGEN: http://www.cs.utexas.edu/users/ml/riddle/data.html
Link for the raw source of GeCo: https://dmm.anu.edu.au/geco/index.php

2. 4 modules:
The modules contain functionsand codes to define how to corrupt the data, produce error, etc.

2.1. attrgenfunct.py: 
This module is for generating attributes. It can generate phone numbers
(based on the American format), credit card numbers, numerical variables which follow
uniform distribution by providing the maximum and minimum values such as generating
age based on uniform, and generating values following the normal distribution by providing
mean, standard error, minimum, and maximum values.

2.2. basefunctions.py: 
This module is for the purpose of providing basic functionality. These
functions are for checking the type and range of variables, how to read a “.csv” file with
a comma as a separator among the values, and how to write a “.csv” file by exporting the
generated data set.

2.3. corruptor.py: 
This module is for corrupting and modifying attributes to define how to apply
a modification, necessary classes, corrupting missing values, and OCR errors which are
related to the optical errors.

2.4. generator.py: 
This module is for generating single and compound attributes.

3. generate-data.py:
This is the main code that one can run to generate
the synthetic data set. The program is in python and the name of the output
is synth-data in a .csv file.


**Note: The main source of program was written by Peter Christen and Dinusha Vatsalan in January-March 2012.**


