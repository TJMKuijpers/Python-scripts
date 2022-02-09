import seaborn as sns
import matplotlib.pyplot as plt

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
        plt.figure('Histogram')
        sns.displot(data_histogram)
        return data_histogram_count

    def create_lmplot(self,variables_of_interest,variable_of_interest_x,variable_of_interest_y,regression_line=False):
        plt.figure('lmplot')
        data_lmplot = self.data.loc[:,variables_of_interest]
        print(data_lmplot)
        sns.lmplot(variable_of_interest_x,variable_of_interest_y,data=data_lmplot,fit_reg=regression_line)


    def create_violin_plot(self,variable_of_interest):
        plt.figure('Violin plot')
        data_violin=self.data.loc[:,variable_of_interest]
        sns.violinplot(data=data_violin)