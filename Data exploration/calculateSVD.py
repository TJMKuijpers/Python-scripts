##################################################################################################
################## Function to calculate Singular Value Decomposition ############################
######################### T.J.M. Kuijpers 09 December 2021 #######################################
##################################################################################################

# import libraries
from scipy.linalg import svd
from sklearn.decomposition import TruncatedSVD
from sklearn.cluster import SpectralClustering

class calculateSVD:

    def __init__(self):
        self.data=None
        self.U=None
        self.s=None
        self.VT=None
        self.svd_truncated=None
        self.svd_truncated_fit = None
        self.svd_truncated_results = None
        self.spectral_clustering_results = None
        self.type='SVD'

    def set_data_svd(self,data):
        self.data=data

    def calculate_svd_solution(self):
        U,s,VT=svd(self.data)
        self.U=U
        self.s=s
        self.VT=VT

    def calculate_truncated_svd(self,number_of_compontents=None):
        svd_truncated=TruncatedSVD(n_components=number_of_compontents)
        self.svd_truncated=svd_truncated
        self.svd_truncated_fit=svd_truncated.fit(self.data)
        self.svd_truncated_results=svd_truncated.transform(self.data)

    def spectral_clustering(self,number_of_clusters=None,solver=None,set_affinity=None):
        s_cluster=SpectralClustering(n_clusters=number_of_clusters,eigen_solver=solver,affinity=set_affinity)
        s_cluster_fitted=s_cluster.fit_predict(self.data)
        self.spectral_clustering_results=s_cluster_fitted
