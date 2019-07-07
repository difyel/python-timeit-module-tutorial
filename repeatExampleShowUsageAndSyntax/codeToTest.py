import re
import timeit


def splitUsingRegex(messageToSplit: str, separator: str = '\s'):
    ''' Split a message using the provided separator

        messageToSplit : string
        separator : default '\s'  which is ' \t\n\r\x0b\x0c'  hence white space
    '''
    patternOfSeparator = f'([^{separator}]+)'
    messageWordList = re.findall(patternOfSeparator, messageToSplit)
    return messageWordList


def splitUsingLoop(messageToSplit: str, separator: str = [' ', '\t', '\n', '\r', '\x0b', '\x0c']):
    ''' Split a message using only loops

        messageToSplit : string
        separator : default  [' ', '\t', '\n', '\r', '\x0b', '\x0c'] which is '\s' which is whitespace
    '''
    messageWordList = []
    word = []
    for char in messageToSplit:
        word.append(char)
        for sep in separator:
            if char == sep:
                word.pop()
                if len(word) != 0:
                    messageWordList.append(''.join(word))
                    word = []
                break
    if word != []:
        messageWordList.append(''.join(word))
    return messageWordList
