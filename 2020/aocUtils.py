import requests
from pathlib import Path
import os
import datetime

def loadInputFile(year, day):
    filePath = f'.\\day{day}.txt'
    if (not Path(filePath).is_file()):
        with open(f'..\\SessionCookie.txt', 'r') as s:
            sessionCookie = s.readline()
        cookies = {'session': sessionCookie}
        req = requests.get(f'https://adventofcode.com/{year}/day/{day}/input', cookies=cookies)
        if req.status_code >= 400:
            raise Exception(req.text)
        with open(filePath, 'w') as newFile:
            newFile.write(req.text)
    return open(filePath, 'r')

def loadInputLines(year, day):
    with loadInputFile(year, day) as f:
        lines = f.read().splitlines()
        printT('Input Loaded')
        return lines

def loadInput(year, day):
    with loadInputFile(year, day) as f:
        return f.read().strip()

def printT(message):
    print(datetime.datetime.now().strftime('%M:%S.%f') + ': ' + str(message))