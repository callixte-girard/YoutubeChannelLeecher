from my_py import disp


def getNewestFile(files_before, files_after):
    for file in files_after:
        if not file in files_before:
            return file
    return None