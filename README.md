# json-challenge

This is my solution for a PoC coding challenge I was given.

## Problem Statement
The input will be a file containing a complex nested JSON with additional text, as well as a config file with the desired field names.

The input data file must be flattened and then the requested data (as per the config file) must be parsed out and stored on a searchable data store.

The input can come at high frequency, so the application should be designed to handle large volumes of data efficiently.

## Solution
The assumption was made that the config file was given in the following format:
```
fieldSet1=id
fieldSet2=equipmentModel_id
fieldSet3=equipmentModel_equipmentType_id
fieldSet4=equipmentModel_supplier_0_id
.
.
.
```
This aligned with the standard output of JSON flattening, using snakecase format and adding numbers to represent values originally organized in an array in the nested JSON.

`json_main.py` takes input file arguments with the tag `-f`, with multiple files separated by commas, and the input config file with the tag `-c`.
For example:
```
python json_main.py -f file1,file2,file3 -c config1
```
For storing the data, I used Elasticsearch, following the instructions here: https://www.elastic.co/guide/en/cloud/current/ec-getting-started-python.html

In summary, run 
```
pip install elasticsearch
pip install elasticsearch-async
```
and add an `example.ini` file with your Elasticsearch credentials, as specified in the link.
