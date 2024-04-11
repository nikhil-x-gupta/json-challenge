from argparse import ArgumentParser
import time

from FileSourceProcessor import FileSourceProcessor


def get_config_field_sets(config):
    fieldSets = []
    with open(config) as cf:
        for line in cf:
            key, value = line.rstrip("\n").split("=")
            fieldSets.append(value)
    
    return fieldSets

def get_filenames(filenames):
    return filenames.split(',')

def get_args():
    parser = ArgumentParser(description = 'JSON processor')
    parser.add_argument('-f', '--filenames', type=str, required=True)
    parser.add_argument('-c', '--config', type=str, required=True)

    return parser.parse_args()


if __name__ == "__main__":    
    args = get_args()
    
    filenames = get_filenames(args.filenames)
    fieldSets = get_config_field_sets(args.config)

    index = 0
    fileSourceProcessor = None


    for filename in filenames:
        if fileSourceProcessor is None:
            fileSourceProcessor = FileSourceProcessor(filename, fieldSets)
        else:
            fileSourceProcessor.addFileSource(filename, fieldSets)
        
        fileSourceProcessor.processThread(index, False)
        index += 1

