<h5> Data exploration scripts </h5>
This repository contains the scripts to perform PCA, TSNE, and SVD. <br>
<h5> Requirements</h5>
<h3>Software</h3>
Python (version 3.8.5) <br>
Pandas (version 1.1.3) <br>
Seaborn (version 0.11.0) <br>

<h5> How to run the functions? </h5>
The first step is to import the function files in your main.py file:<br>
```
from createPCA import PCAplot
from readData import readDataFile
from createTSNE import TSNEplot
```
To load a data file (txt or csv): <br>
```
file_name='example.txt'
data_set=readDataFile(file_name)
```
Based on the file type (txt or csv) the readData function will seelct '\t' or ','  as separator <br>
