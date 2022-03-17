import os
import glob
import shutil

def get_last():
    # find last file in folder
    files_path = sorted(glob.glob("GoldHEN/*.bin"))
    last_file = files_path[-1]
    return last_file

os.mkdir("payload")
shutil.copy(get_last(), "payload/%s" % os.path.basename(get_last()))
shutil.rmtree("GoldHEN")
