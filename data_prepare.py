# Reformat wiki text => Get text for content format
import os
import pandas as pd
import json
import shutil

# Optional: Turn all file to Json if all dump files had no extension
''' 
for count, filename in enumerate(os.listdir(path)):
    dst ="viwiki" + str(count) + ".json"
    src =path+ filename
    dst =path+ dst
    # rename() function will
    # rename all the files
    os.rename(src, dst)
'''
#####################################################################
path="Wiki_Data/wiki/" # path to json file of viwiki
count=0

# Convert file to txt => Hay-stack format
for count, filename in enumerate(os.listdir(path)):
        dst ="Wiki_Data/fmt_txt/viwiki" + str(count) + ".txt"
        src =path + filename
        wiki=pd.read_json(src,lines=True)
        list_doc=[]
        list_doc = [con.strip() for con in wiki['text'] if con!=''] #(! null and delete newline)
        txt=' '.join(list_doc) # merge to one document
        with open(dst, 'wb') as fp:
            fp.write(txt.encode('utf-8'))
            print(src)#test

#################################################################################
# split in to sub folder
source = 'Wiki_Data/fmt_txt/'
N = 150  # the number of files in seach subfolder folder
def move_files(abs_dirname):
    #Move files into subdirectories
    files = [os.path.join(abs_dirname, f) for f in os.listdir(abs_dirname)]

    i = 0
    curr_subdir = None
    files.sort()
    for f in files:
        # create new subdir if necessary
        if i % N == 0:
            subdir_name = os.path.join(abs_dirname, '{0:03d}'.format(i // N + 1))
            os.mkdir(subdir_name)
            curr_subdir = subdir_name

        # move file to current dir
        f_base = os.path.basename(f)
        shutil.move(f, os.path.join(subdir_name, f_base))
        i += 1
move_files(source)