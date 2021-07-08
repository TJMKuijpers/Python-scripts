## File to combine the different image.csv objects
import os
import pandas as pd

## Specify the input map with all the image.csv objects
os.chdir('')
allFiles=os.listdir()
count=0
for x in allFiles:
    if counter=0:
        file=pd.read_csv(x,sep="\t")
        imageOjbect=file
        counter=counter+1
    else:
        file_tmp=pd.read_csv(x,sep="\t")
        imageObject=pd.concat(imageObject,file_tmp)
    print(x+'is concatenated')

# See the dimension of imageOjbect
imageObject.shape
