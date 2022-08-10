import requests
import json

class ConnectToEncodeAPI:

    def __init__(self):
        self.database_name = 'Encode'
        self.url = 'https://www.encodeproject.org/'
        self.response_status_code = None
        self.biosample_response = None
        self.response_experiment = None
        self.md5_search = None
        self.response_fastq_search = None
        self.response_replicates = None
        self.response_search = None

    def check_database_connection(self):
        response=requests.get(self.url)
        if response.status_code != 200:
            print("Connection failed")
        self.response_status_code = response.status_code

    def search_for_biosample(self,accession_number=None):
        url = self.url+"biosample/"+accession_number+"/?frame=object"
        biosample_response = requests.get(url,headers={'accept': 'application/json'})
        self.biosample_response = biosample_response

    def general_search_on_key_word(self,key_word=None):
        tmp_url = self.url +"/search/?searchTerm="+key_word+"&frame=embedded&format=json"
        response_key_word = requests.get(tmp_url, headers={'accept': 'application/json'})
        self.response_search = response_key_word

    def search_file_on_md5(self,md5_code):
        tmp_url = self.url+"search/?type=File&md5sum="+md5_code+"&format=json"
        md5_response = requests.get(tmp_url, headers={'accept': 'application/json'})
        self.md5_search = md5_response

    def search_on_experiment(self,experiment_code):
        tmp_url = self.url+"search/?type=File&dataset=/experiments/"+experiment_code+"/&format=json&frame=object"
        reponse_experiment = requests.get(tmp_url,headers={'accept': 'application/json'})
        self.response_experiment = reponse_experiment

    def search_fastq_files_experiment(self,experiment_code):
        tmp_url = self.url+"/search/?type=File&dataset=/experiments/"+experiment_code+"+/&file_format=fastq&format=json&frame=object"
        response_fastq_search = requests.get(tmp_url, headers={'accept': 'application/json'})
        self.response_fastq_search = response_fastq_search

    def search_all_replicates_for_experiment(self,experiment_code):
        tmp_url = self.url +"/search/?type=Replicate&experiment.accession="+experiment_code+"&format=json"
        response_replicates = requests.get(tmp_url, headers={'accept': 'application/json'})
        self.response_replicates = response_replicates

if __name__ == "__main__":
    database = ConnectToEncodeAPI()
    database.check_database_connection()
    database.search_for_biosample(accession_number="ENCBS000AAA")
    database.search_on_experiment(experiment_code="ENCSR000AKS")
    database.search_all_replicates_for_experiment(experiment_code="ENCSR000AKS")
    database.search_fastq_files_experiment(experiment_code="ENCSR000AKS")
    database.search_file_on_md5("7b9f8ccd15fea0bda867e042db2b6f5a")
    database.general_search_on_key_word(key_word="CTCF")