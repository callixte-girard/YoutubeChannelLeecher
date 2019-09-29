from my_py import disp

from os import walk


def readFile(full_path):
    # file = open(full_path)
    # lines = file.readlines
    # for line in lines:
    for (dirpath, dirnames, filenames) in walk(full_path):    
        # print(dirpath)
        for filename in filenames:
            print(filename)
            ### inspecter ceux qui contiennent .part et faire tout le ptit tintouin
            print(disp.line)
    # return lines