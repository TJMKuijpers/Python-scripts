from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns
class PCAplot:

    def __init__(self,data,components):
        self.data=data
        self.number_components=components
        self.pca=None
        self.pca_output=None

    def perform_pca(self):
        pca=PCA(n_components=self.number_components)
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

    def plot_pca_results(self,component_one,component_two,label):
        plt.figure(figsize=(16,10))
        sns.scatterplot(x=self.pca_output[:,component_one],y=self.pca_output[:,component_two])
