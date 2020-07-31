from translate import Translator
import sys

'''
THIS TRANSLATOR USES THE TRANSLATE PACKAGE.
https://pypi.org/project/translate/

YOU CAN CHANGE THE TRANSLATE LANGUAGE BY CHANGING THE "ja" IN THE CODE BELOW TO THE COUNTRY SHORT CODE

https://en.wikipedia.org/wiki/ISO_639-1
Examples: (e.g. en, ja, ko, pt, zh, zh-TW, ...)

TO USE THIS ON THE COMMAND LINE
"python translator.py FILE_PATH" e.g "python translator.py test.txt"

IT OUTPUTS A FILE ENDING WITH "_trns" TO THE SAME FOLDER

'''

file_path = sys.argv[1]
translator = Translator(to_lang="ja")

try:
    with open(file_path, mode='r') as text_file:
        text = text_file.read()
        translation = translator.translate(text)
        with open(f'{file_path}_trns.txt', mode='w') as text_file2:
            text_file2.write(translation)
            print("Done!")
except FileNotFoundError:
    print('File not found!')
except IOError:
    print('Couldn\'t process translate')
