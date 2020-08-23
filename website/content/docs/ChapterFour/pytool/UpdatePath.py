import os
import re
import glob

# file_name = 'Array.md'
reg = "docs/ChapterFour/(\d{4})"

def deal(number):
    folder = ['0001-0100/', 
              '0101-0200/', 
              '0201-0300/', 
              '0301-0400/', 
              '0401-0500/', 
              '0501-0600/', 
              '0601-0700/', 
              '0701-0800/',
              '0801-0900/',
              '0901-1000/',
              '1001-1100/',
              '1101-1200/',
              '1201-1300/',
              '1301-1400/',
              '1401-1500/']
    return "docs/ChapterFour/" + folder[(int(number)-1)//100] + number

current_working_dir = os.getcwd()
# print(f"current_working_dir: {current_working_dir}")

dir_names = glob.glob("*.md")

for file_name in dir_names:
    content = ""
    if not file_name.startswith("_index"):
        with open(file_name, 'r') as myfile:
            # stext = myfile.read()
            Lines = myfile.readlines() 
            count = 0
            for line in Lines: 
                findContent = re.search(reg, line)
                if findContent is not None:
                    number = findContent.group(1)
                    newContent = deal(number)
                    # print(newContent)
                    line = re.sub(reg, newContent, line)
                    # print(line)
                    count += 1
                content = content + line
        with open(file_name, "w") as myfile:
            myfile.write(content)
        print(file_name + " = " + str(count))