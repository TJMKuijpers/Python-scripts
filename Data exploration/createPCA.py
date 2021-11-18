from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

class PCAplot:

    def __init__(self,data,components):
        self.data=data
        self.number_components=components
        self.pca=None
        self.pca_output=None
        self.loadings=None
        self.loading_matrix = None

    def perform_pca(self):
        pca=PCA(n_components=self.number_components,svd_solver='randomized')
        pca_output=pca.fit_transform(self.data)
        self.pca_output=pca_output
        self.pca=pca
        print('Explained variation per principal component: {}'.format(pca.explained_variance_ratio_))

    def plot_variance_explained(self):
        plt.rcParams.update({'font.size': 16})
        plt.figure(figsize=(20,15))
        number_components=range(1,self.pca.explained_variance_ratio_.__len__()+1)
        labels_components=['Component '+str(i) for i in number_components]
        plt.bar(number_components,self.pca.explained_variance_ratio_)
        plt.xticks(number_components,labels_components,rotation=45)
        plt.title('Variance explained by the {} principal components'.format(number_components.__len__()))
        plt.show()

    def plot_pca_results(self,component_one,component_two,label=None,style_point=None):
        plt.figure(figsize=(20,15))
        plt.rcParams.update({'font.size': 16})
        sns.set_theme(style="white",font_scale=2)
        sns.scatterplot(x=self.pca_output[:,component_one],y=self.pca_output[:,component_two],hue=label,style=style_point,s=150)
        plt.xlabel("Principal component {}".format(component_one+1)+' (variance explained: {})'.format(self.pca.explained_variance_ratio_[component_one]))
        plt.ylabel("Principal component {}".format(component_two+1)+' (variance explained: {})'.format(self.pca.explained_variance_ratio_[component_two]))
        plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)


    def plot_pca_3d(self,component_one,component_two,component_three,label=None,style_point=None):
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        ax.scatter(self.pca_output[:,component_one], self.pca_output[:,component_two], self.pca_output[:,component_three],c=label,s=70)

    def loading_information(self,data=None):
        self.loadings = self.pca.components_.T * np.sqrt(self.pca.explained_variance_)
        print(self.loadings)
        self.loading_matrix = pd.DataFrame(self.loadings,index=data.columns)