import os

def listDir(dir, type = None):
    listedDir = []
    for name in os.listdir(dir):
        if type is None:
            listedDir.append(name)
        elif type == 'file':
            if isFile(dir, name):
                listedDir.append(name)
        elif type == 'folder':
            if isFile(dir, name) == False:
                listedDir.append(name)
    return listedDir

def listFiles(dir):
    return listDir(dir, 'file')

def listFolders(dir):
    return listDir(dir, 'folder')

def listModules():
    return listDir('./app/modules/', 'folder')

def isFile(name):
    return os.path.isfile(os.path.join(name))
