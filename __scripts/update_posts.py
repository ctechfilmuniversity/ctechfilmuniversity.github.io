import sys
import os

path_new_post = "__content/__new-post/"
path_existing_posts = "__content/"

def check_for_new_or_updated_posts():
    new_post_files = index_files_folders(True, path_new_post)
    #existing_posts = index_files_folders(false, path_existing_posts)

    if len(new_post_files) > 0:
        create_new_post(new_post_files)
    

def index_files_folders(return_files, path):
    files = []
    folders = []
    for (_, dirnames, filenames) in os.walk(path):
        folders.extend(dirnames)
        files.extend(filenames)
        break
    if return_files:
        return files
    else:
        return folders

def create_new_post(files):
    path = path_existing_posts + "test_folder"
    try:
        os.mkdir(path)
    except OSError:
        print ("Creation of the directory %s failed" % path)
    else:
        print ("Successfully created the directory %s " % path)

    print("####### test folder erstellt?")
    index_files_folders(false, path_existing_posts)

print("### Starting to look for new or updated content")
check_for_new_or_updated_posts()