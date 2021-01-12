import os
import json
import shutil

cur_dir = os.getcwd()
cur_files = os.listdir()
# print(cur_dir)
# getting file types in the dir & determine the files to move to their appropriate destination
file_types = set([os.path.splitext(file)[1] for file in cur_dir])
# file_type & action link
# action = {'.mp4'}
vid_source = 'C:/Users/Belson/Videos'
aud_source = 'C:/Users/Belson/Music'
doc_source = 'C:/Users/Belson/Documents'

with open("videos.json") as f:
    vid_json = json.load(f)

with open("audios.json") as a:
    aud_json = json.load(a)  # a list here

with open("files.json") as d:
    doc_json = json.load(d)


# print(vid_json)

def vids(videos):
    if len(videos):
        for file in videos:
            shutil.move(f'{cur_dir}/{file}', f'{vid_source}')
        print('Videos moved successfully')
    else:
        print("No videos to move")


def auds(audios):
    if len(audios) > 0:
        for file in audios:
            shutil.move(f'{cur_dir}/{file}', f'{aud_source}')
        print('Audios moved successfully')
    else:
        print("No audio files to move")


def docs(documents):
    if len(documents) > 0:
        for file in documents:
            shutil.move(f'{cur_dir}/{file}', f'{doc_source}')
        print('Docs moved successfully')
    else:
        print('No Documents to move')


# getting the files to move
vid_files = [file for file in cur_files if os.path.splitext(file)[1] in vid_json]
aud_files = [file for file in cur_files if os.path.splitext(file)[1] in aud_json]
doc_files = [file for file in cur_files if os.path.splitext(file)[1] in doc_json]
# alt:doc_files = [file for file in cur_files if os.path.splitext(file)[1] not in vid_json and aud_json]


def all():
    vids(vid_files)
    auds(aud_files)
    docs(doc_files)
# moving the files
# vids(vid_files)
# auds(aud_files)
# docs(doc_files)
