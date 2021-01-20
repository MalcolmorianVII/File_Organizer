import os
import json
import shutil

# cur_dir = os.getcwd()
# cur_files = os.listdir()
# print(cur_dir)
# getting file types in the dir & determine the files to move to their appropriate destination
# file_types = set([os.path.splitext(file)[1] for file in cur_dir])

vid_source = 'C:/Users/Belson/Videos'
aud_source = 'C:/Users/Belson/Music'
doc_source = 'C:/Users/Belson/Documents'
pics_source = 'C:/Users/Belson/Pictures'

with open("videos.json") as f:
    vid_json = json.load(f)

with open("audios.json") as a:
    aud_json = json.load(a)  # a list here

with open("files.json") as d:
    doc_json = json.load(d)

software = [".exe", ".apk", ".py", ".java", ".c", ".js", ".htm", ".html", ".rpm"]
zipped = [".zip", ".rar"]
pics = [".png", ".gif", ".svg", "jpeg", "tiff"]


# file aggregator : mainly for recursive purpose in case subfolders

def aggregator():
    """Total file compiler in  a particular folder to facilitate the move to appropriate destination"""
    cur_dir = os.getcwd()
    cur_files = os.listdir()
    # getting the files to move
    vid_files = [file for file in cur_files if os.path.splitext(file)[1] in vid_json]
    aud_files = [file for file in cur_files if os.path.splitext(file)[1] in aud_json]
    doc_files = [file for file in cur_files if os.path.splitext(file)[1] in doc_json]
    app_files = [file for file in cur_files if os.path.splitext(file)[1] in software]
    zip_files = [file for file in cur_files if os.path.splitext(file)[1] in zipped]
    pic_files = [file for file in cur_files if os.path.splitext(file)[1] in pics]
    folders = [file for file in cur_files if os.path.splitext(file)[1] == ""]

    # Recursive compilation in case of folder(s) in cur_dir
    if len(folders) > 0:
        # Need to chdir here into subfolder
        for folder in folders:
            try:
                os.chdir(os.path.join(cur_dir, folder))
                # cur_files = os.listdir(cur_dir)
                aggregator()
            except NotADirectoryError:
                continue

    print(cur_dir + ":" + str(cur_files))
    # destination = {f'{vid_files}': f'{vid_source}', f'{aud_files}': f'{aud_source}', f'{doc_files}': f'{doc_source}'
    #     , f'{pic_files}': f'{pics_source}'}
    #
    # for files in destination:
    #     for file in files:
    #         try:
    #             shutil.move(f'{cur_dir}/{file}', destination[files])
    #         except shutil.Error:
    #             print("Directory is empty!!!")


# aggregator()
