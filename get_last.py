import os
import glob
import shutil

def get_last(folder=""):
    # find last file in folder
    if folder:
      files_path = sorted(glob.glob("{0}/*.bin".format(folder)))
    else:
      files_path = sorted(glob.glob("GoldHEN/*.bin"))
    last_file = files_path[-1]
    return last_file

if __name__ == '__main__':
    os.mkdir("payload")
    shutil.copy(get_last(), "payload/%s" % os.path.basename(get_last()))
    shutil.rmtree("GoldHEN")
    
