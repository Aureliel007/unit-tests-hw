# from configparser import ConfigParser

# import pytest

# from yadisk import YaDiskNewFolder


# class TestYaDiskNewFolder:

#     def setup_method(self):
#         settings = ConfigParser()
#         settings.read('settings.ini')
#         token = settings['Yadisk']['token']
#         self.yadisk = YaDiskNewFolder(token)

#     def teardown_method(self):
#         del self.yadisk

#     def test_create_folder(self):
#         response = self.yadisk.create_folder('one_more_folder')
#         assert response.status_code == 201

#     def test_folder_exists(self):
#         self.yadisk.create_folder('folder_exists')
#         response = self.yadisk.create_folder('folder_exists')
#         assert response.status_code == 409

#     def test_wrong_path(self):
#         response = self.yadisk.wrong_path()
#         assert response.status_code == 404


    