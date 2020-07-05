from pathlib import Path
from File import File
import re
import codecs


run = True



# main loop
while run:
    path = ''
    charSetLength = ''
    ifExists = False
    # get file path and check validity
    while not ifExists:
        print('Provide valid file path: ')
        path = input()
        path = Path(path)
        print(path)
        print(path.exists())
        if path.exists():
            ifExists = True
            print(ifExists)

    # get length of characters set and check validity
    while type(charSetLength) != int:
        charSetLength = input('Provide valid length of the characters set: ')
        try:
            charSetLength = int(charSetLength)
        except:
            print('Incorrect value!')

    # creating file object and open it
    file = File(path)
    with open(file.path, 'rb') as fileText:
        fileText = fileText.read()
    print(fileText)

    # creating regex object to find printable sets of signs
    charSetReg = re.compile()
    fileText = str(fileText)
    print(fileText)
    print(charSetReg.findall(fileText))
