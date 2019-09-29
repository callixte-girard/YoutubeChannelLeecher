from my_py import disp

from os import walk


def readFilesInPath(full_path):
    # file = open(full_path)
    # lines = file.readlines
    # for line in lines:
    for (dirpath, dirnames, filenames) in walk(full_path):    
        # print(dirpath)
        for filename in filenames:
            print(filename)
            ### inspecter ceux qui contiennent .part et faire tout le ptit tintouin
            print(disp.line)
    return filenames


def getNewestFile(files_before, files_after):
    for file in files_after:
        if not file in files_before:
            return file
    return None