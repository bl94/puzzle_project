"""
Puzzle Project
"""
import zipfile
import os
import re

extract_files=zipfile.ZipFile('C:\\Users\\Bartlomiej Lepa\\Desktop\\Projects\\PuzzleProject\\unzip_me_for_instructions.zip','r')
extract_files.extractall('')

PATH='C:\\Users\\Bartlomiej Lepa\\Desktop\\Projects\\PuzzleProject\\extracted_content'
def search(path):
    """
    listing files,searching number using regexp
    """
    for package,subpackages,files in os.walk(path):
        print(package)
        for file in files:
            opened_file=open(f'{package}\\{file}',mode='r+',encoding='UTF-8')
            lines_in_file=opened_file.read()
            pattern=re.compile(r'(\d{3})-(\d{3})-(\d{4})')
            match=re.findall(pattern,lines_in_file)
            if len(match)> 0:
                print(f"{package}\\{file}")
                print(match)
                break

search(PATH)
    