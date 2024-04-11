from threading import Thread
from flatten_json import flatten, unflatten
import json
import time
from elasticsearch import Elasticsearch, helpers
import configparser

from FileSource import FileSource

class FileSourceProcessor:
    def __init__(self, filename, fieldSets):
        self.fileSources = []
        self.fileSources.append(FileSource(filename, fieldSets))
        self.esConfigFile = 'example.ini'
        self.esConnection = self.createElasticConnection(self.esConfigFile)
        print(self.esConnection.info())
       
    def createElasticConnection(self, configFile):
        config = configparser.ConfigParser()
        config.read(configFile)
        es = Elasticsearch(
            cloud_id=config['ELASTIC']['cloud_id'],
            http_auth=(config['ELASTIC']['user'], config['ELASTIC']['password'])
        )
        return es

    def addFileSource(self, filename, fieldSets):
        self.fileSources.append(FileSource(filename, fieldSets))

    def processThread(self, index, threaded):
        if threaded:
            Thread(target=self.process, args=(index,)).start()
        else:
            self.process(index)

    def process(self, index):
        
        start = time.time()
       
        data_line = self.fileSources[index].getLines()[1]
        data = json.loads(json.loads(data_line))

        # Flatten dictionary
        flat_data = flatten(data)

        """
        with open("flat_data.txt", 'w') as fd:
            fd.write(json.dumps(flat_data))
        """
        # Get values from flat dict based on fieldSets
        output = {}
        for fieldSet in self.fileSources[index].getFieldSets():
            output[fieldSet] = flat_data[fieldSet]
        
        #print("Flat output")
        #print(output)

        #print("JSON output")
        json_output = unflatten(output)
        print(json.dumps(json_output))

        self.sendData(output)

        end = time.time()
        print(end - start)

        return
    
    def sendData(self, data):
        self.esConnection.index(
            index='json-data',
            document=data
        )