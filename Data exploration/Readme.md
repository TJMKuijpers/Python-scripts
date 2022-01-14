<h5> Data exploration scripts </h5>
This repository contains the scripts to perform PCA, TSNE, and SVD. <br>
<h5> Requirements</h5>
<h3>Software</h3>
Python (version 3.8.5) <br>
Pandas (version 1.1.3) <br>
Seaborn (version 0.11.0) <br>

<h5> How to run the functions? </h5>
The first step is to import the function files in your main.py file:<br>
  
```python
from createPCA import PCAplot
from readData import readDataFile
from createTSNE import TSNEplot
```
  
To load a data file (txt or csv): <br>
  
```python
file_name='example.txt'
data_set=readDataFile(file_name)
```
  
Based on the file type (txt or csv) the readData function will seelct '\t' or ','  as separator <br>
Please note that the PCA and TSNE analysis assume the data contains no NAs. NAs can be removed by using the following lines: <br>
```python
# remove NAs for PCA and TSNE  (row-wise: axis=0, column-wise=1)
data_set=data_set.remove_NaN(axis_df=0)
data_set=data_set.remove_NaN(axis_df=1)
```
  
  
To perform an PCA analysis:
  
```python
pca_plot=PCAplot(data=data_set,components=10)
pca_plot.perform_pca()
# get the variance explained by the principal components
pca_plot.plot_variance_explaned()
pca_plot.plot_pca_results(component_one=0,component_two=1,label=None,style_point=None)
# get the loading information
pca_plot.loading_information(data=data_set)
```
  
 As you can see, it is possible to set the label and style points for the samples in your data. To do so, provide an array with the information: <br>
   
 ```python
 label_information=['A','A','A','A','B','B','B','B']
 style_information=['o','o','o','o','s','s','s','s']
 ```
 
 To run a TSNE analysis 
   
 ```python
tsne_plot=TSNEplot(data=data_set,components=2)
tsne_plot.calculate_tsne()
tsne_plot.plot_tsne_results(component_one=0,component_two=1,label=None,style_point=None)
```
  
Again you can add label and style markers by defining them in a variable. <br>

  
