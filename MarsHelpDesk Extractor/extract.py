#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import yaml
import os

def convert_single_yml_to_txt(foldername,file):
    stream = open(foldername+"/"+file, "r")
    docs = yaml.load_all(stream)

    for doc in docs:
        for k, v in doc.items():
            if k == "categories":
                filename = v[0]
            elif k == "conversations":
                conversations = v
                questions = set([con[0] for con in conversations])


    if not os.path.exists(filename):
        #os.makedirs(filename)
        #newpath = filename+"/"+filename+"_test.txt"

        newpath = filename+"_test.txt"
        with open(newpath, 'w') as file_handler:
            for item in questions:
                file_handler.write("{}\n".format(item))

    else:
        print("请将之前版本移除后继续操作")


def extract(foldername, file):
    stream = open(foldername + "/" + file, "r")
    string_file = stream.read()
    list_str = string_file.split('\n')
    new_path = file[:-4] + "_extracted.txt"
    extracted_file = open(new_path, 'w+')

    question_list = []
    response_list = []

    for string in list_str:
        if string[0:4] == '- - ':
            question_list.append(string[4:])
        else:
            response_list.append(string[4:])

    extracted_question_str, extracted_response_str = '', ''
    for item in question_list:
        extracted_question_str += item + '\n'
    for item in response_list:
        extracted_response_str += item + '\n'
    extracted_file_str = extracted_question_str + '\n' + extracted_response_str

    extracted_file.write(extracted_file_str)
    extracted_file.close()
    stream.close()


# loop through files in the folder
for fn in os.listdir('chinese'):
    if fn[-4:] == ".txt":
        extract('chinese', fn)
