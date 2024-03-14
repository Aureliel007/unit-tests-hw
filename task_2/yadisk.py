import requests

class YaDiskNewFolder:

    def __init__(self, token):          
        self.headers = {'Authorization': token}
        self.base_url = 'https://cloud-api.yandex.net/v1/disk/resources'

    def create_folder(self, folder_name='some_new_folder'):
        url = self.base_url
        params = {'path': folder_name}
        response = requests.put(url, params=params, headers=self.headers)
        return response
    
    def wrong_path(self, folder_name='some_wrong_path'):
        url = 'https://cloud-api.yandex.net/v1/disk/esources'
        params = {'path': folder_name}
        response = requests.put(url, params=params, headers=self.headers)
        return response