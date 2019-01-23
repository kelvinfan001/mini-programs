"""
Module for translating PO files.
"""
from googletrans import Translator

# Translate msgid or msgstr?
TRANSLATE_MSGSTR = True

# Choose destination language:
LANG = 'zh-tw'

path = 'to_translate.txt'
new_path = 'translated_file.txt'

to_translate_file = open(path, 'r')
to_translate_file_string = to_translate_file.read()
to_translate_list = to_translate_file_string.split('\n')

translated_file = open(new_path, 'w+')

if __name__ == '__main__':

    # get indices that contain msgstr
    indices_to_edit = []
    for i in range(len(to_translate_list)):
        if to_translate_list[i][0:6] == 'msgstr':
            indices_to_edit.append(i)

    # translate and edit to_translate_list
    translator = Translator()
    if TRANSLATE_MSGSTR:
        for index in indices_to_edit:
            translated = translator.translate(to_translate_list[index][8:-1],
                                              dest=LANG)
            to_translate_list[index] = 'msgstr "' + translated.text + '"'
    else:
        for index in indices_to_edit:
            translated = translator.translate(to_translate_list[index
                                                                - 1][7:-1],
                                              dest=LANG)
            to_translate_list[index] = 'msgstr "' + translated.text + '"'

    # produce a string
    s = ''
    for line in to_translate_list:
        s += line + '\n'

    # write on file
    translated_file.write(s)
    translated_file.close()
    to_translate_file.close()
