import pandas as pd

class ReadDataFile:

    def __init__(self,location_of_data):
        self.data_location = location_of_data
        self.data = None
        self.data_na_removed = None
        self.na_removed = False

    def read_data(self):
        if self.data_location.endswith('.txt'):
            data_file = pd.read_csv(self.data_location, sep='\t')
            self.data = data_file
        if self.data_location.endswith('.csv'):
            data_file = pd.read_csv(self.data_location, sep=',')
            self.data = data_file
        print('Data is loaded')
        return None


    def remove_nan(self,axis_df=None):
        self.data_na_removed=self.data.dropna(axis=axis_df)
        self.na_removed=True
        return True

    def return_data_object(self):
        print(self.data)
        if self.na_removed:
            data_returned = self.data_na_removed
        else:
            data_returned = self.data
        return data_returned