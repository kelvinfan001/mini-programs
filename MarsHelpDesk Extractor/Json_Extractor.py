"""
Module for extracting MarsHelpDesk json files.
Creates a new 'extracted_file.txt' with a list of all "texts" first, followed
by a blank line, followed by a list of all "intents" in the same order.
"""
path = 'MarsHelpdesk.txt'
new_path = 'extracted_file.txt'

json_file = open(path, 'r')
json_file_string = json_file.read()
help_desk_list = json_file_string.split('\n')

extracted_file = open(new_path, 'w+')

if __name__ == '__main__':
    extracted_text = []
    extracted_intents = []
    for i in range(len(help_desk_list) - 1):
        if help_desk_list[i][0:13] == '      "text":' \
                and help_desk_list[i + 1][0:22] != '      "intent": "None"':
            extracted_text.append(help_desk_list[i][15:-2])
            extracted_intents.append(help_desk_list[i + 1][17:-2])
    extracted_text_str, extracted_intents_str = '', ''
    for item in extracted_text:
        extracted_text_str += item + '\n'
    for item in extracted_intents:
        extracted_intents_str += item + '\n'
    extracted_file_str = extracted_text_str + '\n' + extracted_intents_str

    extracted_file.write(extracted_file_str)
    extracted_file.close()
    json_file.close()
