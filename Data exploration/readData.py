import pandas as pd

class readDataFile:
    def __init__(self,location_of_data):
        self.data_location=location_of_data
        self.data=None

    def read_data(self):
        if self.data_location.endswith('.txt'):
            data_file = pd.read_csv(self.data_location, sep='\t')
        if self.data_location.endswith('.csv'):
            data_file = pd.read_csv(self.data_location, sep=',')
        self.data=data_file

    def remove_NaN(self,axis_df=None):
        self.data_na_removed=self.data.dropna(axis=axis_df)
