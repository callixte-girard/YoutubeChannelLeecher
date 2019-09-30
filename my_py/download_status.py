from os import listdir


def countUnfinishedDownloads(path):
    counter = 0
    files = listdir(path)
    for file in files:
        if ".part" in file: counter += 1
    return counter


def isDownloadFinished(path, filename):
    files = listdir(path)
    if filename + ".part" in files: 
        return False
    else: 
        return True