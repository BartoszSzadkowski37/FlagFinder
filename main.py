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
    fileText = str(fileText)
    print(fileText)

    fileText = fileText[2:len(fileText)-1]

    print(fileText)

    #this shit from the top doesn't work, so it should be an algorithm in loop

    bytesErase = False

    printable = ''

    while not bytesErase:
        if fileText[0] == '\\' and fileText[1] == 'x':
            fileText = fileText[4:]
        elif fileText[0] == '\\' and (fileText[1] == 'n' or fileText[1] == 't'):
            fileText = fileText[2:]
        else:
            printable += fileText[0]
            fileText = fileText[1:]

        if len(fileText) == 0:
            bytesErase = True

    print(printable)
    counter = 0
    row = ''
    for i in range(len(printable)):
        if counter == charSetLength:
            print(row)
            #print('\n')
            row = ''
            counter = 0
        row += printable[i]
        counter += 1





