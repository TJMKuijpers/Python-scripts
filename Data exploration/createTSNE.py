##############################################################################################################
######################## Script to analyze the data with tSNE ################################################
##############################################################################################################

# Import the libraries

from sklearn.manifold import TSNE
import seaborn as sns
import matplotlib.pyplot as plt

class TSNEplot:

    def __init__(self,data=None,components=None):
        self.data=data
        self.number_of_components=components

    def calculate_tsne(self):
        tsne = TSNE(n_components=self.number_of_components, verbose=1, random_state=123,perplexity=6, n_iter=1000)
        self.tsne_output = tsne.fit_transform(self.data.transpose())

    def plot_tsne_results(self, component_one, component_two,label=None,style_point=None):
        plt.figure(figsize=(20, 15))
        plt.rcParams.update({'font.size': 16})
        sns.set_theme(style="white", font_scale=2)
        sns.scatterplot(x=self.tsne_output[:, component_one], y=self.tsne_output[:, component_two],hue=label,style=style_point,s=150)
        plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

