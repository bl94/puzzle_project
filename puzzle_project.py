"""
Puzzle Project
"""
import zipfile
import os
import re

extract_files=zipfile.ZipFile('C:\\Users\\Bartlomiej Lepa\\Desktop\\Projects\\PuzzleProject\\unzip_me_for_instructions.zip','r')
extract_files.extractall('extract_files')

f=open('C:\\Users\\Bartlomiej Lepa\\Desktop\\Projects\\PuzzleProject\\extract_files\\extracted_content\\Instructions.txt','r+',encoding='UTF-8')
print(f.read())

PATH='C:\\Users\\Bartlomiej Lepa\\Desktop\\Projects\\PuzzleProject\\extract_files'
print(os.listdir())

for packages,subpackages,files in os.walk(PATH):
    print(f'Package : {packages}')
    for subpackage in subpackages:
        print(f'Subpackage : {subpackage}')
    for file in files:
        print(f'File: {file}')
        f=open(f'{file}',mode='r+',encoding='UTF-8')
        if
pattern=re.compile(r'(\d{3})-(\d{3})-(\d{4})')
match=re.findall(pattern,)
print(match)