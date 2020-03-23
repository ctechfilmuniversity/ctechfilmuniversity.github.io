import sys
import os
import re
import shutil
from datetime import datetime

path_new_post = "__content/new-post/"
path_existing_posts = "__content/"

path_jekyll_post_md = "_posts/projects/"
path_jekyll_post_pics = "assets/img/projects/"


def check_for_new_or_updated_posts():
    new_post_files = index_files_folders(True, path_new_post)
    new_post_files.remove("readme.md")
    if len(new_post_files) > 0:
        create_new_post(new_post_files)

    existing_posts = index_files_folders(False, path_existing_posts)
    existing_posts.remove("new-post")
    if len(existing_posts) > 0:
        copy_post_files_to_destination(existing_posts)
    

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
    r = re.compile(".*.md")
    text = list(filter(r.match, files)) # Read Note

    if len(text) > 0:
        now = datetime.now()
        dt_string = now.strftime("%Y-%m-%d-")

        path = path_existing_posts +  dt_string + text[0].replace(".md", "")
        
        if create_directory(path):
            for file in files:
                if ".md" in file:
                    shutil.copy2(path_new_post + file, path + "/" + dt_string + file)
                else:
                    shutil.copy2(path_new_post + file, path)
                
                # Delete file in origin
                os.remove(path_new_post + file)


def create_directory(path):
    if os.path.exists(path):
        print("Project folder already exists: " + path)
        return True
    else:
        try:
            os.mkdir(path)
        except OSError:
            print ("Creation of the directory %s failed" % path)
            return False
        else:
            print ("Successfully created the directory %s " % path)
            return True


def copy_post_files_to_destination(existing_posts):
    regex_md_pictures = re.compile(r"(!\[.*\]\()(.*\))", re.IGNORECASE)
    regex_cover_image = re.compile(r"(cover-image:\s?)(.*)", re.IGNORECASE)

    for post_folder in existing_posts:
        full_path_post_folder = path_existing_posts + post_folder + "/"
        files = index_files_folders(True, full_path_post_folder)
        print(files)

        for file in files:
            path_pictures = path_jekyll_post_pics + post_folder + "/"

            if ".md" in file:
                shutil.copy2(full_path_post_folder + file, path_jekyll_post_md)

                # Edit picture paths
                mdFile = open(path_jekyll_post_md + file, "r")
                mdFileContent = mdFile.read()
                mdFile.close()

                mdFileContent = regex_md_pictures.sub("\g<1>" + "/" + path_pictures + "\g<2>", mdFileContent)
                mdFileContent = regex_cover_image.sub("\g<1>" + "/" + path_pictures + "\g<2>", mdFileContent)

                mdFile = open(path_jekyll_post_md + file, "w")
                mdFile.write(mdFileContent)
                mdFile.close()
            else:
                if (create_directory(path_pictures)):
                    shutil.copy2(full_path_post_folder + file, path_pictures)
                else:
                    print("Could not update file: " + file + " in directory: " + path_pictures)


print("### Starting to look for new or updated content")
check_for_new_or_updated_posts()