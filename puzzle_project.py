"""
Puzzle Project
"""
import zipfile

extract_files=zipfile.ZipFile('C:\\Users\\Bartlomiej Lepa\\Desktop\\Projects\\PuzzleProject\\unzip_me_for_instructions.zip','r')
extract_files.extractall('extract_files')

f=open('C:\\Users\\Bartlomiej Lepa\\Desktop\\Projects\\PuzzleProject\\extract_files\\extracted_content\\Instructions.txt','r+',encoding='UTF-8')
print(f.read())
