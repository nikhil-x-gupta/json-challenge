class FileSource:
    def __init__(self, filename, fieldSets):
        self.filename = filename
        self.fieldSets = fieldSets
        self.lines = ""
        self.readFile()


    def readFile(self):
         with open(self.getFilename(), 'r') as fp:
            self.lines = fp.readlines()

    def getFilename(self):
        return self.filename
    
    def getFieldSets(self):
        return self.fieldSets
    
    def getLines(self):
        return self.lines
    
    def setFilename(self, filename):
        self.filename = filename
    
    def setFieldSets(self, fieldSets):
        self.fieldSets = fieldSets