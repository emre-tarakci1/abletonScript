import os
from os import listdir
from os.path import isfile, join
from os import walk


class Project:
    MY_PATH = r'C:\Users\user\OneDrive\Belgeler\AbletonExports'
    projects = list()

    def update_projects(self):
        self.projects = [item for item in os.listdir(self.MY_PATH) if os.path.isdir(os.path.join(self.MY_PATH, item))]

    def __init__(self):
        self.update_projects()
        print(self.projects)

    def add_project(self, project_name):
        create_path = self.MY_PATH + r'\\' + project_name
        if os.path.exists(create_path):
            return "PROJECT_EXISTS"
        else:
            os.makedirs(create_path)
            return "SUCCESSFUL"

    def add_song(self, project_name, song_name):
        create_path = self.MY_PATH + r'\\' + project_name
        if not os.path.exists(create_path):
            return "UNDEFINED_PROJECT"

        create_path = create_path + r'\\' + song_name
        if os.path.exists(create_path):
            return "SONG_EXISTS"
        else:
            return "SUCCESSFUL"



'''
if not os.path.exists(mypath):
    os.makedirs(mypath)
'''


