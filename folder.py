import os

def get():
    os.chdir(os.path.dirname(__file__))
    return(os.getcwd()+'\\slike\\')
