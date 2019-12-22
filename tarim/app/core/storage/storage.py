from datetime import datetime
import os
import uuid

class Storage():
    def __init__(self, disk = 'local'):
        self.disk = disk


    def getDriver(self):
        if self.disk is 'local':
            return Local(self,{
                ""
            })

    def move(self, file):
        self.file = file
        self.setName()
        driver = self.getDriver()
        driver.move(file)
        return self

    def setName(self, hash = True, name = None):
        if hash:
            self.name = uuid.uuid4().hex
        elif name:
            self.name = name
        else:
            self.name = self.getOriginalNameNoExtention()

    def getOriginalName(self):
        return self.file.filename

    def getOriginalNameNoExtention(self):
        return self.getOriginalName().replace('.'+self.getExtension(), '')

    def getExtension(self):
        return self.file.filename.split('.')[1]

    def getFilename(self):
        return self.name+"."+self.getExtension()

    def getMimeType(self):
        return self.file.mimetype

    def getVisualFolder(self):
        today = datetime.now()
        folder = "storage/" + today.strftime('%Y/%m/%d')+"/"
        return folder

    def getPhysicalFolder(self):
        path = os.getcwd()+"/app/"+self.getVisualFolder()
        if not os.path.exists(path):
            os.makedirs(path)
        return path

    def getUploadFolder(self):
        return self.getPhysicalFolder()+self.getFilename()

    def getSize(self):
        return os.stat(self.getUploadFolder()).st_size


    def getAsDict(self):
        return {
            'name': self.name,
            'path': self.getVisualFolder(),
            'original_name': self.getOriginalName(),
            'disk': self.disk,
            'mime': self.getMimeType(),
            'extension': self.getExtension(),
            'size': self.getSize()
        }

class Local():
    def __init__(self, storage, config):
        self.config = config
        self.storage = storage

    def move(self, file):
        file.save(self.storage.getUploadFolder())
