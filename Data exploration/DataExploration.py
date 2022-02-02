import pandas as pd
import seaborn as sns

class DataExploration:

    def __init__(self, data_object):
        self.data = data_object

    def get_overview_of_data(self):
        print('Dataframe info')
        print(self.data.info())
        print('Summary dataframe')
        print(self.data.describe())

    def get_histogram(self, variable_of_interest):
        data_histogram = self.data.loc[:,variable_of_interest]
        data_histogram_count = data_histogram.value_counts()
        sns.displot(data_histogram)
        return data_histogram_count


    