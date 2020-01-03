import os
import ntpath
from shutil import copyfile
from datetime import datetime
import markdown

# user fills in:
    #start_path; line 13
    #main_destination_path, line 15


# folder that contains
start_path = r"xxx"
# folder for all subfolders and all submissions
main_destination_path = r"xxx"

html_supported_image_formats = ["bmp", "jpg", "jpeg", "png", "gif", "webp", "svg", "vml"]

#todo read csv in
authors = {
    "Bückner" : "Marcel B.",
    "Bueckner": "Marcel B.",
    "Beitel": "Jennifer B.",
    "Barvinska": "Valeria B.",
    "Clausen": "Phil C.",
    "Dittmann": "Markus D.",
    "Pätzold": "Franziska P.",
    "Paetzold": "Franziska P.",
    "Stimberg": "Simon S.",
    "Traber": "Markus T.",
    "Eperjesi": "Rita E.",
    "Maier": "Ismarah M.",
    "Daduna": "Phillip D.",
    "Nurmukhametova": "Ellina N.",
    "Eschenbacher": "Anna E.",
    "Tariq": "Zainab T.",
    "Lai": "Jacky L.",
    "Bischof": "Denise B."
}

# categories for github pages structure (modules)
categories = {
    "acadamic_methodologies": "AM",
    "creative_coding_i": "CCI",
    "creative_coding_ii": "CCII",
    "creative_technologies_i": "CTI",
    "creative_technologies_ii": "CTII",
    "procedural_generation_and_simulation": "PGS",
    "theoretical_backgrounds_for_audio_and_graphics": "TBAG"
}

error_list =[]

# holds the data for the current submission
# holds the data for the current submission
# curr_submission_data = dict(author="", date="", link="", text="", cover="", gallery=[])
curr_submission_data = {
    "title": "",
    "author": "",
    "date": "",
    "link": "",
    "text": "",
    "cover": "",
    "gallery": []
}


def print_errors():
    for error in error_list:
        print(error)


# iterate through folders
def publish_files(start_path):
    for root, dir, files in os.walk(start_path):
        level = root.replace(start_path, '').count(os.sep)
        indent = ' ' * 4 * (level)
        # print('{}{}/'.format(indent, os.path.basename(root)))
        # if the a folder is a submission folder, save its data
        if "submission_to_publish" in os.path.basename(root):
            clear_curr_submission()
            print("submission folder found")
            find_submitted_files(root, files)
            create_markdown_to_publish(root, main_destination_path)
        subindent = ' ' * 4 * (level + 1)
        # for f in files:
            # print('{}{}'.format(subindent, f))


def get_file_name(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


# clears dictionary to be ready to save new tuple
def clear_curr_submission():
    curr_submission_data["author"] = ""
    curr_submission_data["date"] = ""
    curr_submission_data["link"] = ""
    curr_submission_data["text"] = ""
    curr_submission_data["cover"] = ""
    curr_submission_data["gallery"] = []


# ToDo
# link
# curr_submission_data["link"] = create_github_link(root, repo)


def save_date():
    # save the date
    curr_submission_data["date"] = datetime.now().strftime("%Y-%m-%d")


# todo
# def create_github_link(root, repo):
#     link_base = "https://github.com/ctechfilmuniversity/"
#     link_extension = link_base + repo + "/tree/master"
#     final_link = link_extension + subfolder_path
#
#     return final_link



# create subfolder to save data
# returns path
def create_image_destination_folder():
    #TODO name
    #navigate to assets/img
    path_parts = main_destination_path.split("\\")
    path_parts_loop_condition = (part for part in path_parts if path_parts.index(part) < len(path_parts)-4)

    image_path = ""
    for part in path_parts_loop_condition:
        image_path += part + '\\'

    project_title = create_project_title()
    print("project title: " + project_title)
    current_destination_directory = image_path + 'assets\\img\\' + project_title
    try:
        os.makedirs(current_destination_directory)
    except FileExistsError:
        pass

    return current_destination_directory


# save submission content
def save_markdown_data(root, file_name):
    file_path = root + "\\" + file_name

    # open an read markdown
    submitted_file = open( file_path, 'r')
    submitted_content = markdown.markdown(submitted_file.read())

    # get title and body("text") from submitted markdown
    first_part = submitted_content.split("<h1>Title</h1>")
    second_part = first_part[0].split("<h2>Abstract</h2>")

    # get title (remove html tags)
    title_split_1 = second_part[0].split("<h1>")
    title_split_2 = title_split_1[1].split("</h1>")
    curr_title = title_split_2[0]
    curr_submission_data["title"] = curr_title
    curr_submission_data["text"] = "<h2>Abstract</h2>" + second_part[1]

    # get author
    author_flag = False
    for name in authors:
        if name.lower() in root:
            author_flag = True
            curr_submission_data["author"] = authors[name]
    if not author_flag:
        error_list.append("ERROR: Author not found. Either author is not in database or submission folder was named incorrectly: " + root)

    # create destination for images
    img_dst_path = create_image_destination_folder()

    return img_dst_path


def save_image_data(root, final_destination, file_name):
    src = root + '\\' + file_name
    dst = final_destination + '\\' + file_name
    copyfile(src, dst)

    if "cover" in file_name:
        curr_submission_data["cover"] = dst
    else:
        curr_submission_data["gallery"].append(dst)


# header to make github pages work
def create_front_matter(root):
    # layout
    # todo line break not working
    # todo: check if its nice to have html tags in markdown
    front_matter = ('---\n'
                    'layout: post\n')
    # title
    front_matter += "title: '" + curr_submission_data["title"] + "'\n"
    # author
    front_matter += "author: '" + curr_submission_data["author"] + "'\n"
    # categories
    category_found = False
    for category in categories:
        if category in main_destination_path:
            front_matter += "categories: " + categories.get(category) + "\n"
            category_found = True
    if not category_found:
        error_list.append("ERROR: category not found, project won't be displayed on website: " + root)
        front_matter += "categories: na\n"
    # cover image
    front_matter += "cover_image: '" + curr_submission_data["cover"] + "'\n"
    # cover image gallery todo
    front_matter += "gallery: \n"
    for image in curr_submission_data["gallery"]:
        #TODO relative path
        front_matter += "- path: '" + image + "'\n"
    # final ending of front matter
    front_matter += "---\n\n"

    return front_matter


# create title date + title + ending (16-12-2019-title.md)
def create_project_title():
    title_words = curr_submission_data["title"].split()
    title_length = len(title_words)
    curr_title = curr_submission_data["date"]
    curr_title += "-"
    word_counter = 0
    for word in title_words:
        word_counter += 1
        curr_title += word
        if title_length != word_counter:
            curr_title += "-"

    return curr_title

def create_markdown_to_publish(root, dst):
    curr_title = create_project_title()
    curr_markdown_title = curr_title + ".md"
    # create markdown file
    md = open(dst + "\\" + curr_markdown_title, "x")
    # create front matter
    front_matter = create_front_matter(root)
    # fill md with front matter
    md.write(front_matter)
    # add text/body to md
    md.write(curr_submission_data["text"])
    md.close()
    return curr_title

# if the function finds submitted data in correct data format it calls function to save their data
def find_submitted_files(root, files):
    # searching for markdowns and images, other data will occur an error
    save_date()
    image_destination_path = ""

    correct_data_format_flag = False
    # find markdown first to have basic data
    for file in files:
        file_name = get_file_name(file)

        #save markdown data
        if "md" in file_name:
            correct_data_format_flag = True
            image_destination_path = save_markdown_data(root, file_name)


    # save images in second iteration, to make sure every data is given to save images correctly
    for file in files:
        file_name = get_file_name(file)
        for data_format in html_supported_image_formats:
            if data_format in file_name:
                correct_data_format_flag = True
                save_image_data(root, image_destination_path, file_name)

    # if wrong file format was submitted, print error
    if not correct_data_format_flag:
        error_list.append("ERROR: wrong file format: {}{}".format(root, file_name))


################################Run Programme#########################################

publish_files(start_path)
print_errors()